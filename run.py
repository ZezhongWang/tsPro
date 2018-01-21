from dataAccessor import DataAccessor
from dataProcessor import DataProcessor


import tushare as ts


print ts.__version__

accessor = DataAccessor()
accessor.run()
processor = DataProcessor(data)
processor.run()


print "ts Pro run!"