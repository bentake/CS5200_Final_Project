CREATE DATABASE parking_management;
USE parking_management;

CREATE TABLE Customer (
    Customer_ID INT PRIMARY KEY,
    First_name VARCHAR(10),
    Last_name VARCHAR(10),
    Street VARCHAR(30),
    City VARCHAR(20),
    State VARCHAR(20),
    Zip VARCHAR(6)
);

CREATE TABLE Vehicle (
    License_plate VARCHAR(10) PRIMARY KEY,
    Make VARCHAR(15),
    Model VARCHAR(15),
    Year INT,
    Customer_ID INT,
    Type ENUM('Car', 'Truck'),
    Number_of_doors INT,         
    Fuel_type VARCHAR(10),      
    Cargo_capacity INT,         
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID) ON DELETE CASCADE
);

CREATE TABLE Parking_Lot (
    Lot_ID INT PRIMARY KEY,
    Number_of_spots INT,
    Street VARCHAR(30),
    City VARCHAR(20),
    State VARCHAR(20),
    Zip VARCHAR(6),
    Available_spots INT
);

CREATE TABLE Spot (
    Spot_ID INT PRIMARY KEY,
    Lot_ID INT,
    Spot_status VARCHAR(10),
    FOREIGN KEY (Lot_ID) REFERENCES Parking_Lot(Lot_ID) ON DELETE CASCADE
);

CREATE TABLE Parking_Zone (
    Zone_ID INT PRIMARY KEY,
    Zone_name VARCHAR(20),
    Zone_type VARCHAR(15),
    Zone_capacity INT,
    Lot_ID INT,
    FOREIGN KEY (Lot_ID) REFERENCES Parking_Lot(Lot_ID) ON DELETE CASCADE
);

CREATE TABLE Parking_Gate (
    Gate_ID INT PRIMARY KEY,
    Is_operational BOOLEAN,
    Installed_in INT,
    FOREIGN KEY (Installed_in) REFERENCES Parking_Lot(Lot_ID) ON DELETE CASCADE
);

CREATE TABLE Staff (
    Staff_ID INT PRIMARY KEY,
    Name VARCHAR(20),
    Shift_start TIME,
    Shift_end TIME,
    Lot_ID INT,
    FOREIGN KEY (Lot_ID) REFERENCES Parking_Lot(Lot_ID) ON DELETE CASCADE
);

CREATE TABLE Parking_Record (
    Record_ID INT PRIMARY KEY,
    License_plate VARCHAR(10),
    Spot_ID INT,
    Time_entered DATETIME,
    Time_left DATETIME,
    Lot_ID INT,
    FOREIGN KEY (License_plate) REFERENCES Vehicle(License_plate) ON DELETE CASCADE,
    FOREIGN KEY (Spot_ID) REFERENCES Spot(Spot_ID) ON DELETE SET NULL,
    FOREIGN KEY (Lot_ID) REFERENCES Parking_Lot(Lot_ID) ON DELETE CASCADE
);

CREATE TABLE Billing_Record (
    Billing_ID INT PRIMARY KEY,
    Customer_ID INT,
    Amount DECIMAL(10, 2),
    Billing_date DATE,
    Payment_status VARCHAR(10),
    Lot_ID INT,
    Record_ID INT,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID) ON DELETE CASCADE,
    FOREIGN KEY (Lot_ID) REFERENCES Parking_Lot(Lot_ID) ON DELETE CASCADE,
    FOREIGN KEY (Record_ID) REFERENCES Parking_Record(Record_ID) ON DELETE CASCADE
);

CREATE TABLE Subscription (
    Subscription_ID INT PRIMARY KEY,
    Lot_ID INT,
    License_plate VARCHAR(10),
    Price DECIMAL(10, 2),
    Time_start DATETIME,
    Time_end DATETIME,
    FOREIGN KEY (Lot_ID) REFERENCES Parking_Lot(Lot_ID) ON DELETE CASCADE,
    FOREIGN KEY (License_plate) REFERENCES Vehicle(License_plate) ON DELETE CASCADE
);

-- Trigger 
DELIMITER $$ 
DROP TRIGGER IF EXISTS update_spot $$ 
CREATE TRIGGER update_spot
AFTER INSERT ON Parking_Record
FOR EACH ROW
BEGIN
    UPDATE Spot
    SET Spot_status = 'Taken'
    WHERE Spot_ID = NEW.Spot_ID;
END $$ 
DELIMITER ; 

-- Procedure 
DELIMITER $$ 
DROP PROCEDURE IF EXISTS update_available_spots $$ 
CREATE PROCEDURE update_available_spots (IN param1 INT)
BEGIN
    UPDATE Parking_Lot
    SET Available_spots = (
        SELECT COUNT(*) 
        FROM Spot
        WHERE Lot_ID = param1 AND Spot_status = 'Available'
    )
    WHERE Lot_ID = param1;
END $$ 
DELIMITER ;

-- View
CREATE VIEW spot_information 
AS SELECT Spot.Spot_ID, Spot.Spot_Status, Spot.Lot_ID, Parking_Lot.Street, Parking_Lot.City, Parking_Lot.State
FROM Spot
JOIN Parking_Lot ON Spot.Lot_ID = Parking_Lot.Lot_ID;
