CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id varchar(255) not null,
    latitude decimal(11,8) not null,
    longitude decimal(11,8) not null,
    direction_id INT,
    current_stop_sequence INT,
    label INT,
    speed decimal(5,2),
    trip_id INT,
    stop_id INT,
    bus_bearing INT,
    occupancy_status varchar(255),
    current_status varchar(255),
    updated_at varchar(255) not null
);
