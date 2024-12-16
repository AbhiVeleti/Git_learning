import os,shutil,socket,logging as log
from datetime import datetime

log.basicConfig(level = 10, filename="err.log" )

def lst():
    log.info('entered list commnad')
    f=[i.name for i in os.scandir('.') if i.is_file()]
    print(f)
    log.info("Exited list command")

def lst_dirs():
    log.info('entered list dir commnad')
    f=[i.name for i in os.scandir('.') if i.is_dir()]
    print(f)
    log.info("Exited list dir command")

def get_date():
    log.info('entered get date commnad')
    today=datetime.now()
    new_date=today.strftime('%d-%b-%Y').lower()
    print(new_date)
    log.info("Exited get date command")

def get_time():
    log.info('entered get time commnad')
    today=datetime.now()
    new_time=today.strftime('%H:%M:%S')
    print(new_time)
    log.info("Exited get time command")
     
def get_hour():
    log.info('entered get hour commnad')
    today=datetime.now()
    new_hour=today.strftime('%H')
    print(new_hour) 
    log.info("Exited get hour command")

def get_min():
    log.info('entered get minute commnad')
    today=datetime.now()
    new_min=today.strftime('%M')
    print(new_min) 
    log.info("Exited get minute command")

def get_sec():
    log.info('entered get seconds commnad')
    today=datetime.now()
    new_sec=today.strftime('%S')
    print(new_sec) 
    log.info("Exited get seconds command")

def catt(file):
    log.info('entered cat commnad')
    with open(file,'r') as f:
        r=f.readlines()
        for i in r:
            print(i)
    log.info("Exited cat command")

def head(file,n):
    log.info('entered head commnad')
    with open(file,'r') as f:
        first=f.readlines()[:n]
        for i in first:
           print(i)
    log.info("Exited head command")

def tail(file,n):
    log.info('entered tail commnad')
    with open(file,'r') as f:
        last=f.readlines()[-n:]
        for i in last:
            print(i)
    log.info("Exited tail command")

def copy_file(scr, dst):
    log.info('entered copy file commnad')
    if not os.path.isfile(scr):
        print("file not found")
    else:
        shutil.copy2(scr, dst)
    log.info("Exited copy file command")

def remove_file(filename):
    log.info('entered remove file commnad')
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        print("File not found") 
    log.info("Exited remove file command")  


def empty_file(filename):
    log.info('entered empty file commnad')
    if os.path.isfile(filename):
        with open(filename, "w"):
            pass
    else:
        print("File not found")
    log.info("Exited empty file command")

def ipconfig():
    log.info('entered ipconfig commnad')
    host = socket.gethostname()
    ipadd = socket.gethostbyname(host)
    print(ipadd)
    log.info("Exited ipconfig command")

def pwd():
    log.info('entered pwd commnad')
    print(os.getcwd()) 
    log.info("Exited pwd command")

def clear_screen():
    log.info('entered clear screen commnad')
    os.system('cls')
    log.info("Exited clear screen command")
