import sys

file = open(sys.argv[1], "r")
code = file.read()


out = ""

i = 0
chars = ",.+-[]<>"
indent = 0
while i < len(code):
    ch = code[i]
    if ch in chars:
        if ch not in "[]":
            out += ch
        else:
            if ch == "[":
                out += "\n" + "    " * indent + "[\n" + "    " * (indent + 1)
                indent += 1
            else:
                indent -= 1
                out += "\n" + "    " * indent + "]\n" + "    " * indent
    i += 1

file = open("mdset.bf", "w")
file.write(out)
