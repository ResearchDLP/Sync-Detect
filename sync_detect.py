import getpass
import os


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




#get_username()
#get_Processes_dropbox()
#get_registryvalues_drive()
#get_registryvalues_dropbox()

get_syncloc_dropbox()






#path = r'C:\Users\\' + username +'\\Dropbox'

#print(path + "\n")

#print("content : \n")
#for i in os.listdir(path):
#        print()

#i = 0
#for path, dirs, files in os.walk(r'C:\Users\ARJ'):
#    for f in files:
#        i = i+1
#        if f.endswith('.dropbox'):
#            print(os.path.join(path, f))

#

#os.system('wmic process get description,executablepath | find /I "dropbox" ')
#os.system('REG QUERY HKLM\Software\Google\Drive /se #')
#print(os.path.isfile(r"C:\Users\ARJ\AppData\Local\Dropbox\info.json"))

#f = open(r"C:\Users\ARJ\AppData\Local\Dropbox\info.json", "r")
#contents = f.read()



