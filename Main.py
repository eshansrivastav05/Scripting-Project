import GoogleSearch
import TextExtractor
import Store
import API

if __name__ == "__main__":
    while True:

        try:

            link = (GoogleSearch.run())
            content = TextExtractor.extractText(link)

            userFile = input("Enter the name of your file: ")
            fileName = Store.fileNamer(userFile)
            file = Store.fileCreator(fileName, content)

            API.summarizer(fileName)
        
        except Exception as e:

            print('An error occured')
            print(e)
        
        while True:

            userDecision = input("Would you like to try again? (y/n): ").lower()

            if userDecision=='y':

                break

            elif userDecision == 'n':

                break

            else:

                print('Try Again')
        
        if userDecision == 'y':

            continue

        else:

            break