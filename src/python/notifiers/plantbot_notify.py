#!/usr/bin/env python
import sys, os, time

# Import required modules
sys.path.append(os.environ['PLANTBOT_HOME'] + "/src/python/")
from sensor_reader import SensorReader

reader = SensorReader()

def handleMoistValues(self, last_date):
    """Handles Sensor values and notifies if they have changed"""

    now = int(round(time.time() * 1000))
    if now - last_date >= 60 * 1000 * 30: # Every 30 minutes
        last_date = now

        reader.read()
        moist = reader.getMoistPercentage()

        def thirsty():
            return "I am thirsty. Please give me water."

        if moist < 30:
            self.q.put(thirsty)

    return last_date

def handleLightValues(self, last_value):
    """Handle light values and notifies if they have changed"""
    light = reader.getLightValue()

    def goodnight():
        return "Good Night."
    def goodmorning():
        return "Good Morning."

    if light == 1 and last_value != light:
        self.q.put(goodnight)

    if light == 0 and last_value != light:
        self.q.put(goodmorning)

    return light