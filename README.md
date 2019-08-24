# sh-db
shelf/shit db - keeping track of your shit

```
$ sudo apt-get install python3-venv
$ cd sh-db
$ python3 -m venv venv
$ . venv/bin/activate
(venv)$ pip3 install Flask flask_wtf flask-sqlalchemy flask-migrate --no-cache-dir
(venv)$ export FLASK_APP=sh-db.py
(venv)$ flask db init
(venv)$ flask db migrate
(venv)$ flask db upgrade
(venv)$ flask run
(venv)$ deactivate
$
```

Learning by doing, courtesy from [here](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), results [here](https://github.com/u1313/sh-db).
