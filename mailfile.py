##________This portion works so dont touch it...
## In the Gmail account we need to allow less secure apps in the security
##import smtplib 
##
### creates SMTP session 
##s = smtplib.SMTP('smtp.gmail.com', 587) 
##
### start TLS for security 
###smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
##s.ehlo()
##s.starttls()
##s.ehlo()
### Authentication 
##s.login("SENDER-USERNAME", "SENDER-PASSWORD") 
##
### message to be sent 
##message = "Message_you_need_to_send"
##
### sending the mail 
##s.sendmail("SENDER-USERNAME", "RECEIVER-USERNAME", message) 
##
### terminating the session 
##s.quit() 
##
##
##__
