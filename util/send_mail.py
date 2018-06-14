#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

class SendEmail:
    global send_user
    global email_host
    global password
    password = "lunkbrgwqxhfjgxx"
    email_host = "smtp.qq.com"
    send_user = "xxx@qq.com"

    def send_mail(self,user_list,sub,content):
        user = "shape" + "<" + send_user + ">"

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)

        # 邮件正文内容
        message.attach(MIMEText(content, 'plain', 'utf-8'))

        # 构造附件（附件为txt格式的文本）
        filename = '../log/log.txt'
        time = datetime.date.today()
        att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="%s_Log.txt"'% time
        message.attach(att)

        server = smtplib.SMTP_SSL()
        server.connect(email_host,465)# 启用SSL发信, 端口一般是465
        # server.set_debuglevel(1)# 打印出和SMTP服务器交互的所有信息
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main(self,pass_list,fail_list,no_run_list):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        #未执行的用例
        no_run_num = len(no_run_list)
        count_num = pass_num + fail_num + no_run_num

        #成功率、失败率
        '''
        用%对字符串进行格式化
        %d 格式化整数
        %f 格式化小数；想保留两位小数，需要在f前面加上条件：%.2f；用%%来表示一个%
        如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串 
       '''
        pass_result = "%.2f%%" % (pass_num/count_num*100)
        fail_result = "%.2f%%" % (fail_num/count_num*100)
        no_run_result = "%.2f%%" % (no_run_num/count_num*100)

        # user_list = ['xxx@qq.com','xxx@qq.com']
        user_list = ['xxx@qq.com']
        sub = "接口自动化测试报告"
        content = "接口自动化测试结果:\n通过个数%s个，失败个数%s个，未执行个数%s个：通过率为%s，失败率为%s，未执行率为%s\n日志见附件" % (pass_num,fail_num,no_run_num,pass_result,fail_result,no_run_result)
        self.send_mail(user_list,sub,content)





