import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as source:
    print("I'm listening")
    try:
        audio = rec.listen(source, timeout=5,phrase_time_limit=5)
        print('I think you said '+ rec.recognize_google(audio))
    
    except sr.UnknownValueError: 
        print('please repeat again')
    except sr.WaitTimeoutError:
        print("I'm waiting you to talk")
    except sr.RequestError:
        print('No internet connection')
