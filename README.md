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
|[Audits](https://controllerdata.lacity.org/Finance/Audits/n66v-7d9g)|371|2013-11-29 18:30:02.242789|[CSV](csv/Audits.csv)|[JSON](json/Audits.json)|
|[Catalog](https://controllerdata.lacity.org/dataset/Catalog/hpxk-2i55)|97|2013-11-29 18:30:02.242789|[CSV](csv/Catalog.csv)|[JSON](json/Catalog.json)|
|[eCheckbook Data](https://controllerdata.lacity.org/Finance/eCheckbook-Data/pggv-e4fn)|144521|2013-11-29 18:30:02.242789|[CSV](csv/eCheckbook Data.csv)|[JSON](json/eCheckbook Data.json)|
|[General Fund Budget Expenditures](https://controllerdata.lacity.org/Finance/General-Fund-Budget-Expenditures/uyzw-yi8n)|1923|2013-11-29 18:30:02.242789|[CSV](csv/General Fund Budget Expenditures.csv)|[JSON](json/General Fund Budget Expenditures.json)|
|[General Fund Revenue](https://controllerdata.lacity.org/Finance/General-Fund-Revenue/hfus-a659)|2809|2013-11-29 18:30:02.242789|[CSV](csv/General Fund Revenue.csv)|[JSON](json/General Fund Revenue.json)|
|[Home Page Featured Scrolling Stories](https://controllerdata.lacity.org/Internal/Home-Page-Featured-Scrolling-Stories/hmvt-bjfk)|5|2013-11-29 18:30:02.242789|[CSV](csv/Home Page Featured Scrolling Stories.csv)|[JSON](json/Home Page Featured Scrolling Stories.json)|
|[Home Page Stories](https://controllerdata.lacity.org/Internal/Home-Page-Stories/uuhh-hvvk)|8|2013-11-29 18:30:02.242789|[CSV](csv/Home Page Stories.csv)|[JSON](json/Home Page Stories.json)|
|[Los Angeles City Payroll Calendar](https://controllerdata.lacity.org/dataset/Los-Angeles-City-Payroll-Calendar/anqa-iu8a)|256|2013-11-29 18:30:02.242789|[CSV](csv/Los Angeles City Payroll Calendar.csv)|[JSON](json/Los Angeles City Payroll Calendar.json)|
|[Messages](https://controllerdata.lacity.org/Internal/Messages/dsnd-us3j)|3|2013-11-29 18:30:02.242789|[CSV](csv/Messages.csv)|[JSON](json/Messages.json)|
|[Neighborhood Council Expenditures](https://controllerdata.lacity.org/Finance/Neighborhood-Council-Expenditures/f2ec-m4t9)|464|2013-11-29 18:30:02.242789|[CSV](csv/Neighborhood Council Expenditures.csv)|[JSON](json/Neighborhood Council Expenditures.json)|
|[Payroll](https://controllerdata.lacity.org/Finance/Payroll/qjfm-3srk)|151539|2013-11-29 18:30:02.242789|[CSV](csv/Payroll.csv)|[JSON](json/Payroll.json)|
|[Templates](https://controllerdata.lacity.org/dataset/Templates/jbxg-3qpc)|1|2013-11-29 18:30:02.242789|[CSV](csv/Templates.csv)|[JSON](json/Templates.json)|


What changed in last download
-----------------------------

```bash
Nothing
```

What you can do
---------------

* Try it out and report bugs.
* Figure out ways to build notifications, visualizations or another application on top of the shifting data.
* Try forking it and making it go on a Socrata based data site in your city.
* Or just modify it to work off any old public data set.

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