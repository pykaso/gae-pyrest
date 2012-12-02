from BaseRestModel import BaseModel, InvalidParamsException

class Sample(BaseModel):

	@staticmethod	
	def isValid(params):
		return ('klic' in params and 'klic2' in params)
		
	@staticmethod
	def get(id):
		
		if(id == 'raise'):
			raise Exception('random error')
		if(id == None):
			id = ''
		return {'action':'get', 'id':id}

	@staticmethod
	def insert(id, params):
		if(not Sample.isValid(params)):
			raise InvalidParamsException(params)
		
		if(params['klic'] == 'raise'):
			raise Exception('random error')
		
		return {'action':'insert', 'params': params}
	
	@staticmethod
	def update(id, params):
		if(not Sample.isValid(params)):
			raise InvalidParamsException(params)
		
		if(params['klic'] == 'raise'):
			raise Exception('random error')
		
		return {'action':'update', 'id':id ,'params': params}
	
	
class Sample2(BaseModel):

	@staticmethod	
	def isValid(params):
		return ('klic' in params and 'klic2' in params)
		
	@staticmethod
	def get(id):
		
		if(id == 'raise'):
			raise Exception('random error')
		if(id == None):
			id = ''
		return {'action':'get', 'id':id}

	@staticmethod
	def insert(id, params):
		if(not Sample.isValid(params)):
			raise InvalidParamsException(params)
		
		if(params['klic'] == 'raise'):
			raise Exception('random error')
		
		return {'action':'insert', 'params': params}
	