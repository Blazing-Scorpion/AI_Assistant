import cv2
import os
import speedtest
from PIL import Image
import pytesseract
import random2
import array
import pyperclip
import moviepy.editor as mp
import platform
import qrcode
import requests
from pytube import YouTube
from pytube.cli import on_progress
import time


class YT_Downloader:

    def __init__(self, link):
        self.link = link
        self.yt = YouTube(self.link, on_progress_callback=on_progress)

    def display_video_information(self):
        print("\nBelow are the information about the Video.\n")
        print("Title: " + self.yt.title + "\n")
        print("Length of the Video: " + str(self.yt.length) + " Seconds \n")
        time.sleep(1)

    def get_video(self):
        if platform.system() != "Windows":
            home = os.path.expanduser("~")
        else:
            home = os.environ['USERPROFILE']
        download_path = os.path.join(home, "Downloads")
        ys = self.yt.streams.get_highest_resolution()
        ys.download(download_path)
        print("\n\n\t\t...................................ENJOY!!.....................................\n\n")


class weather:

    def __init__(self, city_name):
        self.city_name = city_name
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        self.API_KEY = "Your API Key"

    def get_report(self):
        URL = self.BASE_URL + "q=" + self.city_name + "&appid=" + self.API_KEY
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            temp_feel_like = main['feels_like']
            humidity = main['humidity']
            pressure = main['pressure']
            weather_report = data['weather']
            wind_report = data['wind']

            print(f"{self.city_name:-^35}")
            print(f"Temperature: {temperature} K")
            print(f"Feel Like: {temp_feel_like} K")
            print(f"Humidity: {humidity} %")
            print(f"Pressure: {pressure} hPa")
            print(f"Weather Report: {weather_report[0]['description']}")
            print(f"Wind Speed: {wind_report['speed']} m/s")
            print(f"Time Zone: {data['timezone']}")
            return temperature, humidity, wind_report['speed']
        else:
            print("Error in the HTTP request")


class video_2_audio:

    def __init__(self, path):
        self.video_path = path

    def convert(self):
        clip = mp.VideoFileClip(r"{}".format(self.video_path))
        filename = os.path.basename(self.video_path)
        if str(platform.system()) == "Windows":
            download_folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/')
        else:
            download_folder = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/')
        output_filename = os.path.splitext(filename)
        final_output_filename = download_folder + output_filename[0] + ".mp3"
        clip.audio.write_audiofile(r"{}".format(final_output_filename))


class Password:

    def __init__(self, length):
        self.max_length = length
        self.DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.UPCASE_CHARACTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                                  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        self.LOWCASE_CHARACTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                                   "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        self.SYMBOLS = ['@', '#', '$', '%', '=', '<', '>', ':', '~', '.', '*', '(', ')', '/', '|', '?']

    def generate(self):

        COMBINED_LIST = self.DIGITS + self.LOWCASE_CHARACTERS + self.UPCASE_CHARACTERS + self.SYMBOLS

        rand_digit = random2.choice(self.DIGITS)
        rand_upper = random2.choice(self.UPCASE_CHARACTERS)
        rand_lower = random2.choice(self.LOWCASE_CHARACTERS)
        rand_symbol = random2.choice(self.SYMBOLS)
        temp_pass = rand_symbol + rand_lower + rand_upper + rand_digit

        for x in range(self.max_length - 4):
            temp_pass = temp_pass + random2.choice(COMBINED_LIST)

        temp_pass_list = array.array('u', temp_pass)
        random2.shuffle(temp_pass_list)

        password = ""

        for x in temp_pass_list:
            password = password + x

        print("")
        print("The new Generated Password is: " + password)
        print("")
        pyperclip.copy(password)
        print("........................Done...........................")


class QR_Code:

    @staticmethod
    def qr_gen(text):
        qr = qrcode.QRCode()
        qr.add_data(text)
        qr.make()
        img = qr.make_image()
        filename = "QR_Code.png"
        i = 1
        while True:
            if os.path.exists(os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'), filename)):
                filename = f"QR_Code_{i}.png"
                i += 1
            else:
                break
        if str(platform.system()) == "Windows":
            result_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            result_path = os.path.join(result_path, filename)
        else:
            result_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
            result_path = os.path.join(result_path, filename)
        img.save(result_path)
        img.show()

    @staticmethod
    def qr_detect(query_1):
        d = cv2.QRCodeDetector()
        val, points, straight_qr = d.detectAndDecode(cv2.imread(query_1))
        print("\n\nThe Extracted Text of the QR Code is: ", val + '\n')
        pyperclip.copy(val)


class Test_Speed:

    def __init__(self):
        self.test = speedtest.Speedtest()

    @staticmethod
    def convert_to_Mbps(number):
        converted = number / 1024 / 1024
        return float(converted)

    def start_test(self):
        print("Loading the Available Servers: \n")
        self.test.get_servers()
        print("Choosing the Appropriate Server: \n")
        best_server = self.test.get_best_server()
        print(f"Chose {best_server} for testing the Speed!\n")
        ping = self.test.results.ping
        print(ping)
        print("Testing the Download Speed...\n")
        download = self.test.download()
        print(f"{round(self.convert_to_Mbps(download), 2)} Mbps")
        print("Testing the Upload Speed...\n")
        upload_speed = self.test.upload()
        print(f"{round(self.convert_to_Mbps(upload_speed), 2)} Mbps")


class extract_text:

    def __init__(self, path):
        self.path = path
        self.output = None

    def final_paths(self):
        filename, extension = os.path.splitext(self.path)
        self.output = f"{filename}_data.txt"

    def write_to_file(self, text):
        text_file = open(f"{self.output}", "w")
        text_file.write(text)
        text_file.close()

    def get_data(self):
        text = pytesseract.image_to_string(Image.open(self.path))
        self.final_paths()
        self.write_to_file(text)


class convert:

    def __init__(self, path):
        self.img_path = path

    def conversion(self):
        img = cv2.imread(self.img_path)
        grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        invert_img = cv2.bitwise_not(grey_img)
        blur_img = cv2.GaussianBlur(invert_img, (111, 111), 0)
        invblur_img = cv2.bitwise_not(blur_img)
        sketch_img = cv2.divide(grey_img, invblur_img, scale=256.0)
        output_Filename = os.path.splitext(self.img_path)
        final_output_Filename = output_Filename[0] + "_Converted" + output_Filename[1]
        cv2.imwrite(final_output_Filename, sketch_img)
        cv2.destroyAllWindows()


class block_unblock_website:

    def __init__(self, website):
        self.website = website
        if not self.website.startswith("https://") and not self.website.startswith("www."):
            self.website = "www." + self.website
        self.redirect = "127.0.0.1"
        if platform.system() == "Windows":
            self.host_path = "C:\Windows\System32\drivers\etc\hosts"
        else:
            self.host_path = "/etc/hosts"

    def block_websites(self):
        with open(self.host_path, 'r+') as file:
            content = file.read()
            if self.website.startswith("https://"):
                temp_website = self.website.replace("https://", "")
            else:
                temp_website = "https://" + self.website
            if self.website in content:
                pass
            else:
                file.write("\n" + self.redirect + " " + self.website + "\n")
            if temp_website in content:
                pass
            else:
                file.write("\n" + self.redirect + " " + temp_website + "\n")

    def unblock_websites(self):
        with open(self.host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not self.website:
                    file.write(line)
            file.truncate()
