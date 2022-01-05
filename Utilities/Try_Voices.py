import pyttsx3

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')


username = input("Enter the Name: ")
for i in range(len(voices)):
    print(voices[i].id, i)
    engine.setProperty('voice', voices[i].id)
    engine.say(f"Hello, {username}, how are you")
    engine.runAndWait()
