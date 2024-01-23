import os
import time
import platform
from plyer import notification

OS = platform.system()

print("start")
while True:
    time.sleep(3600)
    if(OS == "Darwin"):
        command = "osascript -e \'say \"Hey Pritam drink water\"\'; osascript -e \'display alert \"Hey Pritam, Drink water\"\'"
        os.system(command)
    elif(OS == "Win32"):
        notification.notify(
title = "Drink Reainder",
message = "Hey Pritam, Drink water",
timeout = 10
)