from collections import Counter

def wordScore (word, freq) -> int:
    score = 0
    for letter in set(word):
        score += freq[letter]
    return score

def bestGuess(goodLetters, badLetters):
    wordList = {"added", 
            "agent", 
            "alpha", 
            "asset", 
            "audit", 
            "basis", 
            "board", 
            "bonus", 
            "brand", 
            "check", 
            "close", 
            "count", 
            "cover", 
            "curve", 
            "cycle", 
            "debit", 
            "delta", 
            "draft", 
            "entry", 
            "equal", 
            "error", 
            "files", 
            "first", 
            "flows", 
            "funds", 
            "gross", 
            "hedge", 
            "index", 
            "issue", 
            "labor", 
            "limit", 
            "loans", 
            "model", 
            "money", 
            "offer", 
            "order", 
            "point", 
            "price", 
            "rates", 
            "ratio", 
            "risks", 
            "right", 
            "round", 
            "sales", 
            "scale", 
            "scope", 
            "share", 
            "sheet", 
            "shock", 
            "stock", 
            "swaps", 
            "taxes", 
            "terms", 
            "trade", 
            "trust", 
            "value", 
            "vests", 
            "yield"}
    out = "".join(wordList)
    store = Counter(out)

    badLettersArray = list(badLetters)
    goodLettersArray = list(goodLetters)

    badFlag = 0

    res = {}

    for i in wordList:
        badFlag = 0
        while badFlag == 0:
            for goodLetter in goodLettersArray:
                if goodLetter not in i:
                    badFlag = 1
            for badLetter in badLettersArray:
                if badLetter in i:
                    badFlag = 1
            if badFlag == 0:
                badFlag = 1
                res[i] = wordScore(i,store)
    res = dict(sorted(res.items(),key=lambda item:item[1], reverse=True))
    for key in res:
        print(f'{key} - Score: {res[key]}')
bestGuess("","")