import speech_recognition as sr

r = sr.Recognizer()
name = "Hello Ghost"
audioText = ""

with sr.Microphone() as source:

    while True:
        print("Talk")
        audioText = r.listen(source)
        if r.recognize_google(audioText) == name:
            print("Text: " + r.recognize_google(audioText))
        elif r.recognize_google(audioText) == "exit":
            break




