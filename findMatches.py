def findMatches(word, words):
    matches = []
    yes = True
    wd = set(word)
    for w in words:
        if set(w).issubset(wd) and w != word:
            for i in wd:
                if w.count(i) > word.count(i):
                    yes = False
                    break
            if yes:
                matches.append(w)
            yes = True
    return matches
