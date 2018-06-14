#coding:utf-8
from util.operation_excel import OperationExcel
from util.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
import json

class DependentData:

    def __init__(self,case_id):
        self.case_id = case_id
        self.oper_excel = OperationExcel()
        self.method = RunMethod()
        self.data = GetData()

    # 通过case_id去获取依赖case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.oper_excel.get_rows_data(self.case_id)
        return rows_data

    #执行依赖测试，获取结果
    def run_dependent(self):
        row_num = self.oper_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_value(row_num)
        header = self.data.get_request_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = self.method.run_main(method,url,request_data,header,params=request_data)
        return res

    #获取依赖字段的响应数据：通过执行依赖测试case来获取响应数据，响应中某个字段数据作为依赖key的value
    def get_value_for_key(self,row):
        #获取依赖的返回数据key
        depend_data = self.data.get_depend_key(row)
        #执行依赖case返回结果
        response_data = self.run_dependent()
        # print(depend_data)
        # print(response_data)

        return [match.value for match in parse(depend_data).find(response_data)][0]




