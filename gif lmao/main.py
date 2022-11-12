

    # THIS CODE ONLY AND I MEAN ONLY WORKS ON LINUX WITH *SPECIFICALLY* AMD GPUs


from pypresence import Presence
import psutil
import pyamdgpuinfo
import time
import random

gpu = pyamdgpuinfo.get_gpu(0)

client_id = '869994521910476842'  # Put your Client ID here, this is a fake ID
RPC = Presence(client_id)  # Initialize the Presence class
RPC.connect()  # Start the handshake loop


statuses = [
    "beavery",
    "beavy",
    "fuck henwee",
    "uwuwu",
    "building dams",
    "busy building a lodge",
    "stealing from the rich",
    "stealing from the poor",
    "stealing from the middle class",
    "watching henwee",
    "using python",
    "coming up with things to put in here",
    "rallying the patriarchy",
    "never gonna give you up",
    "be who you want to be",
    "canada was built on top of dead beavers, disgusting",
    "beaver do better work than the corps of engineers",
    "beavers are like ninjas, they work at night and are hard to find",
    "save a beaver, eat a tree",
    "dm me if you have questions about beavers",
    "\"work like a beaver\" - a fantastic quote",
]  # The quotes to choose from

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


while True:
    status = random.choice(statuses)
    for x in range(0, random.randint(120, 240)):
        if x % 4 == 0:
            tempFile = open("/sys/class/thermal/thermal_zone0/temp" )
            cpu_temp = tempFile.read()
            tempFile.close()
            
            details = f"CPU: {round(psutil.cpu_percent(), 1)}% {round(float(cpu_temp)/1024, 1)}°C"
        elif x % 4 == 1:
            details = f"GPU: {gpu.query_load()*100}% {gpu.query_temperature()}°C"
        elif x % 4 == 2:
            details = f"RAM: {round(psutil.virtual_memory().percent, 1)}%"
        elif x % 4 == 3:
            battery = psutil.sensors_battery()
            details = f"Battery: {round(battery.percent,1)}%"
            if battery.secsleft > 0:
                details += f" ({convertTime(battery.secsleft)} left)"
            if battery.power_plugged:
                details += " (Charging...)"
        else:
            details = "it broke :("

        RPC.update(
            large_image="https://c.tenor.com/9kZ81NgA1BYAAAAC/baby-beaver.gif",
            details=details,
            state=status
        )
        time.sleep(15) #Wait a wee bit
