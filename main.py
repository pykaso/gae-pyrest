import webapp2
from handlers.RestHandler import RestHandler
from models.Sample import Sample, Sample2

RestHandler.register([Sample, Sample2])

_routes = [
	(r'/rest/([^/]+)/?([^/]+)?', RestHandler)
]
app = webapp2.WSGIApplication(_routes)
