def count_words(text):
    counts = dict()
    words = text.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    counts_sort = sorted(counts.items())
    return counts_sort


example = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
print(count_words(example))  
