from commands import *


direct={
    'list':lst,
    'dirs': lst_dirs,
    'date': get_date,
    'clear':clear_screen,
    'time' : get_time,
    'time-hours':get_hour,
    'time-mins':get_min,
    'time-secs':get_sec,
    'cat':catt,
    'head':head,
    'tail':tail,
    'copy_file':copy_file,
    'remove_file':remove_file,
    'empty_file':empty_file,
    'ipconfig':ipconfig,
    'pwd':pwd,
}
while True:
    try:
        stin=input('$ ').lower()
        length=len(stin.split())
        if length==2:
            name,arg=stin.split()
            direct[name](arg)
        elif length==3:
            name,n,file=stin.split()
            if name=='head'or name=='tail':
                direct[name](file,abs(int(n)))
            elif name=='copy_file':
                direct[name](n,file)
        elif stin=='exit':
            break
        else:
            direct[stin]()
    except KeyError:
        print('Command doesnot Exist')
        log.error('wrong command written')
    except FileNotFoundError:
        print('no such file exists')
        log.error("File not found")





