from gtts import gTTS
from subprocess import run, PIPE

class TextToSpeech:
    def __init__(self, language='en'):
        self.language = language
    
    def generate_audio(self, text, output_file='output.mp3'):
        tts = gTTS(text=text, lang=self.language)
        tts.save(output_file)
        try:
            run(['mpg321', output_file], stdout=PIPE, stderr=PIPE)
        except FileNotFoundError:
            print('mpg321 not found! Please install mpg321 to play audio files.')
        except Exception as e:
            print('Error playing audio file:', e)
