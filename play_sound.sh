play_sound.sh 
#!/bin/bash

echo "Playing MP3s..."
sleep 5
mpg321 -v -a hw:1 -o alsa --random -B /mnt/usb/mp3s &
