<pre><code>    __ __ __   ___    __ __  _ ____   ___   ___  __  _ _      ____ 
   /  ]  |  | /  _]  /  ]  |/ ]    \ /   \ /   \|  |/ ] |    /    |
  /  /|  |  |/  [_  /  /|  ' /|  o  )     |     |  ' /| |   |  o  |
 /  / |  _  |    _]/  / |    \|     |  O  |  O  |    \| |___|     |
/   \_|  |  |   [_/   \_|     \  O  |     |     |     \     |  _  |
\     |  |  |     \     |  .  |     |     |     |  .  |     |  |  |
 \____|__|__|_____|\____|__|\_|_____|\___/ \___/|__|\_|_____|__|__|
                                                                   </code></pre>

A periodically updated archive of financial data published by the city of Los Angeles' [Checkbook LA](https://controllerdata.lacity.org/) data portal.

What it tracks
--------------

|Data set|Row count|Last download|   |   |
|:--------|--------:|:-----------|:--|:--|
|[eCheckbook Data](https://controllerdata.lacity.org/Finance/eCheckbook-Data/pggv-e4fn)|111713|2013-11-11 17:50:03.452753|[CSV](csv/eCheckbook Data.csv)|[JSON](json/eCheckbook Data.json)|
|[General Fund Revenue](https://controllerdata.lacity.org/Finance/General-Fund-Revenue/hfus-a659)|2791|2013-11-11 17:50:03.452753|[CSV](csv/General Fund Revenue.csv)|[JSON](json/General Fund Revenue.json)|
|[Neighborhood Council Expenditures](https://controllerdata.lacity.org/Finance/Neighborhood-Council-Expenditures/f2ec-m4t9)|464|2013-11-11 17:50:03.452753|[CSV](csv/Neighborhood Council Expenditures.csv)|[JSON](json/Neighborhood Council Expenditures.json)|
|[Payroll](https://controllerdata.lacity.org/Finance/Payroll/qjfm-3srk)|150997|2013-11-11 17:50:03.452753|[CSV](csv/Payroll.csv)|[JSON](json/Payroll.json)|
|[General Fund Budget Expenditures](https://controllerdata.lacity.org/Finance/General-Fund-Budget-Expenditures/uyzw-yi8n)|1916|2013-11-11 17:50:03.452753|[CSV](csv/General Fund Budget Expenditures.csv)|[JSON](json/General Fund Budget Expenditures.json)|


Getting started
---------------

Create a virtual enviroment to work inside.

```bash
$ virtualenv --no-site-packages checkbook-la-watchdog
```

Jump in and turn it on.

```bash
$ cd checkbook-la-watchdog
$ . bin/activate
```

Clone the git repository from GitHub.

```bash
$ git clone git@github.com:datadesk/checkbook-la-watchdog.git repo
```

Enter the project and install its dependencies.

```bash
$ cd repo
$ pip install -r requirements.txt
```

Run the script to get the latest files.

```bash
$ python watchdog.py
```