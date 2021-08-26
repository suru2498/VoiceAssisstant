import pyttsx3                           # text to speech -> Speak func()
import speech_recognition as sr          # takes command,
import webbrowser                        # for opening browser
import pywhatkit                         # for many various things
import os                                # related os
import wikipedia
import pyautogui                         # for ss, position, copy and more
import pyperclip                         # paste
import random
import cv2                               # for camera related
import keyboard
import datetime
import PyPDF2                            # for accessing pdf
import instaloader                       # instagram
import psutil                            # battery
import wolframalpha                      # for calculation

from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder

from time import sleep
import time
import requests                                # for sending HTTP request
from bs4 import BeautifulSoup                  # getting data out ou HTML
import speedtest                               # testing bandwidth speed
from pywikihow import search_wikihow           # data predictor
#from win10toast import ToastNotifier

from pytube import YouTube                        # for youtube video
from playsound import playsound                   # to play any sound
from googletrans import Translator                # translator -> hindi to eng
# for sending message and making call
from twilio.rest import Client


# --------------------------- END OF MODULE ------------------------------------------ #


Helper = pyttsx3.init("sapi5")
voices = Helper.getProperty('voices')
Helper.setProperty('voice', voices[3].id)
Helper.setProperty("rate", 150)


def Speak(audio):
    print("  ")
    Helper.say(audio)
    print(f":{audio}")
    Helper.runAndWait()


def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source, phrase_time_limit=10)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language="en-in")
            print(f"you said:{query}")

        except Exception as Error:
            return "none"

        return query.lower()


def takeCommandHindi():

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source,phrase_time_limit=10)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language="hi")
            print(f"you said:{query}")

        except Exception as Error:
            return "none"

        return query.lower()


def Wish():
    hour = int(datetime.datetime.now().hour)
    curr_time = datetime.datetime.now().strftime("%H:%M")

    if hour >= 7 and hour < 12:
        Speak(f"hello sir, good morning, the time is {curr_time}")
    elif hour >= 12 and hour <= 16:
        Speak(f"hello sir, good afternoon, the time is {curr_time}")
    else:
        Speak(f"hello sir, good evening, the time is {curr_time}")


def Temperature():
    user_api = 'c721035755e581cde8a1e8f0db3ea009'
    location = "Haldwani"

    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    #wind_spd = api_data['wind']['speed']
    date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print ("-------------------------------------------------------------")
    print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print ("-------------------------------------------------------------")
    Speak("Temperature Outside is {:.1f} degree Celcius".format(temp_city))
    Speak(f"Today will have {weather_desc}")
    Speak(f"Humidity is {hmdt} %")
    #print ("Current wind speed    :",wind_spd ,'kmph')


def Wolfram(search):

    api = "HAK47W-4A8GLQ5Q5J"
    request = wolframalpha.Client(api)
    requested = request.query(search)

    try:
        Answer = next(requested.results).text
        Speak(Answer)

    except Exception as e:
        Speak("A string value is not answerable")


# def GoogleLoc():
    Speak("Place name you want to go")
    name = takeCommand()

    url = "https://www.google.com/maps/place/" + str(name)
    webbrowser.open(url=url)
    
    sleep(5)

    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(name, addressdetails=True)

    target = location.latitude, location.longitude

    location = location.raw['address']
    target_loc = {
        "state":location.get('state', ''),
        "country":location.get('country', '')
    }

    current = geocoder.ip("me")
    current_loc = current.latlng

    distance = str(great_circle(current_loc,target))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)

    Speak(target_loc)
    Speak(f"sir, {name} is {distance} Kilomitres away from you")

def OpenAnything():
    os.startfile("D:\\")
    
    sleep(2)
    Speak("what would you like to search sir")
    pyautogui.click(x=1748, y=88)
    
    name = takeCommand()
    while True:
        if name == "none":
            name = takeCommand()
        else:
            break
    keyboard.write(name)
    keyboard.press("enter")
    Speak("here what i have found")
    Speak("just a moment")
    
    
    


#toast = ToastNotifier()
#toast.show_toast("Friday", "i am now activated sir", duration=3)




def TaskManager():

    #Wish()
    #Temperature()
   


# Search

    def YoutubeSearch():
        Speak("What do you want to Search on youtube sir")
        name = takeCommand()

        while True:
            if name == "none":
                name = takeCommand()
            else:
                break


        web = "https://www.youtube.com/results?search_query=" + name
        pywhatkit.playonyt(web)
        Speak("playing, sir")

    def GoogleSearch():
        Speak("What do you want to search on google sir")
        name = takeCommand()

        while True:
            if name == "none":
                name = takeCommand()
            else:
                break

        pywhatkit.search(name)
        try:
            wiki = wikipedia.summary(name, 2)
            Speak(f"done sir:{wiki}")
        except:
            Speak("No speakable data available")

        Speak(f"collecting some photos of {name}")

        Google_Image = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

        u_agnt = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',
        }

        Image_Folder = 'C:\\Users\\Administrator\\Desktop\\jar\\Downloads\\Images'

        num_images = 10
        search_url = Google_Image + 'q=' + name

        response = requests.get(search_url, headers=u_agnt)
        html = response.text
        b_soup = BeautifulSoup(html, 'html.parser')
        results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})

        count = 0
        imagelinks = []
        for res in results:
            try:
                link = res['data-src']
                imagelinks.append(link)
                count = count + 1
                if (count >= num_images):
                    break

            except KeyError:
                continue

        print(f'Found {len(imagelinks)} images')
        Speak('downloading Started')

        for i, imagelink in enumerate(imagelinks):
            response = requests.get(imagelink)

            imagename = Image_Folder + '/' + name + str(i+1) + '.jpg'
            with open(imagename, 'wb') as file:
                file.write(response.content)

        Speak('Downloaded Sir!')

    def Website():
        Speak("which website would you like to open, please reply in one word")
        name = takeCommand()
        
        while True:
            if name == "none":
                name = takeCommand()
            else:
                break


        name = name.replace(" ", "")
        web = "https://www." + name + ".com/"
        webbrowser.open(web)
        Speak("here it is sir")

    def How_To():
        Speak("getting data from the internet")
        max_result = 1
        how_to_func = search_wikihow(query, max_result)
        assert len(how_to_func) == 1
        Speak(how_to_func[0].summary)


# Music

    def Music_Hind():

        location = "E:\\SONGS\\Music"
        songs = os.listdir(location)
        rd = random.choice(songs)
        os.startfile(os.path.join(location, rd))
        Speak("music has started")

        while True:
            command = takeCommand()

            if "next" in command:
                new = random.choice(songs)
                os.startfile(os.path.join(location, new))
                Speak("next song is playing")

            elif "previous" in command:
                pyautogui.click(x=60, y=1014)
                Speak("Previous song is playing")

            elif "pause" in command:
                keyboard.press("space")
                Speak("music is paused")

            elif "resume" in command:
                keyboard.press("space")
                Speak("music is resumed")

            elif "close" in command:
                os.system("TASKKILL /F /im VLC.exe")
                Speak("Music is closed")
                break

            elif "keep" in command:
                Speak("music is playing in background")
                Switch()
                break

            elif "play english song" in command:
                Music_Eng()
                break
            
            elif "none" in query:
                Speak("")

    def Music_Eng():
        location = "E:\\SONGS\\memory card\\English NW"
        songs = os.listdir(location)
        rd = random.choice(songs)
        os.startfile(os.path.join(location, rd))
        Speak("music has started")

        while True:
            command = takeCommand()

            if "next" in command:
                new = random.choice(songs)
                os.startfile(os.path.join(location, new))
                Speak("next song is playing")

            elif "previous" in command:
                pyautogui.click(x=60, y=1014)
                Speak("Previous song is playing")

            elif "pause" in command:
                keyboard.press("space")
                Speak("music is paused")

            elif "resume" in command:
                keyboard.press("space")
                Speak("music is resumed")

            elif "close" in command:
                os.system("TASKKILL /F /im VLC.exe")
                Speak("Music is closed")
                break

            elif "keep" in command:
                Speak("music is playing in background")
                Switch()
                break

            elif "play hindi song" in command:
                Music_Hind()
                break

            elif "none" in query:
                Speak("")

    def Music_Yt():
        Speak("what do you want to listen on Youtube sir")
        call = takeCommand()

        while True:
            if call == "none":
                call = takeCommand()
            else:
                break

        pywhatkit.playonyt(call)
        Speak("music is started")


# Open Apps

    def Openapp():
        Speak("which app you want to open sir")
        name = takeCommand()

        while True:
            if name == "none":
                name = takeCommand()
            else:
                break

        if "after effects" in name:
            os.startfile(
                "C:\\Program Files\\Adobe\\Adobe After Effects CC 2019\\Support Files\\AfterFX.exe")
            Speak("opening")

        elif "premiere pro" in name:
            os.startfile(
                "C:\\Program Files\\Adobe\\Adobe Premiere Pro CC 2019\\Adobe Premiere Pro.exe")
            Speak("opening")

        elif "maps" in name:
            webbrowser.open(
                "https://www.google.com/maps/@29.2015999,79.5041315,15z")
            Speak("opening")

        elif "facebook" in name:
            webbrowser.open("https://www.facebook.com/")
            Speak("opening")

        elif "instagram" in name:
            webbrowser.open("https://www.instagram.com/")
            Speak("opening")

        else:
            Speak("there is no such file you have included, sir")

    def Closeapp():

        Speak("which opened app you want to close")
        name = takeCommand()

        while True:
            if name == "none":
                name = takeCommand()
            else:
                break

        if "premiere pro" in name:
            os.system("TASKKILL /F /im Adobe Premiere Pro.exe")
            Speak("closing")

        elif "after effects" in name:
            os.system("TASKKILL /F /im AfterFX.exe")
            Speak("closing")

        elif "facebook" in name:
            os.system("TASKKILL /F /im chrome.exe")
            Speak("closing")

        elif "instagram" in name:
            os.system("TASKKILL /F /im chrome.exe")
            Speak("closing")

        elif "maps" in name:
            os.system("TASKKILL /F /im chrome.exe")
            Speak("closing")

        else:
            Speak("nothing to close")

    def Camera():
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            raise IOError("cannot open webcam")

        Speak("sir, please press escape if you want to close the camera")

        while True:
            ret, img = cap.read()
            img = cv2.resize(img, None, fx=2, fy=2)
            cv2.imshow("Input", img)

            k = cv2.waitKey(1)
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()

    def Trans():
        Speak("Tell me the line you want to translate")
        talk = takeCommandHindi()

        while True:
            if talk == "none":
                talk = takeCommandHindi()
            else:
                break

        translator = Translator()
        try:
            translated = translator.translate(talk)
            Text = translated.text
            Speak(Text)
        except:
            Speak("i didn't get it properly")


# Activity

    def Screenshot():
        Speak("what should i name this file sir")
        name = takeCommand()

        while True:
            if name == "none":
                name = takeCommand()
            else:
                break

        pathname = name + ".jpg"
        path1 = "C:\\Users\\Administrator\\Desktop\\jar\\Screenshot\\" + pathname

        shot = pyautogui.screenshot()
        shot.save(path1)

        os.startfile("C:\\Users\\Administrator\\Desktop\\jar\\Screenshot\\")
        Speak("here is your screenshot")

    def Alarm():

        Speak("at what time, should the alarm will ring sir")
        Speak("example, 8 and 21 will set the alarm to 8 hour and 21 minute")

        time_to_set = takeCommand()

        while True:
            if time_to_set == "none":
                time_to_set = takeCommand()
            else:
                break

        time_now = time_to_set.replace(" and ", ":")
        Alarm_time = str(time_now)

        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")

            if current_time == Alarm_time:
                Speak("wake up sir, its time to work on our project")
                playsound(
                    "C:\\Users\\Administrator\\Desktop\\jar\\Files\\Ringtone.mp3")
                Speak("I hope you are getting up")
            elif current_time > Alarm_time:
                break

    def Download():

        Speak("ok sir, i am working on it")
        sleep(1)
        pyautogui.click(x=686, y=79)
        pyautogui.hotkey("ctrl", "c")
        value = pyperclip.paste()

        try:
            Speak("Downloading started")
            url = YouTube(str(value))
            video = url.streams.first()
            video.download('C:\\Users\\Administrator\\Desktop\\jar\\Downloads')
            Speak("Video has been downloaded sir")
            Speak("you can check out sir")
            os.startfile('C:\\Users\\Administrator\\Desktop\\jar\\Downloads')
        except Exception as e:
            Speak("Due to low internet connectivity, video is not downloading")

    def Temp():
        Speak("Place tell me the city name")
        city = takeCommand()

        while True:
            if city == "none":
                city = takeCommand()
            else:
                break

        search = "temperature in"
        url = 'https://www.google.com/search?q=' + search + city
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        Speak(f"the temperature in {city} is {temp}")

    def Switch():
        Speak("Switching Window")
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.press("left")
        Speak("where to move sir, only right or only left?")
        
        decision = takeCommand()
        
        while True:
            if decision == "none":
                decision = takeCommand()
            else:
                break
            
        if "only right" in decision:
            pyautogui.press("right")
            
        if "only left" in decision:
            pyautogui.press("left")
            
        if "long right" in decision:
            pyautogui.press("right")
            pyautogui.press("right")
    
        if "long left" in decision:
            pyautogui.press("left")
            pyautogui.press("left")
        
        
        pyautogui.keyUp("alt")
        Speak("Done sir")

    def Calculator():

        Speak("what do you want to calculate, example 2 plus 5")
        Term = takeCommand()

        while True:
            if Term == "none":
                Term = takeCommand()
            else:
                break

        Term = Term.replace("plus", "+")
        Term = Term.replace("minus", "-")
        Term = Term.replace("multiply", "*")
        Term = Term.replace("into", "*")
        Term = Term.replace("divide", "/")
        Term = Term.replace("divide by", "/")
        Term = Term.replace("by", "/")

        Final = str(Term)

        try:
            result = Wolfram(Final)
            Speak(f"{result}")

        except Exception as e:
            Speak("A string value is not accepted")

    def Battery():
        battery = psutil.sensors_battery().percent
        Speak(f"sir we have {battery} percentage battery left")

        if battery > 75:
            Speak("we have enough battery to continue work")
        elif battery >= 26 and battery <= 74:
            Speak("we can still work with the amount of battery left")
        elif battery <= 25:
            Speak("sir, you need to charge your laptop")


# Automation

    def Whatsapp():
        Speak("Opening sir")   
        os.startfile("C:\\Users\\Administrator\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
        Speak("Tell me the person name you want to interact with")
        name = takeCommand()
        
        while True:
            if name == "none":
                Speak("")
                name = takeCommand()
            else:
                break
        
        pyautogui.click(x=248, y=159)
        keyboard.write(name)
        sleep(2)
        pyautogui.click(x=233, y=345)
        Speak(f"would you like to send message to {name} or make audio or video call")

        while True:
            next = takeCommand()
            
            if "audio" in next:
                pyautogui.click(x=1690, y=85)
                Speak("any other command")

            elif "video" in next:
                pyautogui.click(x=1612, y=82)

            elif "message" in next:
                pyautogui.click(x=1083, y=981)
                Speak(f"what should i say to {name}")
                msg2 = takeCommand()

                keyboard.write(msg2)
                keyboard.press('enter')
                Speak("what would you like to do next")

            elif "close" in next:
                os.system("TASKKILL /F /im WhatsApp.exe")
                Speak("closing")
                break

            elif "repeat" in next:
                Speak(f"you can send message or make audio or video call")

    def YoutubeAuto():
        Speak("what would you like to choose, resume, pause, restart, mute, fullscreen, default view, keep, next, previous")
        
        while True:
            comm = takeCommand()

            while True:

                if comm == "none":
                    comm = takeCommand()
                else:
                    break


            if 'pause' in comm:
                keyboard.press('space bar')

            elif 'resume' in comm:
                keyboard.press('space bar')

            elif "restart" in comm:
                keyboard.press("0")

            elif "mute" in comm:
                keyboard.press("m")

            elif "full screen" in comm:
                keyboard.press("f")

            elif "default view" in comm:
                keyboard.press("t")

            elif "next" in comm:
                keyboard.press("Shift + N")

            elif "previous" in comm:
                keyboard.press("Shift + P")

            elif "keep" in comm:
                break 

            elif "repeat" in comm:
                Speak("what would you like to choose, resume, pause, restart, mute, fullscreen, default view, keep, next, previous")
            
    def ChromeAuto():
        Speak("Chrome Automation started")
        Speak("What would you like to do")

        comm = takeCommand()

        while True:
            if comm == "none":
                comm = takeCommand()
            else:
                break

        if "close tab" in comm:
            keyboard.press_and_release("ctrl+w")

        elif "open new tab" in comm:
            keyboard.press_and_release("ctrl+t")

        elif "open new window" in comm:
            keyboard.press_and_release("ctrl+n")

        elif "show history" in comm:
            keyboard.press_and_release("ctrl+h")

        elif "show download" in comm:
            keyboard.press_and_release("ctrl+j")

        elif "switch to tab" in comm:
            comm = comm.replace("switch to tab ", "")
            bb = f"ctrl + {comm}"
            keyboard.press_and_release(bb)
        
        else:
            Speak(f"you said {comm}, this is not in database")

        Speak("Done sir")

    def Insta():
        Speak("enter the user name correctly")
        name = input("Enter name here: ")
        webbrowser.open(f"www.instagram.com/{name}")
        Speak(f"here it is sir, profile of {name}")
        time.sleep(1)

        Speak(f"do you want to download profile picture of {name}")
        condition = takeCommand()

        while True:
            if condition == "none":
                condition = takeCommand()
            else:
                break

        if "yes" in condition:
            mod = instaloader.Instaloader()
            mod.download_profile(name, profile_pic_only=True)
            Speak("i am done sir, profile pic is saved in this folder")
        else:
            pass


# Other

    def SpeedTest():

        Speak("Checking speed sir...")
        speed = speedtest.Speedtest()

        downloading = speed.download()
        correctDown = int(downloading/800000)
        upload = speed.upload()
        correctUpload = int(upload/800000)

        if "downloading" in query:
            Speak(f"the downloading speed is {correctDown} MBPS")

        elif "uploading" in query:
            Speak(f"the downloading speed is {correctUpload} MBPS")

        else:
            Speak(
                f"the downloading speed is {correctDown} MBPS and uploading speed is {correctUpload} MBPS")

    def AllTasks():
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("esc")
        pyautogui.keyUp("esc")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl")

    def News():

        Speak("getting data from the internet sir, this may take some time")

        main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0c94821ea5104104b22d528f01c2bac0"
        main_page = requests.get(main_url).json()

        articles = main_page["articles"]
        head = []

        day = ['first', 'second', 'third', 'fourth', 'fifth',
               'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

        for ar in articles:
            head.append(ar['title'])
        for i in range(len(day)):
            Speak(f"today's {day[i]} news is: {head[i]}")

    def pdf_reader():
        book = open(
            "C:\\Users\\Administrator\\Desktop\\jar\\Files\\machine.pdf", "rb")
        Reader = PyPDF2.PdfFileReader(book)
        pages = Reader.numPages
        Speak(f"total number of pages in this book are: {pages}")
        Speak("enter the page from where you want to start the reading")
        pg = int(input("Please enter the page number: "))
        page = Reader.getPage(pg)
        text = page.extractText()
        Speak(text)

# Twilio

    def Message():
        Speak("what should be the message sir")
        msg = takeCommand()

        while True:
            if msg == "none":
                msg = takeCommand()
            else:
                break

        account_sid = 'AC30598a62bee5f82837e128562a1ceec0'
        auth_token = 'a8816a735cf02ec759d306e52bd4e5eb'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=msg,
                from_='+12394946267',
                to='+918954652696'
            )

        print(message.sid)
        Speak("done sir")

    def Call():
        Speak("Boss, I am calling your sister")

        account_sid = 'AC30598a62bee5f82837e128562a1ceec0'
        auth_token = 'a8816a735cf02ec759d306e52bd4e5eb'
        client = Client(account_sid, auth_token)

        message = client.calls \
            .create(
                twiml='<Response><Say>Wear mask, stay home stay and stay safe mam, your life is my life zindagi na milegi dobara mam, love you</Say></Response>',
                from_='+12394946267',
                to='+918954652696'
            )

        print(message.sid)
        Speak("done sir")

    def ChatBot():

        hello = ('hello', 'hai', 'hay', 'hey', 'hi')
        reply_hello = ('hello sir, i am jarvis', 'welcome boss, i am jarvis, your AI assistant',
        "hello sir, do you want anything")

        
        Speak("hello, ask anything sir")
        listen = takeCommand()
        while True:
            if listen == "none":
                listen = takeCommand()
            else:
                break
        chat = str(listen)

        for word in chat.split():
            if word in hello:
                reply = random.choice(reply_hello)
                Speak(reply)
               
                
        


#-------------------------- END OF FUNCTIONS --------------------------------------#

    while True:

        query = takeCommand()

        if "hello" in query:
            Speak("hello sir, i am Friday, how may i help you")
        elif "how are" in query:
            Speak("i am fine sir")

        elif "open youtube" in query:                     # youtube
            YoutubeSearch()
        elif "open google" in query:                      # google
            GoogleSearch()

            # open anything (only global)
        elif "open website" in query:
            Website()
        elif "how to" in query:                           # how to cook
            How_To()

        elif "play hindi song" in query:                  # hindi song
            Music_Hind()
        elif "play english song" in query:                # english song
            Music_Eng()
        elif "play a song" in query:                      # play a song on youtube
            Music_Yt()

        elif "open app" in query:       # open specified (locally + globally)
            Openapp()
        # close specified (locally + globally)
        elif "close app" in query:
            Closeapp()

        elif "open camera" in query:                      # open camera
            Camera()
        elif "open translator" in query:                  # translate hindi to english
            Trans()

        elif "take a screenshot" in query:                # takes a screenshot
            Screenshot()
        elif "set alarm" in query:                        # sets alarm
            Alarm()

        elif "download this video" in query:              # download video from youtube
            Download()
        elif "temperature" in query:                      # tells temp. of a particular city
            Temp()

        elif "switch window" in query:                    # switches window
            Switch()
            
        elif "calculate this" in query:                   # calculate with help of wolframalpha
            Calculator()
        elif "battery" in query:                          # check system battery
            Battery()

        elif "open whatsapp" in query:                    # automate whatsapp
            
            Whatsapp()
        elif "auto youtube" in query:                     # automate youtube
            YoutubeAuto()

        elif "auto chrome" in query or "autochrome" in query:   # automate chrome
            ChromeAuto()
        elif "open instagram" in query:                   # automate instagram
            Insta()

        elif "check internet speed" in query:             # check internet speed
            SpeedTest()
        elif "task manager" in query:                     # opens task manager
            AllTasks()

        elif "news" in query:                             # read news
            News()
        elif "read pdf" in query:                         # read pdf
            pdf_reader()

        elif "message" in query:                          # for twilio account message
            Message()
        elif "call" in query:                             # for twilio account calling
            Call()    

        elif "increase volume" in query:                  # volume up
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            
        elif "decrease volume" in query:                  # volume down
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            
        elif "mute" in query:                             # mute
            pyautogui.press("volumemute")

        elif "remember that" in query:                    # remembers what u said
            message = query.replace("remember that", "")
            Speak(f"You told me to remind that: {message}")
            remember = open("data.txt", "w")
            remember.write(message)
            remember.close()
        elif "any reminder" in query:                     # read the remainder
            remember = open("data.txt", "r")
            Speak(f"you told me that: {remember.read()}")
        elif "repeat after me" in query:                  # repeats what you said
            Speak("speak sir")
            while True:
                jj = takeCommand()

                while True:
                    if jj == "none":
                        jj = takeCommand()
                    else:
                        break

                Speak(f"you said: {jj}")
                keyboard.write(jj)

                if jj == "shut":
                    break
            Speak("I am Done sir")

        elif "pause" in query:
            keyboard.press("space")
        
        elif "play" in query:
            keyboard.press("space")
        
        elif "close" in query:
                os.system("TASKKILL /F /im VLC.exe")
                Speak("Music is stopped")
                
        
        elif "chat" in query:
            ChatBot()
            
        elif "search" in query:
            OpenAnything()

        elif "take care" in query:                        # for closing
            Speak("aww, thank you for caring about me , i love you sir,bye")
            break

        elif "go to rest" in query:                          # closing
            Speak("ok sir, i am going")
            Speak("Just say hey friday, and i will wake up again sir")
            break

        elif "go to sleep" in query:                         # closing
            Speak("going sir")
            break

        elif query == "none":
            Speak("")

        # if he didn't understand what you just said
        elif f"{query}" in query:
            Speak("pardon sir")
            Speak(f"you said : {query} , there is nothing like that")


TaskManager()

