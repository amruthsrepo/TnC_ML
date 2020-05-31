    # extractorFull = Extractor(extractor='DefaultExtractor', url=url).getText()
    # extractorScentences = Extractor(extractor='ArticleSentencesExtractor', url=url).getText().split('\n')
    # numSentences = len(extractorScentences)
    # i = 1
    # iPrev = 0
    # while i < numSentences:
    #     len2Search = len(extractorScentences[iPrev])
    #     len2Search = len2Search if (len2Search<30) else 30
    #     res = re.search(f"({extractorScentences[iPrev][-len2Search:].replace(')','').replace('(','')})(.|\n)*({extractorScentences[i]})",extractorFull)
    #     if res is not None and len(extractorFull[res.regs[1][1]:res.regs[2][0]].strip()) is not 0:
    #         extractorScentences.insert(i,('->' + extractorFull[res.regs[1][1]:res.regs[2][0]].strip().replace('\n','\n->')))
    #         iPrev += 2
    #         i += 2
    #         numSentences += 1
    #     else:
    #         iPrev += 1
    #         i += 1