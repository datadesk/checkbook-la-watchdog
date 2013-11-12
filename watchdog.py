import os
import csv
import requests
from jinja2 import Template
from datetime import datetime
from hurry.filesize import size
from dateutil.parser import parse as dateparse


class Watchdog(object):
    """
    Tricks for downloading and archiving Checkbook LA data.
    """
    file_list = {
        'eCheckbook Data': 'pggv-e4fn',
        'General Fund Revenue': 'hfus-a659',
        'Neighborhood Council Expenditures': 'f2ec-m4t9',
        'Payroll': 'qjfm-3srk',
        'General Fund Budget Expenditures': 'uyzw-yi8n',
    }
    url_template = 'https://controllerdata.lacity.org/api/views/%s/rows.csv?accessType=DOWNLOAD'
    headers = {
        'User-agent': 'Los Angeles Times Data Desk (datadesk@latimes.com)'
    }

    def set_options(self):
        self.now = datetime.now()
        self.this_dir = os.path.dirname(os.path.realpath(__file__))
        self.csv_dir = os.path.join(self.this_dir, 'csv')
        self.template_dir = os.path.join(self.this_dir, 'templates')
        os.path.exists(self.csv_dir) or os.mkdir(self.csv_dir)

    def run(self):
        self.set_options()
        for name, id_ in self.file_list.items():
            url = self.url_template % id_
            print "Downloading %s CSV" % (name)
            self.download(url, "%s.csv" % name)
        self.update_log()

    def download(self, url, csv_name):
        """
        Download a file in pieces.
        """
        r = requests.get(url, headers=self.headers, stream=True)
        csv_path = os.path.join(self.csv_dir, csv_name)
        with open(csv_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()

    def update_log(self):
        template_path = os.path.join(self.template_dir, 'README.md')
        template_data = open(template_path, 'r').read()
        template = Template(template_data)
        dict_list = []
        for name, id_ in self.file_list.items():
            csv_name = "%s.csv" % name
            csv_path = os.path.join(self.csv_dir, csv_name)
            csv_reader = csv.reader(open(csv_path, 'r'))
            dict_list.append({
                'name': name,
                'row_count': len(list(csv_reader)),
                'last_updated': str(self.now),
                'csv_name': csv_name,
            })
        out_data = template.render(file_list=dict_list)
        out_file = open(os.path.join(self.this_dir, 'README.md'), 'w')
        out_file.write(out_data)
        out_file.close()


if __name__ == '__main__':
    wd = Watchdog()
    wd.run()
