import nlpcloud #Summarization api
import time

def summarizer(textFile):

    client = nlpcloud.Client("bart-large-cnn", "<api key>", gpu=True) #Calls summarization model

    fileObject = open(textFile, 'r', encoding="utf-8") #Opens file that holds full text

    for line in fileObject: #Iterates through each line and summarizes it

        print(client.summarization(line)) #Prints the summarized text to terminal

        time.sleep(1) #Sleep prevents overloading model