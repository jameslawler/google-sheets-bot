# Synonymly Python Project (Google App Engine version)

This python application is a Google Sheets driven Twitter bot that
posts regular messages by combining various pieces of data from a
set of Google Sheets.

The python application reads data from Google Sheets, posts a message
to Twitter, and then writes an audit entry back into the Google Sheet file.

## Requirements

* Google App Engine application
* [Python 2.7](https://www.python.org/)
* [Google App Engine SDK Python](https://cloud.google.com/appengine/downloads)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
* [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html)

## Installation

* `git clone https://github.com/jameslawler/synonymly-gae.git`
* `mkvirtualenv synonymly` - to create a new python environment
* `pip install -r requirements.txt`
* `gaenv` - to install locally all the python libraries

## Google App Engine

This program requires a free Google App Engine account.

1. Go to [Google App Engine](https://appengine.google.com/)
2. Create a new application
3. Update the app.yaml with your Application Id

## Configuration

This application requires Google and Twitter OAuth credentials. Rename the `config.ini.sample`
to `config.ini`. Enter your credentials into the `config.ini` file. The timezone is used to
set the auditing date information. A list of available timezones is provided on the 
[Timezones Wikipedia page](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones) 

```ini
[Synonymly]
Timezone: Europe/Amsterdam

[Google]
Username: myusername@gmail.com
Password: mypassword

[Twitter]
ConsumerKey: 
ConsumerSecret: 
AccessToken: 
AccessTokenSecret: 
```

## Scheduled tasks

Configure your scheduled tasks by updating `cron.yaml` by following the
information provided by [Google](https://cloud.google.com/appengine/docs/python/config/cron#Python_app_yaml_The_schedule_format)

## Usage

To locally debug with the Google App Engine SDK run the following command

`python ~/<Google-App-Engine-SDK>/dev_appserver.py synonymly-gae/`

Then open a Browser and browse to [http://localhost:8080/tweet/english/beginner/](http://localhost:8080/tweet/english/beginner/)

## Endpoints

This project has the following endpoints available

* /tweet/english/beginner/ - Tweet English at a Beginner level
* /tweet/english/intermediate/ - Tweet English at a Intermediate level
* /tweet/english/advanced/ - Tweet English at a Advanced level

## Deploying to Google App Engine

To deploy the project to your Google App Engine account run the following command

`python ~/<Google-App-Engine-SDK>/appcfg.py update synonymly-gae/`

Enter your Google username and password credentials.

Note: If you are unable to authenticate it may be because Google has blocked your
attempt to login. You can get past this block by enabling less secure applications
by browsing to [Less Secure Apps setting](https://www.google.com/settings/security/lesssecureapps)

## Known Issues

This project uses Tweepy 2.1. This is the last version of Tweepy that I have
been able to make work with Google App Engine. The newer versions have a lot
more dependencies that are incompatible with Google App Engine.
