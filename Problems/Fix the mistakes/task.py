words = input().split()
for word in words:
    if word.casefold().startswith(('www.', 'https://', 'http://')):
        print(word)
