import getpass
import os
import json
import importlib.util
#from Client import *
import platform
import socket
from datetime import datetime


spec_fileanalyzer = importlib.util.spec_from_file_location("module.name", "C:\Program Files\ALEKSI\FileAnalyzer\\fileAnalyzer.py" )
foo_fileanalyzer = importlib.util.module_from_spec(spec_fileanalyzer)
spec_fileanalyzer.loader.exec_module(foo_fileanalyzer)

details = list()

def get_username():
    username = getpass.getuser()
    print(username)
    return username


def scan_file_dropbox():
    i = 0
    for path, dirs, files in os.walk(r'C:\Users\ARJ'):
        for f in files:
            i = i+1
            if f.endswith('.dropbox'):
                print(os.path.join(path, f))
    print('Scanned ' + str(i) + ' files')


def get_Processes_dropbox():
    ps_dropbox = os.system('wmic process get description,executablepath | find /I "dropbox" ')
    print(ps_dropbox)
    return ps_dropbox

def get_Processes_drive():
    ps_drive = os.system('wmic process get description,executablepath | find /I "drive" ')
    print(ps_drive)
    return ps_drive

def get_registryvalues_drive():
    reg_drive = os.system('REG QUERY HKLM\Software\Google\Drive /se #')
    print(reg_drive)
    return reg_drive

def get_registryvalues_dropbox():
    reg_dropbox = os.system('REG QUERY HKCU\Software\Dropbox\ks /se #')
    print(reg_dropbox)
    return reg_dropbox

def get_syncloc_dropbox():
    path = r"C:\Users\ARJ\AppData\Local\Dropbox\info.json"
    if os.path.isfile(path) == True :
        f = open(path, "r")
        contents = f.read()
        contents = contents.split('"')[5]
        for root, dirs, files in os.walk(contents):
            for file in files:
                print(file)


def up_time(up_time):
    return up_time


#get_username()
#get_Processes_dropbox()
#get_registryvalues_drive()
#get_registryvalues_dropbox()

get_syncloc_dropbox()

#path = r'C:\Users\\' + get_username() +'\\Dropbox'

#print(path + "\n")

#print("content : \n")
#for i in os.listdir(path):
#        print()

#i = 0
#for path, dirs, files in os.walk(r'C:\Users\ARJ\Dropbox'):
#    for f in files:
#        i = i+1
#        if f.endswith('.dropbox'):
#            print(os.path.join(path, f))



#os.system('wmic process get description,executablepath | find /I "dropbox" ')
#os.system('REG QUERY HKLM\Software\Google\Drive /se #')


#f = open(r"C:\Users\ARJ\AppData\Local\Dropbox\info.json", "r")
#contents = f.read()

def get_dropbox():
    username = get_username()
    info_json = r"C:\Users\\" + username + "\AppData\Local\Dropbox\info.json"

    if os.path.isfile(info_json) == True :

        with open(info_json, 'r') as f:
            distros_dict = json.load(f)

        root = ""
        for distro in distros_dict['personal']['path']:
            root = root + distro

        print(root)

        for path, subdirs, files in os.walk(root):
            for name in files:
                cl = foo_fileanalyzer.fileAnalyzer(os.path.join(path, name))
                #print(cl)

                #print(">>>>>>>>>>>>>>"+ str(cl[0]))
                details = cl[1]
                #print(">>>>>>>|>>>>>>>" + str(details[0]))
                #print(">>>>>>>|>>>>>>>" + str(details[1]))
                #print(">>>>>>>|>>>>>>>" + str(details[2]))

                up_time = datetime.now()
                up_link = "Dropbox"
                severity = details[0]
                policy_name = details[1]
                hostname = socket.gethostname()
                os_name = platform.platform()
                version = "1.0.0.1"
                details = "Check"
                host_user = getpass. getuser()
                filename = "name"
                filepath = os.path.join(path, name)
                
                data1 = {"moduleType": "cloud",
                         "alertDetails": {"up_time": up_time, "up_link": up_link, "severity": severity, "policy_name": policy_name},
                         "hostdetails": {"hostname": hostname, "os": os_name, "version": version, "details": details, "host_user": host_user},
                         "evidence": {"filename": filename, "filepath": filepath}, "timestamp": timestamp}

                client = client(data1)

    else:
        print("Error Dropbox :info.jason file not found !!")

get_dropbox()
