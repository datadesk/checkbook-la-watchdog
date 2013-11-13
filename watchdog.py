import os
import csv
import envoy
import requests
from jinja2 import Template
from datetime import datetime
from hurry.filesize import size
from BeautifulSoup import BeautifulSoup
from dateutil.parser import parse as dateparse


class Watchdog(object):
    """
    Tricks for downloading and archiving Checkbook LA data.
    """
    format_list = ['csv', 'json']
    url_template = 'https://controllerdata.lacity.org/api/views/%(id)s/\
rows.%(format)s?accessType=DOWNLOAD'
    headers = {
        'User-agent': 'Los Angeles Times Data Desk (datadesk@latimes.com)'
    }
    catalog_url = 'https://controllerdata.lacity.org/browse?limitTo=datasets\
&sortBy=alpha&view_type=table&limit=1000'

    def handle(self, *args, **kwargs):
        """
        Make everything happen
        """
        print "Running the checkbook la watchdog"
        self.set_options()
        [self.download(f) for f in self.file_list[1:2]]
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
        # Discover all the files we're going to download
        self.get_file_list()

    def get_file_list(self):
        """
        Scrape all of the "datasets" published by the controller.
        """
        r = requests.get(self.catalog_url, headers=self.headers)
        soup = BeautifulSoup(r.text)
        row_list = soup.find("table", {"class": "gridList"}).findAll("tr")
        self.file_list = []
        for row in row_list[1:]:
            cell = row.find("td", { "class": "nameDesc" })
            data = cell.find("a", {"class": "name"})
            name = data.string
            url = data['href']
            self.file_list.append({
                'name': name,
                'url': url,
                'id': url.split("/")[-1],
            })

    def download(self, obj):
        """
        Download a file in pieces.
        """
        for format_ in self.format_list:
            url = self.url_template % dict(
                format=format_,
                id=obj['id'],
            )
            file_name = '%s.%s' % (obj['name'], format_)
            print "- Downloading %s in %s format" % (obj['name'], format_)
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
        diff = envoy.run("git diff --stat").std_out
        out_data = template.render(file_list=dict_list, diff=diff)
        out_file = open(os.path.join(self.this_dir, 'README.md'), 'w')
        out_file.write(out_data)
        out_file.close()

    def update_github(self):
        """
        Commit changes and push them to GitHub
        """
        print "- Updating GitHub"
        r = envoy.run("git add --all")
        self.update_log()
        r = envoy.run("git add --all")
        envoy.run("git commit --file=%s" % os.path.join(
            self.template_dir,
            'commit.txt'
        ))
        envoy.run("git push origin master")


if __name__ == '__main__':
    wd = Watchdog()
    wd.handle()
