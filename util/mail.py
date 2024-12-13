import os
import smtplib
import ssl
from email.message import EmailMessage


class MailSender(object):

    def __init__(self) -> None:
        # 第三方 SMTP 服务
        self.mail_host = os.getenv("SELF_DAILY_MAIL_HOST")  # 设置服务器
        self.mail_user = os.getenv("SELF_DAILY_MAIL_NAME")  # 用户名
        self.mail_pass = os.getenv("SELF_DAILY_MAIL_PASSWORD")  # 口令

    def send_to(self, subject, html_msg, receivers):
        message = EmailMessage()
        message['subject'] = subject
        message['From'] = authorization = os.getenv("SELF_DAILY_MAIL_NAME")
        message['To'] = receivers
        message.set_content(subject)
        message.add_alternative(html_msg, subtype='html')
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.mail_host, 465, context=context) as smtp:
            smtp.login(self.mail_user, self.mail_pass)
            smtp.sendmail(self.mail_user, receivers, message.as_string())
        print("邮件发送成功")
