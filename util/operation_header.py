#coding:utf-8

import json
import requests
from util.operation_json import OperationJson


class OperationHeader:

	def __init__(self,response):
		self.response = response


	def get_response_url(self):
		'''
		获取登录返回的token的url
		'''
		url = self.response['data']['url'][0]
		return url

	def get_cookie(self):
		'''
		获取cookie的jar文件
		'''
		url = self.get_response_url()+"&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
		cookie = requests.get(url).cookies
		return cookie

	def write_cookie(self):
		cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
		op_json = OperationJson()
		op_json.write_data(cookie)