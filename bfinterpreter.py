class Byte:
    def __init__(self, val = 0):
        self._val = val

    def inp(self, data):
        self._val = data % 255

    def __add__(self, other):
        addval = 0
        if type(other) is int:
            addval = other
        elif type(other) is Byte:
            addval = other._val
        return Byte((self._val + addval) % 255)

    def __sub__(self, other):
        subval = 0
        if type(other) is int:
            subval = other
        elif type(other) is Byte:
            subval = other._val
        return Byte((self._val - subval) % 255)

    def __eq__(self, other):
        if type(other) is int:
            return self._val == other
        elif type(other) is Byte:
            return self._val == other._val

    def __ne__(self, other):
        return not (self == other)
    
    def __str__(self):
        return chr(self._val)

    def __repr__(self):
        return int(self._val)

    

def run(bfstring):
    memlength = 30000
    mem = [Byte() for _ in range(memlength)]
    pointer = 0
    strindex = 0
    while strindex < len(bfstring):
        ch = bfstring[strindex]
        if ch == ">":
            pointer = (pointer + 1) % memlength
        elif ch == "<":
            pointer = (pointer - 1) % memlength
        elif ch == "+":
            mem[pointer] += 1
        elif ch == "-":
            mem[pointer] -= 1
        elif ch == ".":
            print(mem[pointer], end = "")
        elif ch == "[":
            if mem[pointer] == 0:
                bracket_count = 1
                while bracket_count > 0:
                    strindex += 1
                    if bfstring[strindex] == "[":
                        bracket_count += 1
                    elif bfstring[strindex] == "]":
                        bracket_count -= 1
        elif ch == "]":
            if mem[pointer] != 0:
                bracket_count = 1
                while bracket_count > 0:
                    strindex -= 1
                    if bfstring[strindex] == "[":
                        bracket_count -= 1
                    elif bfstring[strindex] == "]":
                        bracket_count += 1
        else:
            strindex +=1
            continue
        strindex +=1
        #print(ch, pointer, mem[pointer])


hello_instr = '''>++++++++[<+++++++++>-]<.>++++[<+++++++>-]<+.+++++++..+++.>>++++++[<+++++++>-]<+
+.------------.>++++++[<+++++++++>-]<+.<.+++.------.--------.>>>++++[<++++++++>-
]<+.'''

square_instr = '''++++[>+++++<-]>[<+++++>-]+<+[
    >[>+>+<<-]++>>[<<+>>-]>>>[-]++>[-]+
    >>>+[[-]++++++>>>]<<<[[<++++++++<++>>-]+<.<[>----<-]<]
    <<[>>>>>[>>>[-]+++++++++<[>-<-]+++++++++>[-[<->-]+[<<<]]<[>+<-]>]<<-]<<-
]'''

quine_instr = "->++>+++>+>+>++>>+>+>+++>>+>+>++>+++>+++>+>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+>+>++>>>+++>>>>>+++>+>>>>>>>>>>>>>>>>>>>>>>+++>>>>>>>++>+++>+++>+>>+++>+++>+>+++>+>+++>+>++>+++>>>+>+>+>+>++>+++>+>+>>+++>>>>>>>+>+>>>+>+>++>+++>+++>+>>+++>+++>+>+++>+>++>+++>++>>+>+>++>+++>+>+>>+++>>>+++>+>>>++>+++>+++>+>>+++>>>+++>+>+++>+>>+++>>+++>>+[[>>+[>]+>+[<]<-]>>[>]<+<+++[<]<<+]>>>[>]+++[++++++++++>++[-<++++++++++++++++>]<.<-<]"


run(hello_instr)