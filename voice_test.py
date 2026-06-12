import speech_recognition as sr

secret_code = "apple"

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak the secret code:")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio).lower()

    print("You said:", text)

    if text == secret_code:
        print("VOICE VERIFIED")
    else:
        print("WRONG CODE")

except:
    print("Could not understand audio")