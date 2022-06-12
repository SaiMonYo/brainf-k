def amt(txt, n, symbol):
    # outputs the outmout of "symbol" in a row
    pcount = 1
    n = n+1
    while(n < len(txt) and txt[n] == symbol):
        n+=1
        pcount+=1
    return n-1, pcount

def main(c):
    with open("t2.s", "w") as file:
        # write headers and initialise the 30000 memory locations
        file.write('''.data\n.text\n.global main\n\nmain:\n\tpushq   %rbp\n\tmovq    %rsp, %rbp\n\tsubq    $30016, %rsp\n\tmovq    $0, -30016(%rbp)\n\tmovq    $0, -30008(%rbp)\n\tleaq    -30000(%rbp), %rax\n\tmovl    $29984, %edx\n\tmovl    $0, %esi\n\tmovq    %rax, %rdi\n\tcall    memset\n\tleaq    -30016(%rbp), %rax\n\tmovq    %rax, -8(%rbp)\n''')
        # corresponds to indentedness of the brackets
        bracket_count = 0
        # unique locations for jumping
        unique = 1
        bracket_jumps = []
        i = 0
        while i < len(c):
            ch = c[i]
            match ch:
                case "+":
                    i, pcount = amt(c, i, "+")
                    file.write(f'''    movq    -8(%rbp), %rax\n\tmovzbl  (%rax), %eax\n\taddl    ${pcount}, %eax\n\tmovl    %eax, %edx\n\tmovq    -8(%rbp), %rax\n\tmovb    %dl, (%rax)\n''')
                case "-":
                    i, pcount = amt(c, i, "-")
                    file.write(f'''\tmovq    -8(%rbp), %rax\n\tmovzbl  (%rax), %eax\n\tsubl    ${pcount}, %eax\n\tmovl    %eax, %edx\n\tmovq    -8(%rbp), %rax\n\tmovb    %dl, (%rax)\n''')
                case ">":
                    i, pcount = amt(c, i, ">")
                    file.write(f"    addq    ${pcount}, -8(%rbp)\n")
                case "<":
                    i, pcount = amt(c, i, "<")
                    file.write(f"    subq    ${pcount}, -8(%rbp)\n")
                case ".":
                    file.write('''    movq    -8(%rbp), %rax\n\tmovzbl  (%rax), %eax\n\tmovsbl  %al, %eax\n\tmovl    %eax, %edi\n\tcall    putchar\n''')
                case ",":
                    file.write(f'''    call    getchar\n\tmovl    %eax, %edx\n\tmovq    -8(%rbp), %rax\n\tmovb    %dl, (%rax)\n''')
                case "[":
                    bracket_count += 2
                    bracket_jumps += [unique, unique + 1]
                    unique += 2
                    file.write(f'''    .L{bracket_jumps[bracket_count-2]}:\n\tmovq    -8(%rbp), %rax\n\tmovzbl  (%rax), %eax\n\ttestb   %al, %al\n\tje      .L{bracket_jumps[bracket_count-1]}\n''')
                case "]":
                    bracket_count -= 2
                    a = bracket_jumps[bracket_count]
                    b = bracket_jumps[bracket_count + 1]
                    file.write(f'''    jmp     .L{a}\n\t.L{b}:\n''')
                    bracket_jumps.remove(a)
                    bracket_jumps.remove(b)
                case _:
                    pass
            i+=1
        file.write("    movl $0, %eax\n    leave\n    ret\n")


if __name__ == "__main__":
    main(open("mdset.bf", "r").read())