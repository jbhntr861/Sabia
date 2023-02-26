import speech_recognition as sr
import logging

class VoiceRecognition:
    def __init__(self):
        self.logger = logging.getLogger('Sabia')
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.logger.info("Declare thine words! Mote thy request! for Sabia hearkens...")
            audio = r.listen(source)
        data = ""
        try:
            data = r.recognize_google(audio)
            self.logger.info("I herde thee saye.." + data)
        except sr.UnknownValueError:
            self.logger.error("S'rry, I understood thee not. Pray ye repeat thine words.")
        except sr.RequestError as e:
            self.logger.error("Request Failed; {0}".format(e))
        return data
