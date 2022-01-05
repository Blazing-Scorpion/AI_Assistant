# AI_Assistant


This is a Python based Voice Assistant. This was programmed to increase my understanding of python and also how the in-general Voice Assistants work.

  
                                                     AI_Assistant

                                                    version 0.0.0


Hello Guys!!


This is a cross-platform program, however "THIS PROGRAM IS CURRENTLY DEVELOPED TO WORK ONLY FOR WINDOWS AND macOS 
AND NOT FOR ANY LINUX DISTROS."

Before starting to tell you about my Assistant, I would quickly like to go over some IMPORTANT POINTS which I think
every user should know. This would avoid the users from encountering any errors, and if they do, they would know where 
the problem is.

* Firstly, install all the required packages to ensure smooth functioning of the entire program and its utilities. This
  program has several dependencies, which can be seen in the requirements.txt
	
	* You can do install the program's dependencies by "pip install -r requirements.txt". You can use pip or pip3,
 	  doesn't matter. The command is the same for both platforms (Windows or macOS).

	* Run this command in the "AI_Assistant" directory in the command prompt to avoid FileNotFound Error.

	* Wait for the packages to get installed and if there is any error in the installation of the package, you can
	  either google or raise a query.
  
* This program uses the populer pyttsx3 for text to speech conversion. I have set the Voice ID of the assistant
  in accordance to the voices available on my personal computer. However the "id" may vary on your computer, which
  is why I have programmed "Try_Voices.py" with which you can try each and every voice available on your device. Usage has
  been demonstrated below:

	1) Find the "Try_Voices.py" file in the Installer folder.
	2) Run this program with "python Try_Voices.py" on Windows and "python3 Try_Voices.py" on macOS.
	3) This is used to speak out the Pre-Determined Line in all the available voices.
	4) You can see the voice id and its index (which will be used in the main program).
	5) Note the index of the voice you like and replace that in "line 17"
		"self.engine.setProperty('voice', voices[3].id)" 
	   Change the "3" to the index of your choice of voice.

    In-Case you don't like the voices available on your device, you can add more. Visit the below-mentioned link to get
    to know the step-by-step process of the same.

    "https://puneet166.medium.com/how-to-added-more-speakers-and-voices-in-pyttsx3-offline-text-to-speech-812c83d14c13"

    Finally, I'm providing a link to an article where you can better understand the use and initial setup of pyttsx3.

    https://betterprogramming.pub/an-introduction-to-pyttsx3-a-text-to-speech-converter-for-python-4a7e1ce825c3

* Although this program uses the offline google speech recognition, it requires an Active Internet Connection for various 
  features at all times so that the program can work smoothly.

* If you want to change the initiating audio, then you can either add the audio file to the "Utilities" folder and rename it to 
  "Initial_Audio.mp3" or you can edit the "Asssistant.py" at line 624: playsound.playsound("location of the audio file").

* There are a few features like weather report and wolframalpha which requires personal API keys. You need to visit these sites,
  and get your own API key from these websites, and then replace them in the source files.

	Use any text editor or IDE of your choice.	

	* Edit the "src/Tools.py" file
	
		line 46: self.API_KEY = "Your API Key"
	
	* Edit the "Assistant.py" file

		line 529: app_id = "Your APP ID" 

	Not performing this step would not cause problem in the running of the Assistant but will return an error when the
    user tries to use any of the feature requiring an online API key.

* Lastly, there are some features like blocking a website, shutting down and restarting the device which can only be
  performed when the program is run with elevated privileges.

With this out of the way, let me tell you about some features of the program. I have tried to add all the basic
functions in this program and all the features can be seen in the main screen of the program at all times.

This program can perform the following functions:

              * Interact to some extent					  * Can open websites
              * Open gmail, google search and YouTube			  * Autoplay song on YouTube using Keyword
              * Download Youtube Video with Keyword or Video link	  * Hand-Cricket Game
              * Number Guessing Game					  * Can Shut down and Restart The Device
              * Can Clear Temporary Files				  * Generate QR Code
              * Can help in Converting and Editing a PDF		  * Extract Text from an Image
              * Tell a Joke						  * It can open Instagram and Facebook
              * Tell about the Weather of any place			  * Generate a Password
              * Tell Time						  * Open TOI for top Headlines
              * Take Screenshot						  * Capture a Picture from the Webcam
              * Can redirect you to the Typing Speed Website		  * Test your Internet Speed
              * Tell you the meaning					  * Block / Unblock Websites

As you can see from the features above, this program is equipped with several features to provide convenience to the
users. It can open any website from its name, can try to communicate upto a certain limit and help you with basic problems.

One drawback which I feel is that the speechrecognition package takes the input after 4-5 Seconds of delay, so please
be sure that the program is listening to the command when you are speaking.



For any suggestion, bugs or improvements, please feel me mail me at "BlAzInGScOrPiOn_06@protonmail.com" or feel free to comment below.
