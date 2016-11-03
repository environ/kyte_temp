# kyte_temp
Heating and temp control

	sudo git clone .....git

 	sudo crontab -e
 	@reboot sudo python -u /home/pi/kyte_temp/kyte_temp.py >> /home/pi/kyte_temp/kyte_temp.log &
    */60 * * * * sudo /home/pi/kontroll.sh

<<<<<<< Updated upstream
        # m h  dom mon dow   command
        @reboot sudo python -u /home/pi/kyte_temp/kyte_temp.py >> /home/pi/kyte_temp/kyte_temp.log &
        */60 * * * * sudo /home/pi/kyte_temp/kontroll.sh
        #0 */12 * * * sudo /sbin/shutdown -r now

=======
>>>>>>> Stashed changes

 	nano kyte_temp.log

 	chmod 666 kyte_temp.log 

