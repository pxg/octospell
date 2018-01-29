## Installing
```
mkvirtualenv --python=/usr/local/bin/python3 octospell
pip install requirements.txt
```

Run the app:
```
export FLASK_DEBUG=1
export FLASK_APP=app.py
flask run
```

Run ngrok:
```
ngrok http 5000
```
