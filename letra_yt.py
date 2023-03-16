import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as recurso:
    print("Say Something...")
    audio = r.listen(recurso)
    try:
        text = r.recognize_google(audio,language='es-ES')
        print("What did you say: {}".format(text))
        with open("audio.wav","wb") as fichero:
            fichero.write(audio.get_wav_data())
    except:
        print("I am sorry! I can not understand!")