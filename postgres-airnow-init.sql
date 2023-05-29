-- CREATE USER airnow_admin WITH PASSWORD 'jw8s0F4';

-- CREATE USER airnow_admin WITH PASSWORD 'ClwroyfOolkmotaAUJsv0nd0r5elWfHtRof7C3lYdzwr1FjmxzsrBGyASQvzXa0FFwqVQsvr35aDTou7XXxYpyzvibWBkLrpeiIC';
-- CREATE DATABASE airnow;
CREATE TABLE IF NOT EXISTS pm25_measurements (
    datetime timestamp not null,
    location varchar(100) not null,
    aqi numeric null,
    aqi_cat varchar(30) null,
    conc numeric null,
    PRIMARY KEY(datetime, location)
);

CREATE TABLE IF NOT EXISTS cities (
    location varchar(100) not null,
    latitude numeric null,
    longitude numeric null,
    latlon varchar(50) null,
    PRIMARY KEY(location)
);
