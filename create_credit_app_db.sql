
-- Create table
CREATE TABLE IF NOT EXISTS credit_applications (
    id INT PRIMARY KEY,
    applicant_name VARCHAR(100),
    age INT,
    income DECIMAL(10,2),
    loan_amount DECIMAL(10,2),
    approved BOOLEAN
);

-- Insert data
INSERT INTO credit_applications (id, applicant_name, age, income, loan_amount, approved)
VALUES 
(1, 'Ali Rezaei', 29, 55000, 12000, 1),
(2, 'Sara Ahmadi', 35, 72000, 15000, 1),
(3, 'Mehdi Nazari', 42, 43000, 8000, 0),
(4, 'Mina Kamali', 31, 60000, 11000, 1),
(5, 'Omid Karimi', 26, 39000, 5000, 0);