import inspect
from MySQLdb import _mysql

host = 'localhost'
user = 'root'
pwd = '304db'
database = 'tax'

"""
args = inspect.signature(_mysql.connect)
print(str(args))
"""
db=_mysql.connect(host=host,
                  user=user
                  #password=pwd,
                  #database=database
                  )