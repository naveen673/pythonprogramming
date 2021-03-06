
"""
Write a function that takes a list of strings and prints them, one per line, in a rectangular frame. For example, the list ["Hello", "World", "in", "a", "frame"] gets printed as:
"""

p = input("words?")

def frame(words):
    size = len(max(words, key=len))
    print('*' * (size + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))

frame(p.split(" "))

