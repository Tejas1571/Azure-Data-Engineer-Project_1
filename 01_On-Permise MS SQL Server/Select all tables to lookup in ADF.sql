--all database tables with schema = SalesLT
select t.name as TableName, 
s.name as SchemaName 
from sys.tables as t inner join sys.schemas as s on t.schema_id = s.schema_id
where s.name = 'SalesLT';