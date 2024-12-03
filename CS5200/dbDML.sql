-- Customer table
INSERT INTO Customer (Customer_ID, First_name, Last_name, Street, City, State, Zip)
VALUES 
(1, 'Ben', 'Ko', '123 ABC Street', 'San Jose', 'CA', '95131'),
(2, 'Lillian', 'Le', '234 CDF Street', 'Los Angeles', 'CA', '95126'),
(3, 'Dwayne', 'Johnson', '358 EFG Street', 'New York', 'NY', '11111'),
(4, 'Muhammad', 'Ali', '494 ZYX Street', 'San Francisco', 'CA', '93123'),
(5, 'Jake', 'Paul', '231 ZND Street', 'Chicago', 'IL', '46656'),
(6, 'Kuma', 'Oshi', '1243 ZKJN Street', 'Notre Dame', 'IN', '46617'),
(7, 'Peanut', 'Acai', '343 VKO Street', 'Fairfax', 'VA', '22033');

-- Vehicle table
INSERT INTO Vehicle (License_plate, Make, Model, Year, Customer_ID, Type, Number_of_doors, Fuel_type, Cargo_capacity)
VALUES 
('ABC123', 'Hyundai', 'Elantra', 2020, 1, 'Car', 4, 'Gasoline', NULL),
('DEF456', 'Honda', 'Civic', 2019, 2, 'Car', 4, 'Gasoline', NULL),
('GHI789', 'Ford', 'F-150', 2023, 3, 'Truck', NULL, 'Diesel', 3000),
('JKL012', 'Tesla', 'Model 3', 2022, 4, 'Car', 4, 'Electric', NULL),
('MNO345', 'Chevrolet', 'Silverado', 2018, 5, 'Truck', NULL, 'Gasoline', 2500),
('PQR678', 'Mercedes', 'E350', 2021, 6, 'Car', 4, 'Gasoline', NULL),
('STU901', 'Audi', 'A4', 2024, 7, 'Car', 4, 'Gasoline', NULL);

--  Parking_Lot table
INSERT INTO Parking_Lot (Lot_ID, Number_of_spots, Street, City, State, Zip, Available_spots)
VALUES 
(1, 100, '100 Parking St', 'San Jose', 'CA', '90001', 80),
(2, 150, '200 Parking St', 'San Francisco', 'CA', '94102', 120),
(3, 200, '300 Parking St', 'New York', 'NY', '11011', 150),
(4, 250, '400 Parking St', 'Fairfax', 'VA', '22033', 100),
(5, 300, '100 Garage St', 'Notre Dame', 'IN', '46617', 101),
(6, 100, '200 Garage St', 'San Jose', 'CA', '95131', 84),
(7, 150, '300 Garage St', 'Los Angeles', 'CA', '93143', 39);

-- Spot table
INSERT INTO Spot (Spot_ID, Lot_ID, Spot_status)
VALUES 
(1, 1, 'Available'),
(2, 1, 'Taken'),
(3, 2, 'Available'),
(4, 2, 'Taken'),
(9, 2, 'Available'),
(5, 3, 'Available'),
(6, 3, 'Available'),
(7, 4, 'Available'),
(8, 5, 'Taken');

-- Parking_Zone table
INSERT INTO Parking_Zone (Zone_ID, Zone_name, Zone_type, Zone_capacity, Lot_ID)
VALUES 
(1, 'Zone A', 'General', 50, 1),
(2, 'Zone B', 'Reserved', 30, 1),
(3, 'Zone C', 'General', 100, 2),
(4, 'Zone D', 'Electric', 20, 3),
(5, 'Zone A', 'General', 30, 2),
(6, 'Zone C', 'General', 40, 2);

-- Parking_Gate table
INSERT INTO Parking_Gate (Gate_ID, Is_operational, Installed_in)
VALUES 
(1, TRUE, 1),
(2, FALSE, 2),
(3, TRUE, 3),
(4, FALSE, 4),
(5, TRUE, 5),
(6, FALSE, 6),
(7, TRUE, 7);

-- Staff table
INSERT INTO Staff (Staff_ID, Name, Shift_start, Shift_end, Lot_ID)
VALUES 
(1, 'Yongzheng', '08:00:00', '16:00:00', 1),
(2, 'Yifan', '09:00:00', '17:00:00', 2),
(3, 'Xueming', '10:00:00', '18:00:00', 3),
(4, 'Ben', '19:00:00', '22:59:00', 3),
(5, 'Byunghyun', '10:00:00', '18:00:00', 4),
(6, 'Kevin', '19:00:00', '22:59:00', 4),
(7, 'Simon', '10:00:00', '18:00:00', 5);

-- Parking_Record table
INSERT INTO Parking_Record (Record_ID, License_plate, Spot_ID, Time_entered, Time_left, Lot_ID)
VALUES 
(1, 'ABC123', 2, '2024-11-17 08:30:00', NULL, 1),
(2, 'DEF456', 9, '2024-10-22 09:00:00', '2024-10-22 17:00:00', 2),
(3, 'DEF456', 9, '2024-10-27 09:00:00', '2024-10-27 17:00:00', 2),
(4, 'DEF456', 4, '2024-11-17 09:00:00', '2024-11-17 13:00:00', 2),
(5, 'GHI789', 5, '2024-09-02 08:00:00', '2024-09-02 16:30:00', 3),
(6, 'GHI789', 6, '2024-09-09 08:00:00', '2024-09-09 18:00:00', 3),
(7, 'PQR678', 1, '2024-11-19 21:00:00', NULL, 1),
(8, 'MNO345', 6, '2023-02-09 08:00:00', '2023-02-09 18:00:00', 3),
(9, 'STU901', 5, '2023-07-10 08:00:00', '2023-07-10 18:00:00', 3);

-- Billing_Record table
INSERT INTO Billing_Record (Billing_ID, Customer_ID, Amount, Billing_date, Payment_status, Lot_ID, Record_ID)
VALUES 
(1, 1, 50, '2024-11-17', 'Unpaid', 1, 1),
(2, 2, 5.00, '2024-10-22', 'paid', 2, 2),
(3, 2, 5.00, '2024-10-27', 'paid', 2, 3),
(4, 2, 5.00, '2024-11-17', 'paid', 2, 4),
(5, 3, 17.50, '2024-09-02', 'paid', 3, 5),
(6, 3, 20.00, '2024-09-09', 'paid', 3, 6),
(7, 6, 30, '2024-11-19', 'Unpaid', 1, 7),
(8, 5, 20.00, '2023-02-09', 'paid', 3, 8),
(9, 7, 5.00, '2024-07-10', 'paid', 3, 9);

-- Subscription table
INSERT INTO Subscription (Subscription_ID, Lot_ID, License_plate, Price, Time_start, Time_end)
VALUES 
(1, 1, 'JKL012', 50.00, '2021-02-01 00:00:00', '2021-07-31 23:59:59'),
(2, 1, 'JKL012', 120.00, '2022-01-01 00:00:00', '2022-12-31 23:59:59'),
(3, 1, 'JKL012', 120.00, '2024-01-01 00:00:00', '2024-12-31 23:59:59'),
(4, 3, 'STU901', 30, '2023-05-01 00:00:00', '2023-08-31 23:59:59'),
(5, 3, 'STU901', 30, '2023-09-01 00:00:00', '2023-12-31 23:59:59'),
(6, 3, 'STU901', 20, '2024-10-01 00:00:00', '2024-11-30 23:59:59'),
(7, 2, 'DEF456', 60, '2024-07-01 00:00:00', '2024-12-31 23:59:59'),
(8, 1, 'PQR678', 50, '2024-08-01 00:00:00', '2024-12-31 23:59:59');

-- Example UPDATE operation
UPDATE Spot SET Spot_status = 'Available' WHERE Spot_ID = 2;

-- Delete related records from the child table (Billing_Record)
DELETE FROM Billing_Record WHERE Record_ID = 2;

-- Delete the record from the parent table (Parking_Record)
DELETE FROM Parking_Record WHERE Record_ID = 2;

