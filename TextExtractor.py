import requests
from bs4 import BeautifulSoup

def extractText(URL):

    contentList = []

    page = requests.get(URL, headers = {'User-agent': 'your bot 0.1'}) #Stores page data

    soup = BeautifulSoup(page.text, "html.parser") #Accesses HTML data

    tags = soup.find_all("p") #Finds all paragraph classes

    for tag in tags:
    
        contentList.append(tag.get_text()) #Stores all text in list
    
    return contentList