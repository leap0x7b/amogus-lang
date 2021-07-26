import argparse

parser = argparse.ArgumentParser(prog='amogus', description='A very sussy esoteric language')
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
    elif j == "us":
        value = 0
