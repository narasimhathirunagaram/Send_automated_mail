import webbrowser
import time
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
url="https://mail.google.com/mail/u/0/#inbox?compose=new"
email_to="xxxxxxx@gmail.com"  #receiver email
subject="Hello! This is an automated mail"
msg="Sending mail using python scripting."

webbrowser.open(url)
time.sleep(9)

shell.SendKeys(email_to, 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys(subject, 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys(msg, 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys("{ENTER}", 0)
