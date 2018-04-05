-- sqlite3 database.db < lbs-schema.sql sqlite3 database.db < initial-data.sql

drop table if exists meters;
create table meters (
  id integer primary key autoincrement,
  label string
);

drop table if exists meter_data;
create table meter_data (
  id integer primary key autoincrement,
  meter_id integer,
  timestamp datetime default current_timestamp,
  value integer
);
