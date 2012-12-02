import webapp2
import logging
from lib import demjson
from models.BaseRestModel import InvalidParamsException

def jsonOutput(handler):
	def wrapper(self, *args, **kwargs):
		result = handler(self, *args, **kwargs)
		self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
		self.response.write(demjson.encode(result, encoding='utf-8')) 
	return wrapper


class InvalidActionException(Exception):
	pass

class RestHandler(webapp2.RequestHandler):
	ALLOWED_GET = []
	ALLOWED_POST = []
	ALLOWED_PUT = []
	MAP = {}
	
	@staticmethod
	def register(classname):
		if isinstance(classname, list):
			for cls in classname:
				RestHandler.register(cls)
			return 

		action = str(classname.__name__).lower()
		RestHandler.MAP[action] = classname
		
		if ('get' in classname.__dict__):
			RestHandler.ALLOWED_GET.append(action)
		if ('insert' in classname.__dict__ ):
			RestHandler.ALLOWED_POST.append(action)
		if ('update' in classname.__dict__):
			RestHandler.ALLOWED_PUT.append(action)

		logging.info('register: ' + str(classname.__name__))
	
	@jsonOutput
	def get(self, action=None, id=None):
		try:
			if(action not in RestHandler.ALLOWED_GET):
				raise InvalidActionException()
			return RestHandler.MAP[action.lower()].get(id)
		
		except InvalidActionException, e:
			return {'error': 'invalid-action', 'name':action}	
		except Exception, e:
			return {'error': 'unknown', 'content': unicode(e)}
	
	@jsonOutput
	def post(self, action=None, id=None):
		try:
			if(action not in RestHandler.ALLOWED_POST):
				raise InvalidActionException()
			params = dict(self.request.params)
			return RestHandler.MAP[action.lower()].insert(id, params)

		except InvalidActionException, e:
			return {'error': 'invalid-action', 'name':action}
		except InvalidParamsException, e:
			return {'error': 'invalid-params', 'params':params}	
		except Exception, e:
			return {'error': 'unknown', 'content': unicode(e)}

	@jsonOutput
	def put(self, action=None, id=None):
		try:
			if(action not in RestHandler.ALLOWED_PUT  or id is None):
				raise InvalidActionException()
			params = dict(self.request.params)
			return RestHandler.MAP[action.lower()].update(id, params)

		except InvalidActionException, e:
			return {'error': 'invalid-action', 'name':action}
		except InvalidParamsException, e:
			return {'error': 'invalid-params', 'params':params}	
		except Exception, e:
			return {'error': 'unknown', 'content': unicode(e)}		
