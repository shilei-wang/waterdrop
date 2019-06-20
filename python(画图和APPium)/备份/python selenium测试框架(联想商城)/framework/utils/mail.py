# -*- coding:utf-8 -*-
# __author__ = 'lenovo'

"""
邮件类。用来给指定用户发送邮件。可指定多个收件人，可带附件。
"""
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror, error
from utils.log import logger


class Email:
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        """初始化Email
        :param server: smtp服务器,必填。(发送邮件协议一般都是采用smtp协议，邮件接收协议一般采用pop3协议)
        :param sender: 发件人，必填。
        :param password: 发件人密码，必填。
        :param receiver: 收件人，多收件人用“；”隔开，必填。

        :param title: 邮件标题，必填。
        :param message: 邮件正文，非必填。
        :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        """
        self.server = server
        self.sender = sender
        self.password = password
        self.receiver = receiver

        self.title = title
        self.message = message
        self.files = path

        self.msg = MIMEMultipart('related')

    def _attach_file(self, att_file):
        """将单个文件添加到附件列表中 这块附件实在不是很懂，估计要对MIME很熟悉才可以"""
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name[-1]
        self.msg.attach(att)

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)  # 连接sever
        except (gaierror and error) as e:
            logger.exception(u'发送邮件失败,无法连接到SMTP服务器 %s', e)
        else:
            try:
                #注意：这条在原文中没有，如果没有会出错，是新加的
                #hotmail 需要使用STARTTLS加密验证， 将纯文本连接升级为加密连接（TLS或SSL）
                smtp_server.starttls()

                smtp_server.login(self.sender, self.password)  # 登录
            except smtplib.SMTPAuthenticationError as e:
                logger.exception(u'用户名密码验证失败！%s', e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())  # 发送邮件
            finally:
                smtp_server.quit()  # 断开连接
                # 这里可以用0,1参数代入
                logger.info(u'发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            u'同时检查收件人地址是否正确'.format(self.title, self.receiver))