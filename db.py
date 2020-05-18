class Db:
	def __init__(self):
		self.connect()

	def connect(self):
		print('connect這個function被呼叫了!')

	def insert_data(self):
		print('function被呼叫了!')

def asd():
	print('asd被呼叫了!')

x = 5