import os, platform

def cleans():
    if platform.system()=="Darwin":
        os.system("clear")
    elif platform.system()=="Linux":
        os.system("clear")
    elif platform.system()=="Windows":
        os.system("cls")
cleans()