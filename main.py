import os
import fnmatch

filePath = input("Path: ")
searching_word = input("word: ")
matched_index = []
counter = 0
searching_word = searching_word.lower()
for root, dirs, files in os.walk(filePath):
    for filename in fnmatch.filter(files, "*.txt"):
        source = (os.path.join(root, filename))
        print(source)
        with open(source, "rb") as f:
            read = f.read()
            list_1 = list(read.split())
            # searching_word = searching_word.lower()
            for word in list_1:
                if word == searching_word:
                    matched_index.append(counter)
                    counter += 1
            if searching_word not in list_1:
                print(f"Couldn't found  '{searching_word}' from '{filename}'  ")
                break
            else:
                print(matched_index)

# C:\Users\bekab\Desktop
