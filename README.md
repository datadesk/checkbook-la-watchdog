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

|Data set|Row count|Last updated|
|--------|--------:|------------|
|[Neighborhood Council Expenditures](csv/Neighborhood Council Expenditures.csv)|464|2013-11-11 16:31:18.252780|
|[eCheckbook Data](csv/eCheckbook Data.csv)|111713|2013-11-11 16:31:18.252780|
|[Payroll](csv/Payroll.csv)|150997|2013-11-11 16:31:18.252780|
|[General Fund Revenue](csv/General Fund Revenue.csv)|2791|2013-11-11 16:31:18.252780|
|[General Fund Budget Expenditures](csv/General Fund Budget Expenditures.csv)|1916|2013-11-11 16:31:18.252780|


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