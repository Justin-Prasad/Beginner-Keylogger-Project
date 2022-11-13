# Beginner-Keylogger-Project
This project showcases the pynput API and its uses in the realm of cybersecurity in the form of a keystroke monitor

Given my general interest in cybersecurity, I felt this project was a good way to learn more and showcase what I have learned in a controlled environment. While this project may seem fairly rudimentary, it serves as a very nice stepping stone into developing more utilitarian-natured projects with applications in cybersecurity. 

**Disclaimer: I do not condone the use of malicious software in an illegal manner to obtain data. This project is purely for learning and exploring a general interest in cybersecurity and should not be taken out of context as anything more.**

# Overview #
This function of this project is pretty much given away in the title. It's really only meant to record the key strokes/inputs of the user in a text file that will be created as the code runs. It also has a terminal output given by the ```print(str(key))``` line.

# Now a brief demo:
Let's say a I had this running in the background for some unknown reason. Perhaps it was to test it. Now, the pynput API will recognize inputs from the keyboard no matter where you are typing. It can be in google, it can be in a login website, or any other text field. For the purposes of this demo, I will assume the role of someone typing "How to cook instant ramen" into a google text field.  

![image](https://user-images.githubusercontent.com/101998961/201499069-d255113e-4088-4d8d-bc1c-8a613c3f0e84.png)

The way that the code works is that when it is running, it essentially logs the inputs from the keyboard through the python pynput API and it prints it to the terminal, and as well as that, upon the first key, a new text file is created by the name of "log.txt" and the contents are stored there as well. This will be shown below. 

This is what the terminal output looks like:

![image](https://user-images.githubusercontent.com/101998961/201499203-6fd71648-dd98-41bc-af11-6cf9226e43b9.png)

As a disclaimer, the error messages are messages being printed from some exception handling I added for keys that aren't members of the alphabet. This includes keys such as ```shift```, ```space```, and ```delete```. 

This is what the newly created log.txt file looks like:

![image](https://user-images.githubusercontent.com/101998961/201499285-c8579261-37d9-42c2-81db-fcdb23521c29.png)

As mentioned before, I added exception handling to handle printing spaces and things of the sort, and so it won't show up as such in the text file. 

If one so wants to, they could potentially leave the program running, and in doing so any and all keystrokes are added to the ```log.txt``` file.

# Applications in the real world
It doesn't take a genius to see to see what the biggest application of this program is. Keyloggers are an incredibly powerful tool for reconnaisance if the user has no idea they even downloaded it in the first place. They're essentially giving someone their information without even knowing it! While I do find these applications interesting in a purely conceptual manner, **I do not condone the malicious use of such software and urge others to be careful of such software as well.**  
