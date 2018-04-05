-- sqlite3 database.db < initial-data.sql
INSERT INTO meters (label) VALUES ('Han Dynasty');
INSERT INTO meters (label) VALUES ('Mala Project');
INSERT INTO meters (label) VALUES ('Kunjip');

INSERT INTO meter_data (meter_id, value) VALUES ('1', 121213400);
INSERT INTO meter_data (meter_id, value) VALUES ('1', 239400);
INSERT INTO meter_data (meter_id, value) VALUES ('1', 7852310);
INSERT INTO meter_data (meter_id, value) VALUES ('1', 9012912000);
INSERT INTO meter_data (meter_id, value) VALUES ('2', 12673);
INSERT INTO meter_data (meter_id, value) VALUES ('2', 1267300);
INSERT INTO meter_data (meter_id, value) VALUES ('3', 9012912000);
INSERT INTO meter_data (meter_id, value) VALUES ('3', 121290000);

-- 
-- INSERT INTO meter_data (meter_id, value, timestamp) VALUES ('1', 898989, "2018-04-04 11:43:54");
-- INSERT INTO meter_data (meter_id, value, timestamp) VALUES ('1', 898989, "2017-04-04 11:43:54");
