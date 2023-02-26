import speech_recognition as sr

class UserInput:
    def __init__(self):
        self.r = sr.Recognizer()

    def process_audio(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            try:
                audio = self.r.listen(source, timeout=5)
                prompt = self.r.recognize_google(audio)
                return prompt
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")
                return None
            except sr.RequestError as e:
                print(f"Sorry, there was an error processing your request: {e}")
                return None
