import os
import sys
import time
import csv 
from selenium.webdriver.firefox.options import Options
from seleniumwire import webdriver as wd
import time
from fake_useragent import UserAgent
import random
from random import randint
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def configureProxy(cc):
    host = cc.lower() + '.smartproxy.com'
    port = word_finder(cc)
    options = {
    'proxy': {
        'http': 'http://azforia:azforia@' + host + ':' + port,
        'https': 'https://azforia:azforia@' + host + ':' + port,
        'no_proxy': 'localhost,127.0.0.1,dev_server:8080'
        }
    }

    firefox_options = wd.FirefoxOptions()
    firefox_options.add_argument('--headless')

    Options().headless = True
    browser = wd.Firefox(options=firefox_options, 
    seleniumwire_options=options)
    browser.set_window_position(0, 0)
    browser.set_window_size(1920, 1080)
    return browser

def word_finder(search_string):
    with open('proxylist.csv') as csv:
        for line in csv:
            tokens = line.strip().split(',')
            try:
                i = tokens.index(search_string)
                print(search_string)
                value = tokens[i+1]
                print(value)
            except (ValueError, IndexError):
                pass
        return value

def getdata(num,csvname,ord):

    with open('leads' + '/' + csvfolder + '/' + csvname + '.txt', 'r') as f:
      line = int(f.readlines()[-1])   
    print(line)
    with open("leads/" + num + '/' + csvname + ".csv", 'r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        first = mycsv[line][0]
        last = mycsv[line][1]
        email = mycsv[line][2]
        phone = mycsv[line][3]

        print(first)
    useragent = UserAgent()
    profile = wd.FirefoxProfile()
    profile.set_preference("general.useragent.override", useragent.random)

    browser = configureProxy(csvname)
    browser.get(ord)
    time.sleep(2)

    input_fname = browser.find_element_by_name("first_name")
    input_lname = browser.find_element_by_name("last_name")
    input_email = browser.find_element_by_name("email")
    input_num = browser.find_element_by_name("phone")
    input_submit = browser.find_element_by_name("submit")

    input_fname.send_keys(first)
    input_lname.send_keys(last)
    input_email.send_keys(email)
    input_num.send_keys(phone)
    print("form filled")
    time.sleep(2)
    with open('LEADS.txt', 'a') as f:
        f.write("\n")
        f.write(first + " " + last + " " + email + " " + phone + " " + str(line))
    with open('leads' + '/' + csvfolder + '/' + csvname + 'fb.txt', 'a') as f:
        f.write("\n")
        f.write(first + " " + last + " " + email + " " + phone + " " + str(line))
    with open('leads' + '/' + csvfolder + '/' + csvname + '.txt', 'a') as f:
        f.write("\n")
        f.write(str(line+1))

    input_submit.click()
    time.sleep(10)
    browser.close()

start=0
csvfolder = sys.argv[1]
geo = sys.argv[2].split()
trades = sys.argv[3].split()
#timing in minutes
timing = int(sys.argv[4])*5

links = []
for i in range(len(trades)):    
    links.append("https://pinppages.com/BitcoinERA/?campaigns=Trade" + trades[i] + "&api_key=rngz7pUg6X7dTCX&landings=BitcoinERA&product=")

for i in range(int(sys.argv[4])*len(links)):
    csvname = random.choice(geo)
    if not os.path.exists('leads' + '/' + csvfolder + '/' + csvname + '.txt'):
        with open('leads' + '/' + csvfolder + '/' + csvname + '.txt', 'a') as f:
                        f.write('0')
    print(links[start])
    getdata(csvfolder, csvname, links[start])
    if start < (len(links)-1):
        start = start+1
    elif start == (len(links)-1):
        start = 0
    time.sleep(randint(0.6*timing, timing))
    print(i)
