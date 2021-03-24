# coding=utf-8
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from socket import gaierror, error


class Email(object):
    def __init__(self, sender, password, receiver, title, server, sender_name=None, message=None, html=None, files=None):
        """
        :param sender: 发件人邮箱，必填
        :param password: 发件人邮箱密码，必填
        :param receiver: 接收人邮箱，如果有多个收件人以逗号分隔，必填 Example: receiver = 'aa@aa.com;bb@aa.com'
        :param title: 邮件标题，必填
        :param server: smtp服务器，必填 腾讯可以使用smtp.exmail.qq.com，163可以使用smtp.163.com
        :param sender_name:发件人名称，非必填 填写之后收件人处会显示 sender_name<sender> Example:一个匿名用户<aa@abc.com>
        :param message:邮件正文，非必填
        :param html:html邮件正文，发送html邮件 如果同时填写了message和html，则会根据接收方邮箱版本显示，不支持html的邮箱则会显示message
        :param files:附件，非必填 可以传入单个文件的路径，也可以传入多个文件路径（需要传入list格式） 可以是相对路径，最好填绝对路径
        """
        self.__sender = sender
        self.__sender_name = sender_name
        self.__password = password
        self.__receiver = receiver
        self.__title = title
        self.__server = server
        self.__message = message
        self.__html = html
        self.__files = files
        self.__msg = MIMEMultipart('alternative')

    def _attach_file(self, att_file):
        """将单个文件添加到附件列表中"""
        try:
            att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        except FileNotFoundError as e:
            print('请检查附件地址是否正确！ %s' % e)
            return
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.__msg.attach(att)
        print('attach file {}'.format(att_file))

    def send(self):
        self.__msg['Subject'] = Header(self.__title, 'utf-8')
        # self.__msg['From'] = self.__sender if not self.__sender_name else formataddr(
        #     (Header(self.__sender_name, 'utf-8').encode(), self.__sender))
        self.__msg['From'] = Header("yk_tester", 'utf-8')
        self.__msg['To'] = ';'.join(self.__receiver)

        if self.__html:
            self.__msg.attach(MIMEText(self.__html, 'html', 'utf-8'))
        if self.__message:
            self.__msg.attach(MIMEText(self.__message, 'plain', 'utf-8'))

        if self.__files:
            if isinstance(self.__files, list):
                for file in self.__files:
                    self._attach_file(file)
            if isinstance(self.__files, str):
                self._attach_file(self.__files)
        flag = False
        try:
            smtp_server = smtplib.SMTP_SSL(self.__server, 465)
        except (gaierror and error) as e:
            print('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s' % e)
        else:
            try:
                smtp_server.login(self.__sender, self.__password)
            except smtplib.SMTPAuthenticationError as e:
                print('用户名密码验证失败！%s' % e)
            else:
                smtp_server.sendmail(self.__sender, self.__receiver, self.__msg.as_string())
                print('发送邮件<{0}>成功! 收件人：<{1}>。如果没有收到邮件，请检查垃圾箱，''同时检查收件人地址是否正确'.format(self.__title, self.__receiver))
                flag = True
            finally:
                smtp_server.quit()
                return flag

