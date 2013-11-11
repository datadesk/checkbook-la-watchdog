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

* eCheckbook data
* General Fund Budget Expenditures
* General Fund Revenue
* Neighborhood Council Expenditures
* Payroll

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
