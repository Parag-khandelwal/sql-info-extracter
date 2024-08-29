-- Sample Stored Procedure for Testing
CREATE PROCEDURE GetEmployeeData
AS
BEGIN
    -- Fetch employee details
    SELECT e.EmployeeID, e.FirstName, e.LastName, d.DepartmentName
    FROM Employees e
    INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID
    WHERE e.Status = 'Active';

    -- Fetch employee salary information
    SELECT es.EmployeeID, es.Salary, es.Bonus
    FROM EmployeeSalaries es
    WHERE es.Salary > 50000;
END;
GO

-- View definition
CREATE VIEW ActiveEmployees AS
SELECT e.EmployeeID, e.FirstName, e.LastName
FROM Employees e
WHERE e.Status = 'Active';

-- Another stored procedure
CREATE PROCEDURE UpdateEmployeeStatus
    @EmployeeID INT,
    @NewStatus VARCHAR(50)
AS
BEGIN
    UPDATE Employees
    SET Status = @NewStatus
    WHERE EmployeeID = @EmployeeID;

    -- Log the status change
    INSERT INTO EmployeeStatusLogs (EmployeeID, StatusChangeDate, NewStatus)
    VALUES (@EmployeeID, GETDATE(), @NewStatus);
END;
GO

-- Function definition
CREATE FUNCTION GetEmployeeCount (@DepartmentID INT)
RETURNS INT
AS
BEGIN
    DECLARE @EmployeeCount INT;

    SELECT @EmployeeCount = COUNT(*)
    FROM Employees
    WHERE DepartmentID = @DepartmentID;

    RETURN @EmployeeCount;
END;
GO
