import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("shankarseshamsetti@gmail.com", "Iasgowrishankar@55")
message = "Message_you_need_to_send"
s.sendmail("shankarseshamsetti@gmail.com", "aashritha636@gmail.com", message)
s.quit()