#!/usr/bin/env bash

mkdir -p dags logs plugins airnow-data
chmod a+w ./dags ./logs ./plugins ./airnow-data
docker compose up airflow-init
cp airnow-dags/*.py ./dags