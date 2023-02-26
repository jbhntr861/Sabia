#!/bin/bash
#####use this if you get an error like no default internal mic

# Check if an audio input device is connected
if ! lsusb | grep -q "Audio device"; then
    echo "Error: No audio input device found."
    exit 1
fi

# Check if the audio input device is properly configured
if ! amixer -D pulse sget Capture | grep -q "Front Left:"; then
    echo "Error: Audio input device not properly configured."
    exit 1
fi

# Check if necessary audio drivers are installed
if ! lspci -v | grep -i "audio device" | grep -q "Kernel driver in use:"; then
    echo "Error: Audio drivers not installed."
    exit 1
fi

# Reinstall PyAudio library
pip uninstall -y pyaudio
pip install pyaudio
