import simplejson as json
from django.http import HttpResponse

from constant.ret_codes import Resp
from lib.exception import BusinessExceptionError
from lib.logger import log

NOT_CHECK_DIR = [
	'/admin',
	'/static',
]


class ResponseWrapper(object):

	def process_response(self, request, response):
		for start_with in NOT_CHECK_DIR:
			if request.path.startswith(start_with):
				return response

		if isinstance(response, HttpResponse):
			return response
		else:
			resp_d = {
				"retcode": Resp.RESP_OK.code,
				"message": Resp.RESP_OK.msg,
				"data": response or {}
			}
			content = json.dumps(resp_d)
			return HttpResponse(content, content_type='application/json; charset=utf-8')

	def process_exception(self, request, exception):
		if isinstance(exception, BusinessExceptionError):
			resp_d = {
				"retcode": exception.code,
				"message": exception.msg,
				"data": exception.data,
			}
		else:
			log.exception('process request failed', exc_info=exception)
			resp_d = {
				"retcode": Resp.RESP_SERVER_ERROR.code,
				"message": Resp.RESP_SERVER_ERROR.msg,
				"data": {}
			}
		return HttpResponse(json.dumps(resp_d), content_type='application/json; charset=utf-8')
