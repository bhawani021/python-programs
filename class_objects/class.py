# Class and Object
import datetime


class User(object):

	location = 'Bangalore'

	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

	@classmethod
	def get_location(cls):
		return cls.location

	@staticmethod
	def get_current_time():
		return datetime.datetime.now()


# Initialize User class
bhaw = User('Bhawani')
name = bhaw.get_name()
print(name)

# Get location
location = User.get_location()
print(location)

# Get current time
current_time = User.get_current_time()
print(current_time)

