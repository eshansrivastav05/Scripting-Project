The program searches a term entered by the user using the Google Search API and finds the corresponding wikipedia page (if there is one) within the first 10 links.
The wikipedia page will be scraped for all the text in the HTML paragraph tags
A file will be created and the wikipedia page text will be stored within it.
A new API call is made to a Summarization LLM API to which the page text is uploaded
The text within the file will be summarized and then returned to the user
