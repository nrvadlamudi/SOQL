SELECT * FROM Production.Product;
SELECT Name, ListPrice FROM Production.Product;
SELECT DISTINCT Name FROM Production.ProductCategory;
SELECT * FROM Sales.SalesOrderHeader;
SELECT SalesOrderNumber, OrderDate, TotalDue FROM Sales.SalesOrderHeader;
SELECT DISTINCT CustomerID FROM Sales.SalesOrderHeader;
SELECT COUNT(*) FROM Production.Product;
SELECT AVG(ListPrice) FROM Production.Product;
SELECT * FROM Production.Product WHERE ListPrice > 500.0;
SELECT * FROM Sales.SalesOrderHeader WHERE YEAR(OrderDate) = 2022;
SELECT * FROM HumanResources.Employee WHERE JobTitle = 'Sales Representative';
SELECT TOP 10 CustomerID, SUM(TotalDue) AS TotalPurchases FROM Sales.SalesOrderHeader GROUP BY CustomerID ORDER BY TotalPurchases DESC;
SELECT ProductID, SUM(OrderQty) AS TotalQuantitySold FROM Sales.SalesOrderDetail GROUP BY ProductID ORDER BY TotalQuantitySold DESC;
SELECT CustomerID, COUNT(*) AS OrderCount FROM Sales.SalesOrderHeader GROUP BY CustomerID ORDER BY OrderCount DESC;
SELECT ProductID, AVG(OrderQty) AS AvgOrderQuantity FROM Sales.SalesOrderDetail GROUP BY ProductID ORDER BY AvgOrderQuantity DESC;
SELECT pc.Name AS CategoryName, SUM(soh.TotalDue) AS TotalSales FROM Sales.SalesOrderHeader soh JOIN Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID JOIN Production.Product p ON sod.ProductID = p.ProductID JOIN Production.ProductSubcategory ps ON p.ProductSubcategoryID = ps.ProductSubcategoryID JOIN Production.ProductCategory pc ON ps.ProductCategoryID = pc.ProductCategoryID WHERE YEAR(soh.OrderDate) = 2022 GROUP BY pc.Name ORDER BY TotalSales DESC;

