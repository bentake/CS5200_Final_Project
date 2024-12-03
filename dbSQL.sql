/* Query 1: "What is the total revenue generated from daily parking passes for Parking Lot ID 3?" */
SELECT a.Lot_ID, SUM(a.Amount) AS total_revenue_daily_parking
FROM Billing_Record a 
	 INNER JOIN Parking_Record b on a.Record_ID = b.Record_ID
WHERE b.License_plate NOT IN ( SELECT License_plate
				               FROM Subscription
				               WHERE Lot_ID = 3) AND a.Lot_ID = 3;

/* Query 2: "Show me all vehicles currently parked in Parking Lot ID 1 with a valid subscription." */
WITH parked_vehicle AS (
	SELECT *
	FROM Parking_Record
	WHERE Time_left is null and Lot_ID = 1
),
subscriber AS ( 
	SELECT License_plate, MAX(Time_end) AS Time_end
	FROM Subscription
	GROUP BY License_plate
	HAVING YEAR(Time_end) >= 2024
	ORDER BY License_plate)
SELECT a.License_plate, a.Time_entered, Date(b.Time_end) AS expired_date 
FROM parked_vehicle a
     INNER JOIN subscriber b on a.License_plate = b.License_plate
WHERE a.Time_entered < b.Time_end;

/* Query 3: "What is the parking history for Subscription ID 7?" */
WITH subNO5 AS (
	SELECT * 
	FROM Subscription
	WHERE Subscription_ID = 7)
SELECT *
FROM Parking_Record a 
	 JOIN subNO5 b ON a.License_plate = b.License_plate
WHERE DATE(a.Time_entered) > DATE(b.Time_start) 
      and DATE(a.Time_left) < DATE(b.Time_end);
 

      


/* Query 4:  "Show me all Customers that have subscriptions in the last six months." */
SELECT c.Customer_ID, c.First_name, c.Last_name 
FROM Subscription a
     JOIN Vehicle b on a.License_plate = b.License_plate
     JOIN Customer c on b.Customer_ID = c.Customer_ID
WHERE DATE(Time_end) > DATE_SUB(now(), INTERVAL 6 MONTH);

/* Query 5: "List Customer that have entered the parking lot more than 1 times in the past month." */
WITH vehicle_freq AS (
	SELECT License_plate, COUNT(*) AS parking_freq
	FROM Parking_Record
	WHERE DATE(Time_left) > DATE_SUB(now(), INTERVAL 1 MONTH)
	GROUP BY License_plate 
	HAVING COUNT(*) > 1
	ORDER BY COUNT(*))
SELECT a.Customer_ID, a.First_name, a.Last_name
FROM Customer a
	 JOIN Vehicle b on a.Customer_ID = b.Customer_ID
     JOIN vehicle_freq c on b.License_plate = c.License_plate;

