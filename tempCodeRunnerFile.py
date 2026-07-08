with open("sample.txt") as f:
    words=sum(len(line.split()) for line in f)
print(words)