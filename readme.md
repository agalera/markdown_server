# Markdown server

## SUMMARY
This is a single server, all you have in the "files" folder serves it via web

## REQUIREMENTS

* python 2.7
* gunicorn
* gevent
* markdown

## RUN
host, port, workers, debug
```sh
python server.py '0.0.0.0' 1111 4 False
```
or
```sh
gunicorn -w 3 -k gevent server:app -b 0.0.0.0:1111
```

## TODO'S
* Config file
* Improve argv
* Use templates to also allow customized css
* build with PyInstaller
