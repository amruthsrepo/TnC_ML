import glob

fullSet = set()
removeWordList = ['news', 'insurance']
for filePath in glob.iglob('/Users/amruthnag/Documents/VS Python/Text extraction/Loaded urls/*'):
    with open(filePath,'r') as openFile:
        urlList = openFile.read().split('\n')
        # print({i:urlList.count(i) for i in urlList})
        for link in urlList:
            linkLower = link.strip().lower()
            if not any(word in linkLower for word in removeWordList) and link is not '':
                fullSet.add(link)
print(len(fullSet))
with open('/Users/amruthnag/Documents/VS Python/Text extraction/Loaded urls/urlMaster.txt', 'w') as masterFile:
    listAsStr = repr(list(fullSet))
    masterFile.write(listAsStr[1:-1].replace(', ', '\n').replace("'",""))