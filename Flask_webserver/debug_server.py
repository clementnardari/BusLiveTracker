from threading import Timer
from flask import Flask, render_template
import time
import json
import MBTAApiClient

# ------------------
#    BUS LOCATION  
# ------------------

# Initialize buses list by doing an API call to the MBTA database below
buses = MBTAApiClient.callMBTAApi()

#Update the function below
def update_data():
    global buses
    buses = MBTAApiClient.callMBTAApi()


def status():
    for bus in buses:
        print(bus)

def timeloop():
    print(f'--- ' + time.ctime() + ' ---')
    status()
    update_data()
    Timer(5, timeloop).start()

timeloop()
