
from src.Modules import *


class Assistant:

    def __init__(self):
        if platform.system() == "Windows":
            self.desktop_path = os.path.join(os.environ['USERPROFILE'], "Desktop")
            self.engine = pyttsx3.init('sapi5')
            self.admin = True if ctypes.windll.shell32.IsUserAnAdmin() != 0 else False
        else:
            self.desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            self.engine = pyttsx3.init('nsss')
            self.admin = True if os.geteuid() == 0 else False
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[3].id)
        self.username = None
        self.wake_word = None
        self.dic = PyDictionary()
        self.test = speedtest.Speedtest()

    def computer_copy(self):
        if self.windows():
            pyautogui.hotkey("ctrl", "c")
        else:
            pyautogui.hotkey("command", 'c')

    def get_user_info(self):
        if not os.path.exists("temp/user_info.txt"):
            self.say("What would you like me to call you sir?")
            username = self.take_command()
            print(f"\n{username}\n")
            self.say("Is this Correct?")
            choice = self.take_command()
            if "yes" not in choice or choice is None:
                self.say("Sorry, I couldn't get that, type in your name!")
                self.username = input("Enter your Name: ")
            else:
                self.say("What would you like the WAKE word to be?")
                self.wake_word = self.take_command()
                print(f"\n{self.wake_word}\n")
                self.say("Is this Correct?")
                choice = self.take_command()
                if "yes" not in choice or choice is None:
                    self.say("Sorry, I couldn't get that, type in your name!")
                    self.wake_word = input("Enter the Wake Word: ")
            with open('temp/user_info.txt', 'x') as file:
                file.write(f"username: {self.username}\n")
                file.write(f"wake_word: {self.wake_word}")
                file.close()
        else:
            with open("temp/user_info.txt", 'r') as file:
                data = file.read()
                data = data.split("\n")
                self.username = data[0][10:]
                self.wake_word = data[1][11:]

    def banner(self):
        self.clear()
        columns = shutil.get_terminal_size().columns
        print("#####################".center(columns))
        print(f"Welcome {self.username}".center(columns))
        print("#####################".center(columns))

        print("\nThis is a Voice Assistant Coded to do all the basic stuff. The features of the Assistant are:\n\n"
              "* Interact to some extent\t\t\t\t"
              "* Can open websites\n"
              "* Open gmail, google search and youtube\t\t\t"
              "* Autoplay song on Youtube using Keyword\n"
              "* Download Youtube Video with Keyword or Video link\t"
              "* Hand-Cricket Game\n"
              "* Number Guessing Game\t\t\t\t\t"
              "* Can Shutdown and Restart The Device\n"
              "* Can Clear Temporary Files\t\t\t\t"
              "* Generate QR Code\n"
              "* Can help in Converting and Editing a PDF\t\t"
              "* Extract Text from an Image\n"
              "* Tell a Joke\t\t\t\t\t\t"
              "* It can open Instagram and Facebook\n"
              "* Tell about the Weather of any place\t\t\t"
              "* Generate a Password\n"
              "* Tell Time\t\t\t\t\t\t"
              "* Open TOI for top Headlines\n"
              "* Take Screenshot\t\t\t\t\t"
              "* Capture a Picture from the Webcam\n"
              "* Can redirect you to the Typing Speed Website\t\t"
              "* Perform Internet Test Speed\n""")

    def clear(self):
        if self.windows():
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def windows():
        if platform.system() == "Windows":
            return True
        else:
            return False

    @staticmethod
    def take_command():
        listener = sr.Recognizer()
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=2)
            print("\nListening..")
            voice = listener.listen(source)
            try:
                command = listener.recognize_google(voice, language='en-IN')
                return command.lower()
            except:
                pass

    def say(self, message):
        message = message.lower()
        if message.startswith("joke<sep>"):
            message = message.replace("joke<sep>", "")
            self.engine.setProperty('rate', 150)
            self.engine.say(message)
            self.engine.runAndWait()
            self.engine.setProperty('rate', 200)
        else:
            self.engine.say(message)
            self.engine.runAndWait()

    def exiting(self):
        self.say(f"Okay {self.username}, Good Bye! See You Later!")
        exit(0)

    def greet_user(self):
        greetings = ["How are you doing?", "How may I help you?", "what's up"]
        message = random2.choice(greetings)
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.say(f"Hello, Good Morning {self.username}, {message}")
        elif 12 <= hour < 18:
            self.say(f"Hello,Good Afternoon {self.username}, {message}")
        else:
            self.say(f"Hello,Good Evening {self.username}, {message}")

    def shutdown_restart(self, count):
        if count == 0:
            self.say("Are you Sure you want to Shutdown the computer?")
        elif count == 1:
            self.say("Are you Sure you want to restart the computer?")
        command = self.take_command()
        if command is None:
            self.say("Cancelling the operation")
        elif "yes" in command:
            if self.windows():
                if count == 0:
                    self.say("Shutting Down!")
                    os.system("shutdown /s /f /t 1")
                elif count == 1:
                    self.say("Restarting the device")
                    os.system("shutdown /r /f /t 1")
            else:
                if count == 0:
                    self.say("Shutting Down!")
                    os.system("shutdown now")
                elif count == 1:
                    self.say("Restarting the device")
                    os.system("reboot")
        else:
            self.say("Cancelling the Operation!")

    def convert_to_sketch(self):
        self.say("Starting Convertor. Please Enter the Full Path to the Image")
        img_path = input("\nEnter the path to the Image:")
        self.say("Please wait while I convert This Image to a Pencil Sketch!")
        convertor = convert(img_path)
        convertor.conversion()
        sleep(1)
        self.say("The Image has been converted to a Sketch, and saved in the Same Directory!")

    def hand_cricket(self):
        self.say("Starting Hand Cricket Game!")
        sleep(0.1)
        self.clear()
        self.say("Please Enter the Username with which you would like to play!")
        username = input("Enter your Username: ")
        cricket_game = Hand_Cricket_Game(username)
        self.clear()
        cricket_game.banner()
        self.say("Please Read the Rules of the Game")
        cricket_game.information()
        sleep(4)
        cricket_game.main_game()
        while True:
            score_file = []
            with open("temp/Cricket_Score.txt", 'r') as file:
                score = file.read()
                if score.endswith("\n"):
                    score = score[:-2]
                if score.endswith("<sep>"):
                    score = score[:-5]
                score_list = score.split("<sep>")
                for listed in score_list:
                    name, scores = listed.split(":")
                    score_file.append(int(scores))
            self.say(f"Your Game is over! You Scored {score_file[len(score_file) - 1]} Runs")
            sleep(0.5)
            self.say("Do you want to Play Again?")
            choice = self.take_command()
            if choice == 'yes':
                self.say("Starting the Game, enter your moves!")
                cricket_game.main_game()
            else:
                self.say("Okay, Exiting!")
                self.clear()
                break

    def internet_speed(self):
        self.clear()
        self.say("Initiating The Internet Speed Test!")
        print("\t\t\t\tINTERNET SPEED TEST\n")
        self.say("Getting the Appropriate Servers")
        self.test.get_best_server()
        self.say("Checking the Latency:")
        ping = self.test.results.ping
        self.say(f"The Current Internet Latency is {ping.__floor__()} ms")
        print(f"\n\tPing: {ping.__floor__()} ms")
        self.say("Checking the Download Speed")
        download_speed = self.test.download()
        download_speed = download_speed / 1024 / 1024
        print(f"\n\tDownload Speed: {round(download_speed, 2)} Mbps")
        self.say(f"The Current Download Speed is {round(download_speed, 2)} Mbp s")
        self.say("Checking the Upload Speed:")
        upload_speed = self.test.upload()
        upload_speed = upload_speed / 1024 / 1024
        print(f"\n\tUpload Speed: {round(upload_speed, 2)} Mbps")
        self.say(f"The Current Upload Speed is {round(upload_speed, 2)} Mbp s")
        sleep(1)

    def guessing_game(self):
        self.say("Starting the Number Guessing Game!")
        sleep(0.5)
        self.clear()
        self.say("Please Enter the Username with which you would like to Play!")
        username = input("\nEnter username: ")
        self.clear()
        number_game = Number_Guessing_Game()
        number_game.start_game(username)

    def edit_pdf(self):
        self.say("I am Directing you to the PDF editing website")
        webbrowser.open_new_tab("https://www.sejda.com/pdf-editor")
        self.say("The website has been opened, you can now upload and edit your PDF file!")

    def pdf_convert(self):
        self.say("Opening the website where you can convert your file to a pdf")
        webbrowser.open_new_tab("https://ilovepdf.com")

    def make_qr(self, action):
        if action == 1:
            self.say("Enter the Data to be Converted to a QR Code")
            data = input("\nEnter the Data: ")
            QR_Code.qr_gen(data)
            self.say("A QR Code for the entered data has also been Generated and saved to the Desktop!")
        else:
            self.say("Enter the Path to the QR Code")
            path = input("\nEnter the Path: ")
            QR_Code.qr_detect(path)
            self.say("The Qr code has been scanned and the extracted data has been displayed on the screen")

    @staticmethod
    def clean_command(command):
        general_words = ["can you", "wikipedia", "search for", "on", "app", "application", "open", "search", "play",
                         "on youtube", "google", "search", "website", "youtube", "what is the", "meaning of",
                         "what does", "mean"]
        if command.startswith("look"):
            command = command.replace("look", "")
        for words in general_words:
            if words in command:
                command = command.replace(f"{words}", "")
        return command.strip()

    def wikipedia(self, statement):
        statement = self.clean_command(statement)
        self.say(f"Searching for {statement} on Wikipedia ")
        sleep(1)
        results = wikipedia.summary(statement, sentences=3)
        self.say("According to Wikipedia ")
        print("\n\n" + results + "\n\n")
        self.say(results)

    def youtube(self):
        self.say("Opening Youtube!")
        sleep(1)
        webbrowser.open_new_tab("https://youtube.com")

    def play_yt(self, statement, action):
        if action == 1:
            statement = self.clean_command(statement)
            self.say(f"Playing {statement} on Youtube")
        pywhatkit.playonyt(statement)

    def download_yt_video(self):
        self.say("Do you have the link of the Video?")
        user_input = self.take_command()
        if "yes" in user_input:
            self.say("Enter the link of the Video: ")
            user_link = input("Enter the Link: ")
            self.say("Searching for the Video on Youtube")
            sleep(0.5)
        else:
            self.say("No worries, tell me the name of the video")
            video_name = self.take_command()
            self.play_yt(video_name, 0)
            self.say("Looking for the video on youtube")
            sleep(5)
            pyautogui.press('space')
            sleep(0.5)
            self.say("Is this the video you were looking for? ")
            sleep(0.5)
            if "yes" in self.take_command():
                if self.windows():
                    pyautogui.hotkey("ctrl", 'l')
                    sleep(0.5)
                    self.computer_copy()
                    sleep(0.5)
                    pyautogui.hotkey("alt", 'tab')
                else:
                    pyautogui.hotkey("command", 'l')
                    sleep(0.5)
                    self.computer_copy()
                    sleep(0.5)
                    pyautogui.hotkey("command", 'tab')
                user_link = pyperclip.paste()
            else:
                self.say("Search for the Video and copy the link and paste it in the terminal!")
                sleep(0.5)
                user_link = input("Enter the Link: ")
        download = YT_Downloader(user_link)
        self.say("The Information of the Video are Displayed on the Screen!")
        download.display_video_information()
        self.say("Starting Download")
        try:
            download.get_video()
            self.say("Your Video has Been Successfully Downloaded and saved to the Downloads folder")
        except Exception as e:
            self.say("Oops! Some Error Occurred")
            print(e)

    def open_app(self, command):
        command = self.clean_command(command)
        command = command.strip()
        if self.windows():
            pyautogui.hotkey("ctrl", 'r')
            sleep(0.5)
            if "word" in command:
                pyautogui.write("winword.exe")
                pyautogui.press("enter")
                return True
            elif "excel" in command:
                pyautogui.write("excel.exe")
                pyautogui.press("enter")
                return True
            elif "powerpoint" in command or "power point" in command:
                pyautogui.write("powerpnt.exe")
                pyautogui.press("enter")
                return True
            elif "chrome" in command:
                pyautogui.write("chrome.exe")
                pyautogui.press("enter")
                return True
            elif "spotify" in command:
                pyautogui.write("spotify")
                pyautogui.press("enter")
            elif "microsoft browser" in command or "ms edge" in command:
                pyautogui.write("MSEDGE")
                pyautogui.press("enter")
            elif "control panel" in command:
                pyautogui.write("control panel")
                pyautogui.press("enter")
                return True
            elif "command prompt" in command or "cmd" in command:
                pyautogui.write("cmd")
                if "elevated" not in command:
                    pyautogui.press("enter")
                    return True
                else:
                    pyautogui.hotkey("ctrl", "shift", "enter")
                    return True
            elif "powershell" in command:
                pyautogui.write("cmd")
                if "elevated" not in command:
                    pyautogui.press("enter")
                    return True
                else:
                    pyautogui.hotkey("ctrl", "shift", "enter")
                    return True
        else:
            application_folder = "/Applications"
            for path in os.listdir(application_folder):
                if command in path.lower():
                    output = os.path.join(application_folder, str(path))
                    self.say(f"Opening {command}")
                    os.system(f"open '{output}'")
                    return True

    def tell_joke(self):
        joke = pyjokes.get_joke(language='en', category='all')
        joke = f"joke<sep>{joke}"
        self.say(joke)

    def extract_text(self):
        self.say("Enter the Path to the Image")
        path = input("Enter the Path: ")
        extractor = extract_text(path)
        extractor.get_data()
        self.say("The text has been Copied and saved in a text file in the same Directory!")

    def google(self):
        self.say("Opening Google Search Engine!")
        sleep(1)
        webbrowser.open_new_tab("https://google.co.in")

    def gmail(self):
        self.say("Opening your Gmail !")
        sleep(1)
        webbrowser.open_new_tab("https://mail.google.com")

    def instagram(self):
        self.say("Opening Instagram on browser !")
        sleep(1)
        webbrowser.open_new_tab("https://instagram.com")

    def facebook(self):
        self.say("Opening Facebook on browser !")
        sleep(1)
        webbrowser.open_new_tab("https://facebook.com")

    def meaning(self, command):
        command = self.clean_command(command)
        word = self.dic.meaning(command)
        self.say(f"{command} means {word}")

    def generate_password(self):
        self.say("Enter the Length of the Password to be Generated")
        length = int(input("\nEnter the Length: "))
        self.say(f"Generating a Random Password of {length} characters")
        generator = Password(length)
        generator.generate()
        sleep(0.5)
        self.say("The Password has been Generated and also Copied to the Clipboard.")

    def weather(self):
        self.say("Which place's Weather Report Do you want!")
        city_name = self.take_command()
        self.say(f"Fetching the Current Weather Reports of {city_name}!")
        weather_report = weather(city_name)
        temperature, humidity, wind_report = weather_report.get_report()
        temperature = int(temperature) - 273.15
        self.say(f"It is around {int(temperature)} degree celsius in {city_name}.")
        self.say(f"The humidity is {humidity} percent and the wind speed is {wind_report} metres per second")
        self.say("All the other Details are displayed on the Screen!")
        sleep(3)

    def clear_cache(self):
        self.say("Starting the Cleaning Process")
        if not self.windows():
            if not self.admin:
                os.system("rm -rf ~/Library/Caches/*")
            else:
                os.system("sudo src/cleanup.sh")
        else:
            directories = ["C:\\Windows\\Prefetch\\*", "C:\\Windows\\Temp\\*",
                           f'{os.path.expandvars("%userprofile%")}\\AppData\\Local\\Temp\\*']
            for directory in directories:
                os.system(f"del /S /F /Q {directory}")
        self.say("All the Temporary Files have been Cleaned")
        sleep(1)

    def get_new_foldername(self, path):
        name = "New Folder"
        file_path = os.path.join(path, name)
        while True:
            i = 0
            if self.path_exists(file_path):
                i += 1
                name = f"{name} ({i})"
                file_path = os.path.join(path, name)
            else:
                os.mkdir(file_path)
                break

    @staticmethod
    def path_exists(path):
        if os.path.exists(path):
            return True
        else:
            return False

    def create_folder(self, command):
        command = self.clean_command(command)
        if self.windows():
            if "Desktop" in command:
                self.get_new_foldername(self.desktop_path)
            elif "Downloads" in command or "Download" in command:
                self.get_new_foldername(self.desktop_path.replace("Desktop", "Downloads"))
            else:
                self.say("I'm sorry, I cannot create a Folder at the asked Destination.")
        else:
            if "Desktop" in command:
                self.get_new_foldername(self.desktop_path)
            elif "Downloads" in command or "Download" in command:
                self.get_new_foldername(self.desktop_path.replace("Desktop", "Downloads"))
            else:
                self.say("I'm sorry, I cannot create a Folder at the asked Destination.")

    def tell_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        self.say(f"The current time is {current_time}")

    def convert_to_audio(self):
        self.say("Enter The path to the Video File:")
        video_path = input("Enter the Path: ")
        video_convertor = video_2_audio(video_path)
        self.say("Starting the Conversion")
        video_convertor.convert()
        self.say("The Audio has been extracted and saved to the Desktop")

    def news(self):
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        print(news)
        self.say("Top Headlines on the Times Of India's website has been opened. Happy Reading!")

    def wolf_alpha(self, counter, command):
        app_id = "Your APP ID"
        client = wolframalpha.Client(app_id)
        if counter == 1:
            self.say("I can try and answer computational and geographical questions.")
            self.say("What is your Question?")
            command = self.take_command()
        result = client.query(command)
        answer = next(result.results).text
        print(f"\n{answer}")
        self.say(answer)

    def block_website(self):
        self.say("Enter the website that you want to block.")
        website_name = input("Enter the website")
        self.say("Adding the site to block list.")
        with open("temp/blocked_list.txt") as file:
            file.write(website_name + "\n")
            file.close()
        blocker = block_unblock_website(website_name)
        blocker.block_websites()
        self.say("The Website has been successfully blocked")

    def unblock_website(self):
        self.say("Which website do you want to unblock?")
        if not os.path.exists("temp/blocked_list.txt"):
            pass
        else:
            with open("temp/blocked_list.txt") as file:
                content = file.readlines()
            print("\nList of Blocked Websites: \n")
            for line in content:
                print(line)
        website_name = input("Enter the site: ")
        unblocker = block_unblock_website(website_name)
        unblocker.unblock_websites()
        self.say("The Website has been successfully unblocked")

    def web_search(self, command):
        self.clean_command(command)
        self.say("Searching on google")
        webbrowser.open_new_tab(f"https://www.google.com/search?q={command}")
        sleep(1)
        self.say("The result has been displayed on the screen")

    def typing_speed(self):
        self.say("Directing you to the Website where you can test your typing Speed")
        sleep(0.1)
        webbrowser.open_new_tab("https://www.typing.com/student/typing-test/1-minute")
        self.say("One Minute test has been automatically selected, you can change the duration of the test if you want")
        self.say("Good Luck!")

    def open_site(self, statement):
        statement = self.clean_command(statement)
        self.say(f"Opening {statement} on the browser!")
        results = []
        for j in search(statement, num=10, stop=10, pause=2):
            results.append(j)
        webbrowser.open_new_tab(results[0])

    def take_screenshot(self):
        filename = "Screenshot.png"
        i = 0
        while True:
            if os.path.exists(os.path.join(self.desktop_path, filename)):
                filename = f"Screenshot_{i}.png"
                i += 1
            else:
                break
        pyautogui.screenshot(os.path.join(self.desktop_path, filename))
        self.say("Screenshot has been taken, and saved to the Desktop!")

    def take_picture(self):
        filename = "Picture.jpg"
        i = 0
        while True:
            if os.path.exists(os.path.join(self.desktop_path, filename)):
                filename = f"Picture{i}.jpg"
                i += 1
            else:
                break
        cam = cv2.VideoCapture(0)
        s, img = cam.read()
        cam.release()
        if s:
            cv2.imwrite(os.path.join(self.desktop_path, filename), img)
        self.say("Picture has been taken, and saved to the Desktop!")

    def operations(self):
        self.banner()
        command = self.take_command()
        if command is None:
            pass
        elif len(command) == 0:
            pass
        elif f"hey {self.wake_word}" in command or f"hi {self.wake_word}" in command:
            playsound.playsound("Utilities/Initial_Audio.mp3")
            self.say("Yes?")
            command = self.take_command()
            if command is None:
                pass
            elif len(command) == 0:
                pass
            elif "close the program" in command or "exit" in command:
                self.exiting()
            elif "what are you doing" in command:
                self.say("Waiting for your commands!")
            elif "how are you" in command:
                self.say(f"I'm Fine {self.username}, how are you!")
            elif "nothing" in command:
                pass
            elif "fuck you" in command:
                self.say("Same to you!")
            elif "i love you" in command:
                self.say("I love you too.")
            elif "i am fine" in command or "i am good" in command or "i am great" in command:
                self.say("Good to hear that")
            elif "thank you" in command or "thanks" in command:
                self.say("Happy to help")
            elif "search" in command or 'look' in command:
                if "wikipedia" in command:
                    self.wikipedia(statement=command)
                else:
                    self.web_search(command)
            elif 'screenshot' in command:
                self.take_screenshot()
            elif "download" in command and 'youtube' in command:
                self.download_yt_video()
            elif "open" in command:
                if "youtube" in command:
                    self.youtube()
                elif "google" in command:
                    self.google()
                elif "gmail" in command:
                    self.gmail()
                elif "facebook" in command:
                    self.facebook()
                elif "instagram" in command:
                    self.instagram()
                elif "website" in command:
                    self.open_site(command)
                elif "Desktop" in command:
                    os.system(f"open {self.desktop_path}")
                elif "Download" in command or "Downloads" in command:
                    os.system(f"open {self.desktop_path.replace('Desktop', 'Downloads')}")
                elif not self.open_app(command):
                    self.web_search(command)
            elif "play" in command and "on youtube" in command:
                self.play_yt(command, 1)
            elif command == "what's the time" or command == "what is the time" or command == "tell me the time" \
                    or command == "can you tell me the time":
                self.tell_time()
            elif "top headlines" in command or "latest news" in command:
                self.news()
            elif 'take' in command and 'picture' in command:
                self.say("Capturing an Image from the Webcam!")
                self.take_picture()
            elif "maths" in command or "geographical" in command or "science" in command:
                self.wolf_alpha(1, None)
            elif "distance" in command and "between" in command:
                self.wolf_alpha(0, command)
            elif "convert" in command and "image" in command and "sketch" in command:
                self.convert_to_sketch()
            elif "hand" in command and "cricket" in command:
                self.hand_cricket()
            elif "guessing" in command or "game" in command:
                self.guessing_game()
            elif "generate" in command and "password" in command:
                self.generate_password()
            elif 'temporary files' in command or "temporary file" in command or "temp files" in command:
                self.clear_cache()
            elif "internet" in command and "speed" in command:
                self.internet_speed()
            elif "convert" and "audio" in command or "extract" and "audio" in command:
                self.convert_to_audio()
            elif 'weather' in command or 'weather conditions' in command or 'weather report' in command \
                    or "weather like" in command:
                self.weather()
            elif "shutdown" in command or "log off" in command or "turn off" in command:
                if self.admin:
                    self.shutdown_restart(0)
                else:
                    self.say("Not enough privileges to perform this operation.")
            elif "reboot" in command or "restart" in command:
                if self.admin:
                    self.shutdown_restart(1)
                else:
                    self.say("Not enough privileges to perform this operation.")
            elif "what is the" in command and "meaning of" in command:
                self.meaning(command)
            elif "meaning of" in command:
                self.meaning(command)
            elif "what does" in command and "mean" in command:
                self.meaning(command)
            elif "convert" in command and "pdf" in command:
                self.pdf_convert()
            elif "edit pdf" in command or "edit a pdf" in command:
                self.edit_pdf()
            elif "tell" in command and "joke" in command:
                self.tell_joke()
            elif "create" in command and "folder" in command:
                self.create_folder(command)
            elif "typing" in command and "speed" in command:
                self.typing_speed()
            elif command.startswith("who") or command.startswith("when") or command.startswith("where") \
                    or command.startswith("how") or command.startswith("what") or command.startswith("why"):
                self.web_search(command)
            elif "qr code" in command:
                if "generate" in command or "create" in command or "make" in command:
                    self.make_qr(1)
                elif "read" in command or "scan" in command:
                    self.make_qr(0)
                else:
                    self.web_search(command)
            elif "copy" in command and "image" in command:
                self.extract_text()
            elif "block" in command and "website" in command:
                if self.admin:
                    self.block_website()
                else:
                    self.say("You don't have enough privileges to Run this command. ")
            elif "unblock" in command and "website" in command:
                if self.admin:
                    self.unblock_website()
                else:
                    self.say("You don't have enough privileges to Run this command. ")
            else:
                print(f"\n{command}\n")
                self.say("Do you want me to search for this on google?")
                user_option = self.take_command()
                if user_option is None:
                    pass
                elif 'yes' in user_option or "sure" in user_option:
                    self.web_search(command)
                elif "no" in user_option or "nahi" in user_option:
                    self.say("Okay")
        else:
            pass


if __name__ == "__main__":
    siri = Assistant()
    siri.get_user_info()
    siri.banner()
    siri.greet_user()
    while True:
        siri.operations()
        siri.banner()
