import os

def amt(txt, n, symbol):
    pcount = 0
    ch = txt[n]
    while(ch == symbol):
        n+=1
        ch = txt[n]
        pcount+=1
    return n-1, pcount

def main():
    code = open("mdset.bf", "r").read()
    with open("out.cpp", "w") as file:
        file.write("#include <iostream>\n")
        file.write("int main(){\n")
        file.write("char mem[30000];\n")
        file.write("int pointer = 0;\n")
        i = 0
        while i < len(code):
            ch = code[i]
            match ch:
                case "+":
                    i, pcount = amt(code, i, "+")
                    file.write(f"mem[pointer]+={pcount};\n")
                case "-":
                    i, pcount = amt(code, i, "-")
                    file.write(f"mem[pointer]-={pcount};\n")
                case ">":
                    i, pcount = amt(code, i, ">")
                    file.write(f"pointer+={pcount};\n")
                case "<":
                    i, pcount = amt(code, i, "<")
                    file.write(f"pointer-={pcount};\n")
                case ".":
                    file.write("std::cout << (char) mem[pointer];\n")
                case ",":
                    file.write("mem[pointer] << std::cin;\n")
                case "[":
                    file.write("while (mem[pointer]){\n")
                case "]":
                    file.write("}\n")
                case _:
                    pass
            i+=1
        file.write("}")


    #os.system("g++ -o out.exe out.cpp")
    #os.system("out.exe")

if __name__ == "__main__":
    main()
