import sys, socket, json, time
import requests, subprocess, psutil
from bs4 import BeautifulSoup



# -- made by YourWonders, aka "Yama"


sa1 = sys.argv[1]

cmd_1 = {'basic ping':'pn',
         'website status code':'wp',
         'webscrape command':'ws',
         'local network monitor':'lm',
         'username look up':'ul'}       



def sysPing():

    # -- user must input an ipv4 address
    ipver = socket.gethostbyname(sys.argv[2])

    if ipver:

        p = subprocess.run(['ping','-c','3',ipver],
                       capture_output=True,
                       shell=False,
                       text=True)
        
        sys.stdout.writelines("Initializing ping...\n")
        sys.stdout.writelines(f"\n{p.stdout[p.stdout.find("3 packets"):]}\n")
        sys.stdout.writelines("Ping was successful!\n")
        

    else:

        sys.stdout.writelines("Unexpected Error Has Occurred\n")


def sysWebStat():
    
    if 'https://' in sys.argv[2]:

        r = requests.get(sys.argv[2])

        r_strip = sys.argv[2][8:]

        web_ip = socket.gethostbyname(r_strip)

        web_loc = subprocess.run(['curl', f'ipinfo.io/{web_ip}'],
                                 capture_output=True,
                                 shell=False,
                                 text=True)
        
        web_json = json.loads(web_loc.stdout)

        sys.stdout.writelines(

f"""
-- COMPLETE STATUS OF URL --

[URL] -> {r.url}
[STATUS CODE] -> {r.status_code}
[CITY] -> {web_json['city']}
[COUNTRY] -> {web_json['country']}
[SERVER] -> {web_json['org']}

"""

)

    elif sys.argv[2] == 'scan':
        
        if 'https://' in sys.argv[3]:

            http_strip = sys.argv[3][8:]

            scn_web = subprocess.run(['nmap','-p','1-500', f'{http_strip}'],
                                     shell=False,
                                     text=True,
                                     capture_output=True)
            
            
            temp = scn_web.stdout.find('PORT')

            sys.stdout.writelines(f'[PORT URL] -> {scn_web.stdout[temp:]}\n')


        elif socket.gethostbyname(f'{sys.argv[3]}') in sys.argv[3]:

            ip_prt = subprocess.run(['nmap', '-p', '1-500',f'{socket.gethostbyname(sys.argv[3])}'],
                                    text=True,
                                    shell=False,
                                    capture_output=True)
            
            temp_ip = ip_prt.stdout.find('PORT')

            sys.stdout.writelines(f'[PORT IPV4] -> {ip_prt.stdout[temp_ip:]}\n')


    elif sys.argv[2] == socket.gethostbyname(sys.argv[2]):

        ip_sub = subprocess.run(['curl',f'ipinfo.io/{sys.argv[2]}'],
                                shell=False,
                                capture_output=True,
                                text=True)
        
        ip_json = json.loads(ip_sub.stdout)

        sys.stdout.writelines(

f"""
-- COMPLETE STATUS OF IPV4 -- 

[IPV4] -> {ip_json['ip']}
[STATUS] -> AVAILABLE
[CITY] -> {ip_json['city']}
[COUNTRY] -> {ip_json['country']}
[SERVER] -> {ip_json['org']}

"""

)



def webscrapeFunction():
    
    target_web = sys.argv[2]

    web_args = {'arg 1':sys.argv[3], # -- this is like the initialization
                'arg 2':sys.argv[4]} # -- this is for the class to look into the initialization

    wr = requests.get(target_web)

    bs = BeautifulSoup(wr.text, 'html.parser')

    fnd = bs.find_all(web_args['arg 1'],
                      class_={web_args['arg 2']})
    
    for _ in fnd:
        sys.stdout.writelines(f'{_}\n')



def networkMonitorFunction():


    def maxCount():

        nm_start = 0
        nm_max = int(sys.argv[3])

        ntwrk = psutil.net_connections(kind='tcp4')

        while nm_start < nm_max:

            for i in ntwrk:

                nm_start += 1

                sys.stdout.writelines(f'(TCP) SOURCE [{i[3]}] -> DESTINATION [{i[4]}], {nm_start}\n')

                time.sleep(1)

                if nm_start == nm_max:
                    break


    def infCount():

        netwrk_inf = psutil.net_connections(kind='tcp4')

        while True:

            for i in netwrk_inf:

                sys.stdout.writelines(f"(TCP) SOURCE [{i[3]}] -> DESTINATION [{i[4]}]\n")
                time.sleep(1)


    def udpMaxFunc():

        udpnm_start = 0
        udpnm_max = int(sys.argv[3])

        u_ntwrk = psutil.net_connections(kind='udp4')

        while udpnm_start < udpnm_max:

            for i in u_ntwrk:

                udpnm_start += 1

                sys.stdout.writelines(f'(UDP) SOURCE [{i[3]}] -> DESTINATION [{i[4]}], {udpnm_start}\n')

                time.sleep(1)

                if udpnm_start == udpnm_max:
                    break


    def udpInfFunc():
        
        u_ntw = psutil.net_connections(kind='udp4')

        while True:

            for i in u_ntw:

                sys.stdout.writelines(f'(UDP) SOURCE [{i[3]}] -> DESTINATION [{i[4]}]\n')

                time.sleep(1)


    lm_cmds = {'Continuous Max':'-tcpm',
               'Continuous':'-tcpc',
               'Udp Max':'-udpm',
               'Udp Continuous':'-udpc'}


    if sys.argv[2] == lm_cmds['Continuous Max']:
        maxCount()

    elif sys.argv[2] == lm_cmds['Continuous']:
        infCount()

    elif sys.argv[2] == lm_cmds['Udp Max']:
        udpMaxFunc()

    elif sys.argv[2] == lm_cmds['Udp Continuous']:
        udpInfFunc()

    else:

        sys.stdout.writelines(f"command '{sys.argv[2]}' does not exist\n")



def userlookFunction():

    target_user = sys.argv[2]

    url_d = {'roblox look up':f'https://www.roblox.com/search/users?keyword={target_user}',
          'youtube look up':f'https://www.youtube.com/results?search_query={target_user}',
          'tik tok look up':f'https://www.tiktok.com/search/user?q={target_user}',
          'instagram look up':f'https://instagram.com/{target_user}/',
          'twitch look up':f'https://www.twitch.tv/search?term={target_user}',
          'twitter look up':f'https://x.com/search?q={target_user}&f=user'}
    

    sys.stdout.writelines(f'-- POSSIBLE MATCH FOR "{target_user}" --\n')

    for data, user in url_d.items():

        r = requests.get(user)

        sys.stdout.writelines(f"WEB PAGE STATUS ({r.status_code}) $ TARGET URLS ({user})\n")




# ----- command starts here -----

if sa1 == cmd_1['basic ping']:
    sysPing()


elif sa1 == cmd_1['website status code']:
    try:
        sysWebStat()
    except requests.exceptions.MissingSchema:
        print(f"Invalid url! '{sys.argv[2]}' is not a valid https url")

    except Exception as e:
        print("Unexpected error has occurred", e)

elif sa1 == cmd_1['webscrape command']:
    webscrapeFunction()


elif sa1 == cmd_1['local network monitor']:
    networkMonitorFunction()


elif sa1 == cmd_1['username look up']:
    userlookFunction()



elif sa1 == 'show':

    for _,__ in cmd_1.items():
        sys.stdout.writelines(f'{_} -> {__}\n')


else:
    print(f"'{sa1}' does not exist")