
from collections import Counter
with open("/home/dhanuka/research/python/data.txt", "rt", encoding="utf-8-sig") as file:  # with can auto close the file
    wordcount = Counter(file.read().split())

for k, v in wordcount.most_common(len(wordcount)):
    print(k, v)