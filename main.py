import argparse

parser = argparse.ArgumentParser(description='Very sussy esoteric language')
parser.add_argument('file', type=str, nargs=1,
                    help='a sussy file to be decoded into amogus language')
args = parser.parse_args()

value = 0
code = open(args.file[0], "r").read()

lexed = []
for i in code.split():
    lexed.append(i)

for j in lexed:
    if j == "amogus":
        value += 1
    elif j == "sus":
        value -= 1
    elif j == "among":
        print(chr(value), end="")
        value = 0
    elif j == "us":
        quit()
    elif j == "sussy":
        print(code)    
