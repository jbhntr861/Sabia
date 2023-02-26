import subprocess

# Check microphone
def check_microphone():
    print("Checking microphone...")

    # Record a short audio sample
    subprocess.run(["arecord", "-d", "3", "-f", "S16_LE", "-r", "44100", "-c", "2", "test.wav"])

    # Play back the audio sample
    subprocess.run(["aplay", "test.wav"])

    # Clean up
    subprocess.run(["rm", "test.wav"])

# Check ALSA
def check_alsa():
    print("Checking ALSA...")

    # Check configuration file
    subprocess.run(["cat", "/etc/asound.conf"])

    # Test command
    subprocess.run(["speaker-test", "-c", "2", "-r", "48000", "-D", "hw:0,0"])

# Check PulseAudio
def check_pulseaudio():
    print("Checking PulseAudio...")

    # Check configuration file
    subprocess.run(["cat", "/etc/pulse/default.pa"])

    # Test command
    subprocess.run(["pactl", "load-module", "module-null-sink"])

# Check JACKD
def check_jackd():
    print("Checking JACKD...")

    # Check configuration file
    subprocess.run(["cat", "/etc/jackdrc"])

    # Test command
    subprocess.run(["jackd", "-d", "alsa"])

# Set permissions for Sabia
def set_permissions():
    print("Setting permissions for Sabia...")

    # Add user to audio group
    subprocess.run(["sudo", "usermod", "-a", "-G", "audio", "sabia_user"])

# Install necessary packages
def install_packages():
    print("Installing necessary packages...")

    # Check if packages are installed and install them if necessary
    subprocess.run(["sudo", "apt", "install", "-y", "alsa-utils", "pulseaudio", "jackd", "python3-pyaudio"])
    subprocess.run(["pip", "install", "numpy", "pyaudio", "SpeechRecognition", "gtts"])

# Main function
def main():
    check_microphone()
    check_alsa()
    check_pulseaudio()
    check_jackd()
    set_permissions()
    install_packages()

if __name__ == "__main__":
    main()
