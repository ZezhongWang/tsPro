from dataAccessor import DataAccessor
from dataProcessor import DataProcessor


import tushare as ts


print ts.__version__

accessor = DataAccessor()
accessor.run(size='all')
processor = DataProcessor()
processor.run()
print "tsPro exit"