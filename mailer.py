import smtplib
import json
import logging

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import make_msgid, formataddr, formatdate

MAIL_SERVER = 'smtp.gmail.com:587'

logger = logging.getLogger()

class Mailer:
    def __init__(self, cred_path):
        with open(cred_path) as f:
            data = json.load(f)
            self.username = data['username']
            self.password = data['password']

            s = smtplib.SMTP(MAIL_SERVER)
            s.starttls()
            logger.info('Connecting to Google...')
            s.login(self.username, self.password)
            logger.info('Connection complete')
            self.s = s

    def send(self, toaddrs, fromaddrs='experiment@example.com',
            subject='experiment', body='experiment', payload=None):

        msg = MIMEMultipart()
        msg['From'] = fromaddrs
        msg['To'] = ', '.join(toaddrs)
        msg['Subject'] = subject
        msg['Message-Id'] = make_msgid()
        msg['Date'] = formatdate(localtime=True)

        msg.attach(MIMEText(body, 'plain'))

        if payload is not None:
            img = MIMEApplication(payload[1].read())
            img.add_header('Content-Disposition',
                'attachment; filename="%s"' % payload[0])
            msg.attach(img)

        logger.info('Sending mail...')
        self.s.sendmail(fromaddrs, toaddrs, msg.as_string())
        logger.info('Sent mail')
