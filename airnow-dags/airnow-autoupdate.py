from os import environ
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.providers.docker.operators.docker import DockerOperator

from docker.types import Mount

output_target = "/app/output"

piper_env_vars = {
    "AIRNOW_DB_HOST": "localhost",
    "AIRNOW_DB_NAME": "airnow",
    "AIRNOW_DB_USER": "airnow_admin",
    "AIRNOW_DB_PASSWORD": "ClwroyfOolkmotaAUJsv0nd0r5elWfHtRof7C3lYdzwr1FjmxzsrBGy",
}

shared_volume = Mount(
    target=output_target,
    source="airnow-data-volume",
    type="volume",
    read_only=False
)

with DAG(
    "airnow-autoupdate",
    is_paused_upon_creation=False,  # enable upon DAG creation
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["admin@solsyn.dev"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="Autoupdate pipeline for airnow",
    schedule_interval=timedelta(hours=4),
    start_date=datetime(2022, 12, 1),
    catchup=False,
    tags=["recurrent"],
) as dag:

    scraper = DockerOperator(
        api_version='1.30',
        docker_url='tcp://docker-socket-proxy:2375',
        task_id="scrape_data",
        image="ghcr.io/airnow-dashboard/airnow-scraper:latest",
        auto_remove="force",
        mounts=[shared_volume],
        command="current"
    )

    scraper.doc_md = dedent(
        """\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.
    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
    **Image Credit:** Randall Munroe, [XKCD](https://xkcd.com/license.html)
    """
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG; OR
    dag.doc_md = """
    This is a documentation placed anywhere
    """  # otherwise, type it like this

    piper = DockerOperator(
        api_version='1.30',
        docker_url='tcp://docker-socket-proxy:2375',
        task_id="piper",
        image="ghcr.io/airnow-dashboard/piper:latest",
        auto_remove="force",
        mounts=[shared_volume],
        command=[output_target, "current"],
        network_mode="host",
        environment=piper_env_vars
    )

    scraper >> piper