from collections import *
def word_count(file_name):
    with open(file_name) as a:
        return Counter(a.read().split())
print("Number of words in the given file are: ",word_count("content"))