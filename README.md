# python3_interface

（1）case：存放测试用例数据的，比如请求类型get/post、请求url、请求header、请求数据等；

（2）data：获取excel文件中相应数据的方法封装，获取excel中对应表格内的数据，excel的行列数据等：get_data.py；判断用例之间是否存在依赖关系并获取依赖数据：dependent_data.py；初始化excel文件：data_config.py；

（3）dataconfig：存放请求中涉及到的header、data、cookies等数据；

（4）log：存放测试完成之后生成的日志文件，可以查看日志定位问题；

（5）main：脚本执行的主函数run_test.py

（6）util：通用方法的封装，各种不同断言方式common_assert.py；对excel文件的读写操作operation_excel.py；从请求返回数据中拿取数据作为下一个接口的请求header数据operation_header.py；从json文件中拿取想要的数据operation_json.py；将接口自动化过程中的相关日志输出到log.txt中print_log.py；根据请求类型的不同执行对应的get/post方法runmethod.py；将测试结果以邮件形式发送给相关人员send_mail.py。
