#!/bin/bash
INDEX=$(pacmd list-sink-inputs | grep 'index: '| cut -d' ' -f6)
module_exists=$(pactl list modules | grep sink_name=browser_stream)
echo ${#module_exists}
if [[ ${#module_exists} -eq 0 ]]; then
	pactl load-module module-null-sink sink_name=browser_stream
fi
pactl move-sink-input $INDEX browser_stream
parec -d browser_stream.monitor --file-format=wav output.wav