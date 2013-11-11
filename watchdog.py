import requests
import os
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
        self.this_dir = os.path.dirname(os.path.realpath(__file__))
        self.csv_dir = os.path.join(self.this_dir, 'csv')
        os.path.exists(self.csv_dir) or os.mkdir(self.csv_dir)

    def run(self):
        self.set_options()
        for name, id_ in self.file_list.items():
            url = self.url_template % id_
            print "Downloading %s CSV" % (name)
            self.download(url, "%s.csv" % name)

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


if __name__ == '__main__':
    wd = Watchdog()
    wd.run()
