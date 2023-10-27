GO
CREATE OR ALTER PROC CreateSQLServelessView_new_gold @ViewName nvarchar(100)
AS
BEGIN

DECLARE @statement VARCHAR(MAX)

    SET @statement = N'CREATE OR ALTER VIEW ' + @ViewName + ' AS
        SELECT *
        FROM
            OPENROWSET(
            BULK ''https://001azstorageaccount.dfs.core.windows.net/gold-layer/SalesLT/' + @ViewName + '/'',
            FORMAT = ''DELTA''
        ) AS [result]
        '


EXEC (@statement)

END
GO