# airnow-dashboard
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/airnow-dashboard/docker-compose.svg)](https://github.com/airnow-dashboard/docker-compose/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/airnow-dashboard/docker-compose.svg)](https://github.com/airnow-dashboard/docker-compose/issues)
[![Contributions welcome](https://img.shields.io/badge/Contributions-welcome-orange.svg)](https://github.com/airnow-dashboard/docker-compose/blob/master/CONTRIBUTING.md)


Welcome to the airnow-dashboard repository! This repository hosts Docker Compose files for setting up and running the AirNow Dashboard system. The AirNow Dashboard provides visualizations and analytics for air quality data collected from various sources.

## Features
Visualization of air quality data
Historical data analysis
Customizable dashboards
Integration with external APIs

## Prerequisites
Before using the AirNow Dashboard system, make sure you have the following prerequisites installed on your system:

Docker Engine/Desktop: [Installation Guide](https://docs.docker.com/get-docker/)

*Note: Docker Compose is included in the latest version of Docker Engine/Desktop, so no additional installation is needed!*

## Getting Started

To get started with the AirNow Dashboard, follow these steps:

1. Clone this repository:

```bash
git clone https://github.com/airnow-dashboard/docker-compose.git
```

2. Change to the cloned directory:
```bash
cd docker-compose
```

3. Customize the configuration:
Modify the `docker-compose.yml` file if needed.


4. Initialize the AirNow Dashboard system:

```bash
. deploy.sh
```

5. Start the AirNow Dashboard system:
```bash
docker-compose up
```
Or, if you want it to start detached (i.e. running in the background):
```bash
docker-compose up -d
```
This command will download the necessary Docker images and start the containers.

6. Access the system components via:

- Airflow Webserver: Port 8080 
- Postgres: Port 5432

## Contributing
Contributions to the AirNow Dashboard project are welcome! If you would like to contribute, please follow the guidelines provided in the CONTRIBUTING.md file.

## License
The AirNow Dashboard is open source and available under the MIT License.

## Acknowledgements
We would like to thank the following libraries, frameworks, and APIs that are used in this project:

- [Docker](https://www.docker.com)
- [Apache Airflow](https://airflow.apache.org/)
- [PostgreSQL](https://www.postgresql.org/)

## Support
If you have any questions or encounter any issues, please open an issue on GitHub.

Enjoy using the AirNow Dashboard!