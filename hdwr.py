from tkinter import *
import psutil, cpuinfo, re, logging, platform, socket
import subprocess, json


lg = logging.basicConfig(level=logging.INFO,
                         format="""
LEVEL => %(levelname)s
INFORMATION => %(message)s
"""
)

try:
     drivers = str(psutil.disk_usage('/'))
except (FileNotFoundError, NameError):
    logging.critical('Linux driver cannot be found!')
    quit()

fnd_total = drivers.find('total=')
ln_total = len('total=')
total_foundation = fnd_total + ln_total

fnd_free = drivers.find('free=')
ln_free = len('free=')
free_foundation = fnd_free + ln_free

fnd_perc = drivers.find('percent=')
ln_perc = len('percent=')
perc_foundation = fnd_perc + ln_perc


perc_data = drivers[perc_foundation:-1]

keep = []

div_trill = 1_000_000_000_000

for i in re.finditer(',', drivers):
    keep.append(i.start())

drv = round(int(drivers[total_foundation:keep[0]]) / div_trill, 2)
free = round(int(drivers[free_foundation:keep[2]]) / div_trill, 2)


# ====================================

cpu = cpuinfo.get_cpu_info()['brand_raw']
mn_distro = platform.node()

# ====================================

cmd = 'echo $USER'

host_name = subprocess.run(cmd,
                           capture_output=True,
                           shell=True)

host = host_name.stdout.decode()

# ====================================

location = subprocess.run(['curl','ipinfo.io'],
                      capture_output=True,
                      shell=False,
                      text=True)

ipconfig = subprocess.run('ifconfig',
                          capture_output=True,
                          shell=False,
                          text=True)

wifi = str(ipconfig.stdout)
fnd_wifi = wifi.find('wlp')


tj = json.loads(location.stdout)

city = tj['city']
isp = tj['ip']


def wifiStats():

    tp = Toplevel()
    tp.title('wifi information')
    tp.geometry('300x300')
    tp.configure(bg='#323d92')


    def wifi_opt_function():

        wp = Toplevel()
        wp.configure(bg='#323d92')
        wp.title('wifi extended info')


        wb = Label(wp,
                      text=f'{wifi[fnd_wifi:]}',
                      bg='#323d92',
                      fg='#ffffff')

        wb.pack()


    user_ip = socket.gethostbyname(socket.gethostname())

    class TPlvlConfig:

        lbl1 = Label(tp,
                     text=f'city area -> {city}\nISP -> {isp}\nUser ipv4 -> {user_ip}',
                     bg='#5671bc',
                     fg='#ffffff')

        wifi_info = Button(tp,
                           text='more',
                           command=wifi_opt_function,
                           bg='#5671bc',
                           fg='#ffffff')


    TPlvlConfig.lbl1.pack()
    TPlvlConfig.lbl1.place(y=20)
    TPlvlConfig.wifi_info.pack()
    TPlvlConfig.wifi_info.place(y=100)

        
# ====================================
class FrameMain:

    root = Tk()
    root.title("linux hardware stats")
    root.geometry('400x400')

    root.configure(bg="#323d92")


class FunctionFrame:

    

    info1 = Label(FrameMain.root,
                  text=f'total disk space => {drv}',
                  bg="#5671bc",
                  fg="#ffffff")

    info2 = Label(FrameMain.root,
                  text=f'free space => {free}',
                  bg="#5671bc",
                  fg="#ffffff")

    info3 = Label(FrameMain.root,
                  text=f'Percentage used => {perc_data}%',
                  bg="#5671bc",
                  fg="#ffffff")

    info4 = Label(FrameMain.root,
                  text=f'CPU type => {cpu}',
                  bg="#5671bc",
                  fg="#ffffff")

    info5 = Label(FrameMain.root,
                  text=f'distro type => {mn_distro}',
                  bg='#5671bc',
                  fg="#ffffff")

    info6 = Label(FrameMain.root,
                  text=f'your name => {host}',
                  bg="#5671bc",
                  fg="#ffffff")


    button1 = Button(FrameMain.root,
                     text='network information',
                     bg='#5671bc',
                     fg='#ffffff',
                     command=wifiStats)


FunctionFrame.info1.pack()
FunctionFrame.info1.place(x=10, y=75)

FunctionFrame.info2.pack()
FunctionFrame.info2.place(x=200, y=75)


FunctionFrame.info3.pack()
FunctionFrame.info3.place(x=10,y=130)


FunctionFrame.info4.pack()


FunctionFrame.info5.pack()
FunctionFrame.info5.place(x=200,y=130)

FunctionFrame.info6.pack()
FunctionFrame.info6.place(x=10,y=175)

FunctionFrame.button1.pack()
FunctionFrame.button1.place(x=10, y=250)



FrameMain.root.mainloop()