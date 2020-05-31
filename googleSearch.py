from googlesearch import search
from datetime import datetime
import time

query = '"terms and conditions" "terms of service" -template, -sample, -what, -pdf inurl:term'
loaded = failed = 0
removeWordList = ['news', 'insurance']
ts = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

with open('/Users/amruthnag/Documents/VS Python/Text extraction/Loaded urls/'+ts+'.txt', 'a') as urlFile:
    for i in range(1,10,1):
        searchResults = search(query, tld="com", num=100, start=((i*100) + 1), pause=30)
        print((i*100) + 1)
        for j in searchResults:
            print(j)
            linkLower = j.strip().lower()
            if not any(word in linkLower for word in removeWordList):
                urlFile.write('\n' + j)
