import webbrowser as browser
import urllib.request as urll
import json
from pprint import  pprint

def openBrowser(id):
    url ="https://en.m.wikipedia.org/wiki?curid="
    browser.open(url+str(id))

def random_art():
    response=urll.urlopen(" https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=5&format=json ")
    jsondata = response.read()
    data = json.loads(jsondata.decode("utf-8"))
    return (data)

def  red_art():
    data=random_art()
    print(data["query"]["random"])


    while(True):
        print("Enter a value to read the article")
        count=0
        art=[]
        for i in data["query"]["random"]:
            count+=1
            art.append(i["id"])
            print(count," - ",i["title"])
        option = input("option: ")

        if(option):
            try:
                option=int(option)

            except ValueError as e:
                print("enter a valide value")

        print("your option: ",option)
        if(option==0):
            break
        elif(option==1):
            openBrowser(art[0])
        elif(option==2):
             openBrowser(art[1])
        elif(option==3):
             openBrowser(art[2])
        elif(option==4):
            openBrowser(art[3])
        elif(option==5):
            openBrowser(art[4])

while(True):
    print("Welcome to Wiki random Article")
    print("Enter your option")
    print("1 - Load random article")
    #print("2 - Read article")
    print("0 - exit the program")
    opt= input("option: ")


    try:
        opt=int(opt)

        print("your option: ",opt)
    except ValueError as e:
        print("enter a valide value")

    if(opt==0):
        print("Program exited")
        break
    elif(opt==1):
        red_art()