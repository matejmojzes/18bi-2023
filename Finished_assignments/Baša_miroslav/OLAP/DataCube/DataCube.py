

from olapy.core.mdx.executor import MdxEngine


executor = MdxEngine() # instantiate the MdxEngine

executor.load_cube('CAvideos')

print(executor.get_all_tables_names())
#print(executor.tables_loaded)
print(executor)

#query = """SELECT
#Hierarchize({[Measures].[video_id]}) ON COLUMNS
#FROM [CAvideos]
#"""

#df = executor.execute_mdx(query)['result']

#print(df)


