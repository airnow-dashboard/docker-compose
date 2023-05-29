#!/usr/bin/env bash

chmod a+w ./dags ./logs ./plugins
docker compose up airflow-init