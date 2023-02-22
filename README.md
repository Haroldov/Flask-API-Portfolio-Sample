# Peak Power Challenge

![build](https://github.com/haroldov/peak_power/actions/workflows/python-app.yml/badge.svg)

# Folder Structure
```sh
.
├── app.py
├── resources
│   ├── __init__.py
│   ├── text_parser_resource.py
├── routers
│   ├── __init__.py
│   ├── health_check_router.py
│   ├── text_parser_router.py
├── services
│   ├── __init__.py
│   ├── text_service.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── ...
```

# Start Application for Development

You can either use python locally by running:

```sh
python app/app.py
```

Or you can use the docker container by running:

```sh
docker build -t peak_power
docker run -ti peak_power
```

# Start Application for Deployment

You can start the app using the docker compose file by running:

```sh
docker-compose up
```

# Use the app

Simply by executing a curl such as:

```sh
curl -X POST -H "Content-Type: application/json" localhost:5000/text-statistic -d'{"text": "hello world"}'
{
  "aggregation": [
    {
      "count": 1,
      "word": "hello"
    },
    {
      "count": 1,
      "word": "world"
    }
  ],
  "number_of_words": 2,
  "text_length": {
    "with_no_spaces": 10,
    "with_spaces": 11
  }
}
```