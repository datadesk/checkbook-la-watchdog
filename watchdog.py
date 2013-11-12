import os
import csv
import envoy
import requests
from jinja2 import Template
from datetime import datetime
from hurry.filesize import size
from dateutil.parser import parse as dateparse


class Watchdog(object):
    """
    Tricks for downloading and archiving Checkbook LA data.
    """
    file_list = [
        dict(name='eCheckbook Data', id='pggv-e4fn', url='https://controllerdata.lacity.org/Finance/eCheckbook-Data/pggv-e4fn'),
        dict(name='General Fund Revenue', id='hfus-a659', url='https://controllerdata.lacity.org/Finance/General-Fund-Revenue/hfus-a659'),
        dict(name='Neighborhood Council Expenditures', id='f2ec-m4t9', url='https://controllerdata.lacity.org/Finance/Neighborhood-Council-Expenditures/f2ec-m4t9'),
        dict(name='Payroll', id='qjfm-3srk', url='https://controllerdata.lacity.org/Finance/Payroll/qjfm-3srk'),
        dict(name='General Fund Budget Expenditures', id='uyzw-yi8n', url='https://controllerdata.lacity.org/Finance/General-Fund-Budget-Expenditures/uyzw-yi8n'),
    ]
    format_list = ['csv', 'json']
    url_template = 'https://controllerdata.lacity.org/api/views/%(id)s/\
rows.%(format)s?accessType=DOWNLOAD'
    headers = {
        'User-agent': 'Los Angeles Times Data Desk (datadesk@latimes.com)'
    }

    def handle(self, *args, **kwargs):
        """
        Make everything happen
        """
        print "Running the checkbook la watchdog"
        self.set_options()
        [self.download(f) for f in self.file_list]
        self.update_log()
        self.update_github()

    def set_options(self):
        """
        Prep everything.
        """
        self.now = datetime.now()
        # Set template paths
        self.this_dir = os.path.dirname(os.path.realpath(__file__))
        self.template_dir = os.path.join(self.this_dir, 'templates')
        self.csv_dir = os.path.join(self.this_dir, 'csv')
        self.json_dir = os.path.join(self.this_dir, 'json')
        # Make sure template paths exist
        os.path.exists(self.csv_dir) or os.mkdir(self.csv_dir)
        os.path.exists(self.json_dir) or os.mkdir(self.json_dir)

    def download(self, obj):
        """
        Download a file in pieces.
        """
        print "- Downloading data"
        for format_ in self.format_list:
            url = self.url_template % dict(
                format=format_,
                id=obj['id'],
            )
            file_name = '%s.%s' % (obj['name'], format_)
            print "-- Downloading %s in %s format" % (obj['name'], format_)
            r = requests.get(url, headers=self.headers, stream=True)
            file_path = os.path.join(getattr(self, '%s_dir' % format_), file_name)
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()

    def update_log(self):
        """
        Log activity to the README file.
        """
        print "- Updating log"
        template_path = os.path.join(self.template_dir, 'README.md')
        template_data = open(template_path, 'r').read()
        template = Template(template_data)
        dict_list = []
        for obj in self.file_list:
            csv_name = "%s.csv" % obj['name']
            csv_path = os.path.join(self.csv_dir, csv_name)
            csv_reader = csv.reader(open(csv_path, 'r'))
            json_name = "%s.json" % obj['name']
            dict_list.append({
                'name': obj['name'],
                'row_count': len(list(csv_reader)),
                'last_updated': str(self.now),
                'csv_name': csv_name,
                'json_name': json_name,
                'url': obj['url'],
            })
        out_data = template.render(file_list=dict_list)
        out_file = open(os.path.join(self.this_dir, 'README.md'), 'w')
        out_file.write(out_data)
        out_file.close()

    def update_github(self):
        """
        Commit changes and push them to GitHub
        """
        print "- Updating GitHub"
        r = envoy.run("git add --all")
        #print r.status_code
        envoy.run("git commit --file=%s" % os.path.join(
            self.template_dir,
            'commit.txt'
        ))
        #print r.status_code
        envoy.run("git push origin master")
        #print r.status_code


if __name__ == '__main__':
    wd = Watchdog()
    wd.handle()
