import speech_recognition as sr
from bs4 import BeautifulSoup
import requests

# mean - print (title)
# dont say mean - print(what i said)

# definiation of .... [find index of OF +1 OR ... is at -1]
# what is the def of .... [find index of OF +1 OR ... is at -1]
# meaning of ... [find index of OF +1 OR ... is at -1]
# what does ... mean [find index of mean -1  OR -2]

#def website(text,arr):
#    URL = "https://www.merriam-webster.com/dictionary/" + str(text[2])
#    r1 = requests.get(URL)

def word(URL,query):
    text = query.split(' ')
    if(text[0]=="define" or text[1]=="of" or text[1]=="is"): # [define ...] [what is ...] [definition of ...] [meaning of ...]
        return URL + str(text[-1]) 
    elif(text[-1]=="is"or text[-1]=="mean"): # [meaning of this ... is] [what does ... mean]
        return URL + str(text[-2])
    elif(text[-1]=="meaning"): # [... meaning] 
        return URL + str(text[0]) 
    return URL + str(text[2])

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening......")
    audio = r.listen(source)
    r.adjust_for_ambient_noise(source)

try:
    #code to get voice from mic
    print("Recognizing...")    
    query = r.recognize_google(audio, language='en-in')
    print(f"USER: {query}\n")
            
    #get website to parse
    r1 = requests.get(str(word("https://www.merriam-webster.com/dictionary/",query)))
    
    #begin parse
    soup = BeautifulSoup(r1.text, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib
    #print(soup.span) #soup.find_all("span", class_="dtText") soup.find_all('span', attrs={'class': 'dtText'})
    ram = soup.find('span', {'class': 'dtText'}) #('span', {'class': 'sb-0'})     
    counter = 0
    for span in ram:
        #if (counter==162):
        print(span.text)
        #print(counter)
        counter = counter + 1

except Exception:
    print(Exception) 

