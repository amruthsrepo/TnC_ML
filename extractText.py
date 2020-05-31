import nltk
from newspaper import Article

url = 'https://en.wikipedia.org/wiki/Terms_of_service'
# url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)
article.download()
article.parse()
article.nlp()
print(article.text)
print('Summary: \n\n')
print(article.summary)