import time
from datetime import datetime as dt

hosts_temp = "hosts.txt"
hosts_path=r"/etc/hosts"
redirect= "127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 12) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16) :
        print("working hours...")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content :
                    pass
                else :
                    file.write(redirect + " "+ website + "\n")
    else:
        with open("hosts.txt",'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list) :
                    file.write(line)
            file.truncate()
        print("have fun...")
    time.sleep(5)
