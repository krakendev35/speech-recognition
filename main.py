import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as source:
    print('konus dinliyorum')
    try:
        audio = rec.listen(source, timeout=5,phrase_time_limit=5)
        print('galiba '+ rec.recognize_google(audio)+' dedin')
    
    except sr.UnknownValueError:
        print('anlamadim lutfen tekrar et')
    except sr.WaitTimeoutError:
        print('neden konusmadin he dalga mi geciyosun canim?')
    except sr.RequestError:
        print('net yok')