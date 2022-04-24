# Must have line of code to pack data files.
import os
import sys
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS) 
# Must have line of code to pack data files.

try:
    import json
    from difflib import get_close_matches
    import pyttsx3

    engine = pyttsx3.init()
    data= json.load (open("data.json"))

    restart=True

    while restart!='9':
        def dictonary(w):
            w=w.lower()
            if w in data:
                return data[w]
            elif w.title() in data:
                return data[w.title()]
            elif w.upper() in data:
                return data[w.upper()]          
            elif len(get_close_matches(w , data.keys())) > 0:
                yn= input("Did you mean %s ? Press 'Y' if yes otherwise 'N' for no : " % get_close_matches(w, data.keys())[0])
                if yn.upper()=="Y":
                    return data[get_close_matches(w , data.keys())[0]]
                elif yn.upper()=="N":
                    return "Check your word again!"
                else:
                    return "Answer is not acceptable!"
            else:
                return "Word not exist!"

        word=input("Type word you want to search: ")

        output= dictonary(word)

        if type(output) == list:
            for i in range(len(output)) :
                print(f'Meaning-{i+1}: {(output[i]).strip("[]")}')
                engine.say(output[i])
                engine.runAndWait()

        else:
            print(output)
            engine.say(output)
            engine.runAndWait()

        restart=input("Press any key to continue or press 9 to exit: ")

except:
    print('pyttsx3 package Not Found.\n\nPlease execute below steps command to install it.\n')
    print('Command: conda install pyttsx3 OR pip install pyttsx3')
     