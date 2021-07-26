import sys, builtins
def input(prompt=None):
    if prompt:
        sys.stderr.write(str(prompt))
    return builtins.input()

text = input("Input text to be converted to Amogus esolang: ")
for i in range(len(text)):
    for l in range(ord(text[i])):
        print("amogus", end=" ")
    print("among us", end=" ")
