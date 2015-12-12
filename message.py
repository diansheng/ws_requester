class Message():
    req="api.openweathermap.org/data/2.5/weather?q=Singapore"
    resp=""
    result=""

    def pocess_result():
        pass

    #imcomplete
    def notify():
        sender="chnlds@gmail.com"
        receivers=['liu.diansheng@gmail.com',]
        message = """From: From Fremont <%s>
        To: To Person <to@todomain.com>
        Subject: SMTP e-mail test
        
        This is a test e-mail message. %s
        """ % sender, self.result
        
        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail(sender, receivers, message)         
            print "Successfully sent email"
        except SMTPException:
            print "Error: unable to send email"
    
    def construct_request():
        pass