#!/usr/bin/env bash

mkdir -p dags logs plugins
chmod a+w ./dags ./logs ./plugins
docker compose up airflow-init
cp airnow-dags/*.py ./dags