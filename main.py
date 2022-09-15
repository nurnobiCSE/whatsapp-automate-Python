import datetime as dt
import pywhatkit as pwk

def whatsappautomate():
    currentTime = dt.datetime.now()
    currentTime = currentTime.strftime("%d/%m/%Y-%H:%M:%S")
    currentTime = currentTime.split("-")
    time = currentTime[1].split(":")
    h = int(time[0])
    m = int(time[1])
    s = int(time[2])
    print(h,m,s)
    if h <12:
        msg = "Good morning"
    elif 12 <= h <18:
        msg = "good afternoon"
    elif h > 18 <19:
        msg = "Good evening"
    else:
        msg = "Good night"
    print(msg)

    data = {
        "name": "+880************",
        "name2": "+880***********"
    }
    name = input("whom do you want to knock : ")
    for i in data:
        if i==name:
            res_name=i
            res_no = data[i]
    msg = msg+" "+ res_name + " i knocked you throw python "
    m =  m+1
    pwk.sendwhatmsg(res_no,msg,h,m)
whatsappautomate()



