# ZipAirlines API

### Aircraft passenger capacity issue

We are creating a new software for a airline company called `ZipAirlines`.
 The company is assessing 10 different airplanes.

 - Each airplane has a fuel tank of (`200 liters * id` of the airplane) capacity.  For example, if the airplane `id = 2`, the fuel tank capacity is `2*200 = 400 liters`.
 - The airplane fuel consumption per minute is the logarithm of the airplane `id multiplied by 0.80 liters`.
 - `Each passenger` will increase fuel consumption for additional `0.002 liters per minute`.

 Write a RESTful API using Django Rest Framework to:

 - Allow for input of 10 airplanes with user defined id and passenger assumptions
 - Print `total airplane fuel consumption per minute` and `maximum minutes able to fly`

## Requirements for project:
 - `python3` and `virtualenv`

 or

 - `docker`


## Run

`python3` and `virtualenv`:
```sh
 # you are at root dir of project
virtualenv venv
source venv/bin/activate
cd zipairlines-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Or use `docker`:
```sh
cd zipairlines-api # this is root dir of project
docker build -t zipairlines-api .
docker run -t -i -p 8000:8000 zipairlines-api
```


## API urls
`http://localhost:8000/api/v1/airlines/airplanes/`

>POST - calculate airplanes from sent data

POST data:
```json
{
  "airplanes": [
  	{
      "id": 1,
      "passengers": 100
    },
    {
      "id": 2,
      "passengers": 200
    },
    {
      "id": 3,
      "passengers": 300
    },
    {
      "id": 4,
      "passengers": 300
    }
  ]
}
```

Response data:
```json
{
  "airplanes": [
    {
      "id": 1,
      "passengers": 100,
      "tank_capacity": 200.0,
      "per_passenger_consumption": 0.2,
      "per_minute_fuel_consumption": 1.0,
      "max_fly_minutes": 200.0,
      "fuel_required": 20.8
    },
    {
      "id": 2,
      "passengers": 200,
      "tank_capacity": 400.0,
      "per_passenger_consumption": 0.4,
      "per_minute_fuel_consumption": 2.0,
      "max_fly_minutes": 200.0,
      "fuel_required": 81.6
    },
    {
      "id": 3,
      "passengers": 300,
      "tank_capacity": 600.0,
      "per_passenger_consumption": 0.6,
      "per_minute_fuel_consumption": 3.0,
      "max_fly_minutes": 200.0,
      "fuel_required": 182.4
    },
    {
      "id": 4,
      "passengers": 300,
      "tank_capacity": 800.0,
      "per_passenger_consumption": 0.6,
      "per_minute_fuel_consumption": 3.8,
      "max_fly_minutes": 210.526,
      "fuel_required": 183.2
    }
  ]
}
```


### Tests
```sh
python manage.py test
```

Also, there is integration with CircleCI:
https://circleci.com/gh/mirzadelic/zipairlines-api
