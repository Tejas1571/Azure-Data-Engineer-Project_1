SET IDENTITY_INSERT [AdventureWorksLT2017].[SalesLT].[Customer] ON;

DECLARE @UNIQUEX UNIQUEIDENTIFIER
SET @UNIQUEX = NEWID();
DECLARE @UNIQUE UNIQUEIDENTIFIER
SET @UNIQUE = NEWID();

  INSERT INTO [AdventureWorksLT2017].[SalesLT].[Customer]
  ([CustomerID]
      ,[NameStyle]
      ,[Title]
      ,[FirstName]
      ,[MiddleName]
      ,[LastName]
      ,[Suffix]
      ,[CompanyName]
      ,[SalesPerson]
      ,[EmailAddress]
      ,[Phone]
      ,[PasswordHash]
      ,[PasswordSalt]
      ,[rowguid]
      ,[ModifiedDate])
	  VALUES
	  (30119,0,'Mr.', 'Alex','lok', 'biber','Jr.','resale.in','adventure-works\jmt0','Alex12@adventure-works.com','684-555-0134','KJqV15wsX3PG8TS5GSddp6LFFVdd3CoRftZM/tP0+R4=','YTNH5Rw=',@UNIQUEX,'2005-08-01 00:00:00.000'),
	  (32111,0,'Mrs.', 'Tina','wha', 'bibmt','Jr.','resal','adventure-works\jkt0','ATina2@adventure-works.com','684-585-0194','LPqV15wsX3PG8TS5GSddp6LFFVdd3CoRftZM/tP0+R7=','jpHKbqE=',@UNIQUE,'2005-08-01 00:00:00.000')

	  SET IDENTITY_INSERT [AdventureWorksLT2017].[SalesLT].[Customer] OFF;