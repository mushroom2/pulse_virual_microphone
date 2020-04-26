#! /bin/bash
echo "Writing audio file to virtual microphone."
ffmpeg -re -i output.wav -f s16le -ar 16000 -ac 1 - > $HOME/audioFiles/virtmic