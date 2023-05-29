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
