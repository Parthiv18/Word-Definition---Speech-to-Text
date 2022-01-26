import speech_recognition as sr
from bs4 import BeautifulSoup
import requests

# function to get MAIN word 
def word(URL,query):
    text = query.split(' ')
    if(text[0]=="define" or text[1]=="of" or text[1]=="is"): # [define ...] [what is ...] [definition of ...] [meaning of ...]
        return URL + str(text[-1]) 
    elif(text[-1]=="is"or text[-1]=="means"): # [meaning of this ... is] [what does ... means]
        return URL + str(text[-2])
    elif(text[-1]=="meaning"): # [... meaning] 
        return URL + str(text[0]) 
    return URL

# Setting up Mic
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening......")
    audio = r.listen(source)
    r.adjust_for_ambient_noise(source)

try:
    # Code to get voice from mic
    print("Recognizing...")    
    query = r.recognize_google(audio, language='en-in')
    print(f"USER: {query}\n")
            
    # Get website to parse
    r1 = requests.get(str(word("https://www.merriam-webster.com/dictionary/",query)))
    
    # Begin parse
    soup = BeautifulSoup(r1.text, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib    
    ram = soup.find_all('span', {'class': 'dtText'}) #('span', {'class': 'sb-0'})  find 
    
    # Counter for Test 
    # Loop to print definition
    emp = []
    for span in ram:        
        #print(span.text)
        emp.append(span.text) 
    print(*emp, sep="\n")

except Exception:
    print(Exception) 

