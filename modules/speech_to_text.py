import speech_recognition as sr

def audio_to_text(audio_path):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio, language="en-IN")
        print("Transcript:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("Speech recognition: Could not understand audio")
        return ""

    except sr.RequestError as e:
        print("Speech recognition request error:", e)
        return ""

    except Exception as e:
        print("General speech recognition error:", e)
        return ""