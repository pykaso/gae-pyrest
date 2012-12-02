import unittest
import webapp2
import main

class RestHandlerTest(unittest.TestCase):
	
	def test_get_root(self):
		print('GET request to "/"')
		request = webapp2.Request.blank('/')
		response = request.get_response(main.app)
		self.assertEqual(response.status, '404 Not Found')
	
	def test_get_without_id(self):
		print('GET request to "/rest/sample/"')
		request = webapp2.Request.blank('/rest/sample/')
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"action":"get","id":""}')

	def test_get_object(self):
		print('GET request to "/rest/sample/999"')
		request = webapp2.Request.blank('/rest/sample/999')
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"action":"get","id":"999"}')
	
	def test_get_unhandled_exception(self):
		print('GET request to "/rest/sample/raise"')
		request = webapp2.Request.blank('/rest/sample/raise')
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"content":"random error","error":"unknown"}')
		
	def test_insert_empty_object(self):
		print('POST empty request to "/rest/sample"')
		request = webapp2.Request.blank('/rest/sample', POST={})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"error":"invalid-params","params":{}}')

	def test_insert_invalid_object(self):
		print('POST request to "/rest/sample"')
		request = webapp2.Request.blank('/rest/sample', POST={'klic':'hodnota'})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"error":"invalid-params","params":{"klic":"hodnota"}}')
		
	def test_insert_valid_object(self):
		print('POST request to "/rest/sample"')
		request = webapp2.Request.blank('/rest/sample', POST={'klic':'hodnota','klic2':5})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"action":"insert","params":{"klic":"hodnota","klic2":"5"}}')

	def test_insert_unhandled_exception(self):
		print('POST request to "/rest/sample"')
		request = webapp2.Request.blank('/rest/sample', POST={'klic':'raise','klic2':5})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"content":"random error","error":"unknown"}')
				
	def test_update_empty_object(self):
		print('PUT empty request to "/rest/sample/999"')
		request = webapp2.Request.blank('/rest/sample/999', method = 'PUT', POST={})
		request.method = 'PUT'
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"error":"invalid-params","params":{}}')

	def test_update_invalid_object(self):
		print('PUT request to "/rest/sample/999"')
		request = webapp2.Request.blank('/rest/sample/999', method = 'PUT', POST={'klic':'hodnota'})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"error":"invalid-params","params":{"klic":"hodnota"}}')
		
	def test_update_valid_object(self):
		print('PUT request to "/rest/sample/999"')
		request = webapp2.Request.blank('/rest/sample/999', method = 'PUT', POST={'klic':'hodnota','klic2':5})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"action":"update","id":"999","params":{"klic":"hodnota","klic2":"5"}}')
		
	def test_update_unhandled_exception(self):
		print('PUT request to "/rest/sample/999"')
		request = webapp2.Request.blank('/rest/sample/999', method = 'PUT', POST={'klic':'raise','klic2':5})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"content":"random error","error":"unknown"}')
		
		
# Sample2 - not allowed to update

	def test_get_root_sample2_(self):
		print('GET request to "/"')
		request = webapp2.Request.blank('/')
		response = request.get_response(main.app)
		self.assertEqual(response.status, '404 Not Found')
	
	def test_get_without_id_sample2_(self):
		print('GET request to "/rest/sample2/"')
		request = webapp2.Request.blank('/rest/sample2/')
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"action":"get","id":""}')

	def test_get_object_sample2_(self):
		print('GET request to "/rest/sample2/999"')
		request = webapp2.Request.blank('/rest/sample2/999')
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"action":"get","id":"999"}')
	
	def test_get_unhandled_exception_sample2_(self):
		print('GET request to "/rest/sample2/raise"')
		request = webapp2.Request.blank('/rest/sample2/raise')
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"content":"random error","error":"unknown"}')
		
	def test_insert_empty_object_sample2_(self):
		print('POST empty request to "/rest/sample2"')
		request = webapp2.Request.blank('/rest/sample2', POST={})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"error":"invalid-params","params":{}}')

	def test_insert_invalid_object_sample2_(self):
 		print('POST request to "/rest/sample2"')
		request = webapp2.Request.blank('/rest/sample2', POST={'klic':'hodnota'})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"error":"invalid-params","params":{"klic":"hodnota"}}')
		
	def test_insert_valid_object_sample2_(self):
		print('POST request to "/rest/sample2"')
		request = webapp2.Request.blank('/rest/sample2', POST={'klic':'hodnota','klic2':5})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"action":"insert","params":{"klic":"hodnota","klic2":"5"}}')

	def test_insert_unhandled_exception_sample2_(self):
		print('POST request to "/rest/sample2"')
		request = webapp2.Request.blank('/rest/sample2', POST={'klic':'raise','klic2':5})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"content":"random error","error":"unknown"}')
				
	def test_update_empty_object_sample2_(self):
		print('PUT empty request to "/rest/sample2/999"')
		request = webapp2.Request.blank('/rest/sample2/999', method = 'PUT', POST={})
		request.method = 'PUT'
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"error":"invalid-action","name":"sample2"}')

	def test_update_invalid_object_sample2_(self):
		print('PUT request to "/rest/sample2/999"')
		request = webapp2.Request.blank('/rest/sample2/999', method = 'PUT', POST={'klic':'hodnota'})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"error":"invalid-action","name":"sample2"}')
		
	def test_update_valid_object_sample2_(self):
		print('PUT request to "/rest/sample2/999"')
		request = webapp2.Request.blank('/rest/sample2/999', method = 'PUT', POST={'klic':'hodnota','klic2':5})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"error":"invalid-action","name":"sample2"}')
		
	def test_update_unhandled_exception_sample2_(self):
		print('PUT request to "/rest/sample2/999"')
		request = webapp2.Request.blank('/rest/sample2/999', method = 'PUT', POST={'klic':'raise','klic2':5})
		response = request.get_response(main.app)
		self.assertEqual(response.status, '200 OK')
		self.assertEqual(response.body, '{"error":"invalid-action","name":"sample2"}')