
from googlesearch import search

def googleSearch(queryTerm):

    searchItems = []
    #Looks for top 10 dot com links and pauses for 5 seconds between links to prevent HTTPS error
    for result in search(query = queryTerm, tld="com", num=10, lang = "en", start=0, stop=10, pause = 5):

        searchItems.append(result)
    
    return(searchItems)

def findWikiLink(urls): #Searches for wikipedia link

    for url in urls:

        if "wikipedia" in url.lower():

            return str(url)
        
        else:

            pass

def run():
    
    userQuery = input("Enter search term: ")
    searchResults = googleSearch(userQuery)
    link = findWikiLink(searchResults)

    return link

if __name__ == "__main__":
    
    run()