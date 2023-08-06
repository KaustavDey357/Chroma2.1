import speech_recognition as sr
from pydub import AudioSegment
import pyaudio
import wikipedia
from gtts import gTTS
from playsound import playsound
import os
from PIL import Image
import io
import requests

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
mic = sr.Microphone()
r = 2
q = 1
o = "How can I help you today?"
print("Hello I'm Chroma2.1, nice to meet you")
playsound("welcome.mp3")
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

while r > 0:
    with mic as source:

        recognizer.adjust_for_ambient_noise(source)
        print(o)
        playsound("welcomez.mp3") if q > 1 else playsound("welcomer.mp3")
        if q > 1:
            o = "Anything else?"
        else:
            o = "How can I help you today?"

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(text)
        if text == 'Quit' or text == 'quit' or text == 'quite':
            t1 = gTTS("Thanks for using Chroma2.1")
            t1.save("welcomet.mp3")
            playsound("welcomet.mp3")
            os.remove("welcomet.mp3")
            print("Thanks for using Chroma2.1")
            break

        else:
            text = text.split()

            def wordcount(Basic, text):

                file = open(Basic, "r")
                read = file.readlines()
                file.close()

                for i in range(len(text)):

                    word = text[i-1]

                    for j in range(len(read)):

                        sentence = read[j]
                        line = sentence.split()

                        for z in range(len(line)):
                            each = line[z]
                            line2 = each.lower()
                            line2 = line2.strip(",.!@#$%^&*<>~")
                            if word == line2:
                                if word in text:
                                    text.remove(word)

                            elif (word.lower()) == line2:
                                if word in text:
                                    text.remove(word)
                            z += 1
                        j += 1
                    i += 1

            wordcount("Basic.txt", text)
            # text = ' '.join(map(str, text))

            try:
                s = wikipedia.summary(text, sentences=3)
            except:
                text = ' '.join(map(str, text))
                s = wikipedia.summary(text, sentences=3)
            t1 = gTTS(s)
            t1.save("welcomet.mp3")

            def query(payload):
                response = requests.post(
                    API_URL, headers=headers, json=payload)
                return response.content
            t = s
            s = s.split()

            image_bytes = query({
                "inputs": s[0],
            })
            image = Image.open(io.BytesIO(image_bytes))
            image.show()
            image_bytes = query({
                "inputs": s[1],
            })
            image = Image.open(io.BytesIO(image_bytes))
            image.show()
            image_bytes = query({
                "inputs": s[2],
            })
            image = Image.open(io.BytesIO(image_bytes))
            image.show()
            print(t)
            playsound("welcomet.mp3")
            q += 1
            os.remove("welcomet.mp3")

    except sr.UnknownValueError:
        print("Sorry I cannot understand")
        s = "Sorry I cannot understand"
        t1 = gTTS(s)
        t1.save("welcomet.mp3")
        playsound("welcomet.mp3")
        os.remove("welcomet.mp3")

    except sr.RequestError:
        print("Speech service down\n")
        s = "Speech service down"
        t1 = gTTS(s)
        t1.save("welcomet.mp3")
        playsound("welcomet.mp3")
        os.remove("welcomet.mp3")
# Import the required module for text
# to speech conversion

# s = wikipedia.summary(audio, sentences=5)
# print(s)
# t1 = gTTS(s)
# t1.save("welcome.mp3")
# playsound("welcome.mp3")
