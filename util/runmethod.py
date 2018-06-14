#coding:utf-8
import requests
import json

class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        return res.json()

    def get_main(self,url,params=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=params, headers=header)
        else:
            res = requests.get(url=url, params=params)
        return res.json()

    def run_main(self,method,url,data=None,header=None,params=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,params,header)
        return res

