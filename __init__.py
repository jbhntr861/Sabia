from .audio_processor import AudioProcessor
from .voice_recognition import VoiceRecognition
from .response_generator import ResponseGenerator
from .text_to_speech import TextToSpeech

class Sabia:
    def __init__(self):
        self.audio_processor = AudioProcessor()
        self.voice_recognition = VoiceRecognition()
        self.response_generator = ResponseGenerator()
        self.text_to_speech = TextToSpeech()

    def run(self):
        while True:
            audio = self.voice_recognition.listen()
            if audio:
                preprocessed_audio = self.audio_processor.preprocess_audio(audio)
                response = self.response_generator.generate_response(preprocessed_audio)
                if response:
                    self.text_to_speech.speak(response)
