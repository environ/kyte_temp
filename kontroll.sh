#!/bin/sh

#this script checks if the wanted service runs. If not it will start the service again.

ps auxw | grep kyte_temp.py | grep -v grep > /dev/null

if [ $? != 0 ]
then
       sudo python -u /home/pi/kyte_temp.py >> /home/pi/kyte_temp.log &
fi
