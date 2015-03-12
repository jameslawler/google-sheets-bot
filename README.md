# Synonymly Python Project (Google App Engine version)

This is a Google App Engine version of the [Synonymly](http://www.synonymly.com) project.

## Work in Progress

## Installation

* Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
* Git clone this repository
* Make a new environment `mkvirtualenv synonymly`
* `pip install -r requirements.txt`
* `gaenv`


## Temp fix

http://stackoverflow.com/questions/16192916/importerror-no-module-named-ssl-with-dev-appserver-py-from-google-app-engine

Revert to tweepy 2.2 and add the ssl and sockets entries to the sandbox
