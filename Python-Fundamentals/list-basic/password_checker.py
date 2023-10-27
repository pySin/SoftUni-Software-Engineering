# Password Checker


import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

pwd = pyautogui.password("Enter your password: ")

sample_pwd = ""

while sample_pwd != pwd:
    sample_pwd = [random.choice(chars) for _ in range(len(pwd))]  # Generate a list of random characters

    print("<====" + "".join(sample_pwd) + "====>")

    if sample_pwd == list(pwd):
        print("The Password is: " + "".join(sample_pwd))
        break
