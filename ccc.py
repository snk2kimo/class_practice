# 從 db.py(這個module模組)載入 Db這個 calss 
# 從 db.py(這個module模組)載入 asd這個 function
# 從 db.py(這個module模組)載入 x這個變數
from db import Db, asd, x # 或寫 from db import * (調用db模組內的全部程式)

class Tool:
	def __init__(self):
		print('Tool這個class被呼叫了')
		self.db = Db()
		self.db = asd()

t = Tool() # 實體化(執行)Tool這個class

print(x)

# 另一種寫法
import db # 載入db.py這個模組

class Tools:
	def __init__(self):
		print('Tools這個class被呼叫了')
		self.db = db.Db()
		self.db = db.asd()

s = Tools() # 實體化(執行)Tools這個class