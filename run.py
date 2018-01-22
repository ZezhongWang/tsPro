from dataAccessor import DataAccessor
from dataProcessor import DataProcessor


import tushare as ts


print ts.__version__


if __name__ == "__main__":
    accessor = DataAccessor(outputA=aNNN)
    accessor.run(size='all')
    processor = DataProcessor(inputA=aNNN)
    processor.run()
    print "tsPro exit"