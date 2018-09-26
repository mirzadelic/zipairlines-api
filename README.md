# ZipAirlines API

## Requirements for project:
 - `python3` and `virtualenv`

 or

 - `docker`


## Run

`python3` and `virtualenv`:
```sh
virtualenv venv
source venv/bin/activate
cd zipairlines-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Or use `docker`:
```sh
cd zipairlines-api
docker build -t zipairlines-api .
docker run -t -i -p 8000:8000 zipairlines-api
```


## API urls
`http://localhost:8000/api/game/game/`


### Tests
```sh
python manage.py test
```

Also, there is integration with CircleCI:
https://circleci.com/gh/mirzadelic/zipairlines-api
