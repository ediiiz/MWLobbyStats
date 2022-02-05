import pandas as pd
from urllib import request
import re
import json

usernamesCheck=[]
usernames=[]
kd_ratios=[]
accuracys=[]

def getPlayerData (username): #Continue if player is already in list
    if username not in usernamesCheck:
        for x in range(2):
            platform = console(x)
            #print(platform)
            buildUrl = "http://dreamteam.gg/cod/profile/" + platform + "/" + username
            print(buildUrl)
            url_requested = request.urlopen(buildUrl)
            if 200 == url_requested.code:
                html_content = str(url_requested.read())
                try:
                    filter(html_content, username) #implement trycatch
                except:
                    print("Player not available on " + platform)
    usernamesCheck.append(username)



def console(argument):
    switcher = {
        1: "psn",
        0: "xbl"
    }
    return switcher.get(argument, "Invalid platform")

def filter(html_content, username):
    result = re.search("\"general\"" + ":{\"accuracy" + "(.*),\"weekly\"", html_content)
    result = (result.group(1))
    result = "{\"accuracy" + result
    print(result)
    if username not in usernames:
        parse(result, username)

def parse(jsonstring, username):
    json_parsed = json.loads(jsonstring)
    usernames.append(username)
    kd_ratios.append(json_parsed["kd_ratio"])
    accuracys.append(json_parsed["accuracy"])
    #print(usernames)

def listToCSV():
    df = pd.DataFrame({'Name': usernames, 'KD': kd_ratios, 'Accu': accuracys})
    df.to_csv('Match.csv', index=False, encoding='utf-8')


#print(getPlayerData("Zack_7027"))
