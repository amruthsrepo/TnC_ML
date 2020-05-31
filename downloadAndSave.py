from googlesearch import search
from newspaper import fulltext
from newspaper import Article
from tld import get_tld
import re

query = '"terms and conditions" "terms of service" -template, -sample, -what, -pdf inurl:term'
loaded = failed = 0
startFrom = 471
for i in range(10):
    searchResults = search(query, tld="com", num=100, start=((i*100) + 1), pause=5)
    for j in searchResults:
        print(j)
        url = j
        article = Article(url)
        article.download()
        try:
            fullText = re.sub('\n+','\n',(fulltext(article.html) + '\n' + url))
        except:
            failed += 1
            print(f'Failed {failed} \t Total: {failed+loaded}')
            continue
        parsedName = get_tld(url,as_object=True)
        domain = parsedName.fld.replace('.','_')
        with open(("/Users/amruthnag/Documents/VS Python/Text extraction/download1/"+ domain +".txt"),"w") as openFile:
            openFile.write(fullText)
            loaded += 1
            print(f'Loaded {loaded} \t Total: {failed+loaded}')
        with open('/Users/amruthnag/Documents/VS Python/Text extraction/loaded URLs.txt', 'a') as urlFile:
            urlFile.write('\n' + url)
print(f"\n\n\nTotal loaded: {loaded} \t Total failed: {failed}")
