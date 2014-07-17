dailyactivity
=============

Scraper and parser for 2012 Sacramento PD [daily activity logs](http://www.sacpd.org/dailyactivity/)

First downloads HTML pages to pages directory, then scrapes incident names and dates into new file crimes.csv.

Usage
=====
Scraping:

    pip install -r requirements.txt
    python sacpd-scraper.py
    python scrape-pages.py

Analysis ([nbviewer](http://nbviewer.ipython.org/github/danhillreports/dailyactivity/blob/master/analysis.ipynb)):

    ipython notebook --pylab inline
