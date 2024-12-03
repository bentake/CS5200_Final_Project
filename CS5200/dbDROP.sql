-- Drop view
DROP VIEW IF EXISTS spot_information;

-- Drop trigger
DROP TRIGGER IF EXISTS update_spot;

-- Drop stored procedure
DROP PROCEDURE IF EXISTS update_available_spots;

-- Drop tables 
DROP TABLE IF EXISTS Billing_Record;
DROP TABLE IF EXISTS Subscription;
DROP TABLE IF EXISTS Parking_Record;
DROP TABLE IF EXISTS Staff;
DROP TABLE IF EXISTS Parking_Gate;
DROP TABLE IF EXISTS Parking_Zone;
DROP TABLE IF EXISTS Spot;
DROP TABLE IF EXISTS Parking_Lot;
DROP TABLE IF EXISTS Vehicle;
DROP TABLE IF EXISTS Customer;

-- Drop database 
DROP DATABASE IF EXISTS parking_management;
