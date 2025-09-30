'''
Regex-Calculator

Author: Madhav Garg
'''

import re
import time
import os
from pynput.keyboard import Key, Listener

try:
    import colorama
    colorama.init()
except ImportError:
    pass

IS_WINDOWS = True if os.name == 'nt' else False
NORMAL_TEXT = "\033[0m"

RED = '\033[31m'
BLUE = '\033[0;34m'	
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
NORMAL = 'normal'

BOLD = '\033[1;37m'

MULT = r"(?<!\*)\*(?!\*)|[xX]|times|multiplied by|multiplyed by|multipled by|multipliedby"
ADD = r"\+|plus|added by|in addition to|in addtion to|increased by|icnreased by"
SUB = r"-|minus|subtracted by|lowered by"
DIVIDE = r"\\|/|divided by"
EXP = r"\^|\*\*|to the power of|to the exponent of"
SQRT = r"(?:sqrt|r|sqrt of|square root)"

ADD_MEMORY = r'add memory by|m\+'
SUBTRACT_MEMORY = r'subtract memory by|m-'

HELP = r'help|func'

IS_ADD_MEMORY = 'isaddmemory'
IS_SUB_MEMORY = 'issubtractmemory'

HELP_DOCUMENT = [
    'There are several currently availible functions:',
    '1. Multiplication. To do multiplication, you can use the "*" or the "x" operators, i.e. 3x3 or 3*3'
    '2. Addition. To add, you can use the "+" operator, i.e. 3+3',
    '3. Subtraction. To subtract, use the "-" operator',
    '4. To Divide, you can use "/"',
    '5. To ge the square root, use "sqrt" or "sqare root"',
    '6. To Add to memory, use "m+"',
    '7. To subtract memory, use "m-"',
    '8. To recall memory, use "rcm"',
    '9. For exponents, use "^", "**", "to the power of", or "to the exponent of"'
]

memory = 0

pkey = ' '

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def xy(self):
        return self.x, self.y

def move(x, y):
    return "\033[%d;%dH" % (y, x)

def on_press(key):
    global pkey
    #print(key)
    try:
        pkey = key.char
        pkey += ' '
    except AttributeError:
        if key == Key.enter:
            pkey = key
            #print("enter")
        elif key == Key.backspace:
            pkey = ''
        elif key == Key.space:
            pkey = '  '
        else:
            pkey = ' '
    return False

# Collect events until released

def join():
    with Listener(on_press=on_press,) as listener:
        listener.join()


os.system("color")

def clear(after=0):
    time.sleep(after)
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def red(*strings, end=''):
    tbr = RED
    for string in strings:
        tbr += str(string)
        if string != strings[-1]:
            tbr += ' '
    tbr += NORMAL_TEXT
    tbr += end
    return tbr

def green(*strings, end=''):
    tbr = GREEN
    for string in strings:
        tbr += str(string)
        if string != strings[-1]:
            tbr += ' '
    tbr += NORMAL_TEXT
    tbr += end
    return tbr

def blue(*strings, end=''):
    tbr = BLUE
    for string in strings:
        tbr += str(string)
        if string != strings[-1]:
            tbr += ' '
    tbr += NORMAL_TEXT
    tbr += end
    return tbr

def yellow(*strings, end=''):
    tbr = YELLOW
    for string in strings:
        tbr += str(string)
        if string != strings[-1]:
            tbr += ' '
    tbr += NORMAL_TEXT
    tbr += end
    return tbr

def bold(*strings, end=''):
    tbr = BOLD
    for string in strings:
        tbr += str(string)
        if string != strings[-1]:
            tbr += ' '
    tbr += NORMAL_TEXT
    tbr += end
    return tbr


def operate(string, operation):
    if operation == MULT:
        out = 1
    elif operation == ADD:
        out = 0
    elif operation == SUB:
        out = 'SUB'
    elif operation == DIVIDE:
        out = 'DIVIDE'
    elif operation == EXP:
        out = 'EXP'
    else:
        print (operation)
        time.sleep(1)
        exit()
        return (False, None)

    numbers = re.findall(r"([0-9]+(?:\.[0-9]+)?[ ]*)", string, re.I)
    present_operation = re.search(f"[0-9]+(?:\.[0-9]+)?[ ]*({operation})", string, re.I)

    if present_operation:
        #print(present_operation.groups())
        #print(numbers)

        for number in numbers:
            number_to_operate = float(number)
            #print(number)
            if operation == MULT:
                out *= number_to_operate
            elif operation == ADD:
                out += number_to_operate
            elif operation == SUB:
                if out == 'SUB':
                    out = number_to_operate
                else:
                    out -= number_to_operate
            elif operation == DIVIDE:
                if out == 'DIVIDE':
                    out = number_to_operate
                else:
                    out /= number_to_operate
            elif operation == EXP:
                if out == 'EXP':
                    out = number_to_operate
                else:
                    out **= number_to_operate
            else:
                print(present_operation)
                exit()

        if len(numbers) > 1:
            return (True, round(out, 15))
    return (False, None)

def operate_one_number(string, operation):
    test = re.findall(f"{operation}[ ]*([0-9]+(?:\.[0-9]+)?)", string, re.I)

    if len(test) > 1:
        return (False, "Too many numbers")
    elif len(test) == 0:
        return (False, "No numbers detected")
    else:
        try:
            test = float(test[0])
        except ValueError:
            print(test)
            time.sleep(1)
            return (False, None)
        
        if operation == SQRT:
            return (True, test ** 0.5)
        elif operation == ADD_MEMORY:
            return (True, test)
        elif operation == SUBTRACT_MEMORY:
            return (True, test)

def sqrt(string):
    return operate_one_number(string, SQRT)
    
def is_add_memory(string):
    return operate_one_number(string, ADD_MEMORY)

def is_subtract_memory(string):
    return operate_one_number(string, SUBTRACT_MEMORY)

def is_get_memory(string):
    test = re.findall(r"get memory|rcm", string, re.I)
    if len(test) == 1:
        return True
    return False

def is_help(string) :
    if re.match(HELP, string):
        return True
    return False

def ans(inp):
    global memory
    ismult, multans = operate(inp, MULT)
    isadd, addans = operate(inp, ADD)
    issub, subans = operate(inp, SUB)
    isdiv, divans = operate(inp, DIVIDE)
    isexp, expans = operate(inp, EXP)
    issqrt, sqrtans =  sqrt(inp)
    isaddmemory, add_memory_by = is_add_memory(inp)
    issubtractmemory, subtract_memory_by = is_subtract_memory(inp)
    isgetmemory = is_get_memory(inp)
    ishelp = is_help(inp)

    #print(isaddmemory, add_memory_by)
    #print(issubtractmemory, subtract_memory_by)
    #time.sleep(1)

    funcs = [ismult, isadd, issub, isdiv, isexp, issqrt, isaddmemory, issubtractmemory, isgetmemory, ishelp]
    functions = 0
    final_answer = 0

    for function in funcs:
        if function == True:
            functions += 1
    error = ''
    if functions == 0:
        error = red("No Valid Operation Detected...")
        return error, False
    elif functions > 1:
        error = red(f"Calculating with multiple functions ({functions} detected) is not yet supported...\n{funcs}")
        return error, False

    if ismult:
        final_answer = multans
    elif isadd:
        final_answer = addans
    elif issub:
        final_answer = subans
    elif isdiv:
        final_answer = divans
    elif isexp:
        final_answer = expans
    elif issqrt:
        final_answer = sqrtans
    elif isaddmemory:
        final_answer = (IS_ADD_MEMORY, add_memory_by)
    elif issubtractmemory:
        final_answer = (IS_SUB_MEMORY, subtract_memory_by)
    elif isgetmemory:
        final_answer = memory
    elif ishelp:
        final_answer = (HELP, 'Provides help on function, etc.')

    return final_answer, True


def cinput(string='', special=NORMAL, string_len = Vector2(5, 2)):
    global pkey

    move_offset = string_len

    output = ''
    print(end="\n" + string)
    pkey = ' '

    move_to = Vector2()

    while True:
        join()
        if pkey == ' ':
            continue
        elif pkey == Key.enter:
            break
        output += pkey
        output = output[:-1]
        #print(output)

        a, b = ans(output)
        
        if b:
            if isinstance(a, tuple):
                if a[0] == IS_ADD_MEMORY:
                    final_answer = yellow(f'  = add memory by {a[1]}')
                elif a[0] == IS_SUB_MEMORY:
                    final_answer = yellow(f"  = decrease memory by {a[1]}")
                elif a[0] == HELP:
                    final_answer = yellow(f"  {a[1]}")
            else:
                final_answer = yellow(f"  = {a:g}")
        else:
            final_answer = ''

        clear()


        move_to.x = move_offset.x + len(output)
        move_to.y = move_offset.y

        #print(move_to.x, move_to.y)

        if special == NORMAL:
            print(end="\n" + string + output + final_answer + move(move_to.x, move_to.y) )
        elif special == BOLD:
            print(end="\n" + string + bold(output) + final_answer + move(move_to.x, move_to.y) )
        else:
            raise ValueError(f"No special '{special}' found. Maybe try lowercase?")

    return output


def main():
    global pkey, memory
    first = True
    clear()
    final_answer = 0
    offset = Vector2(5,2)
    while True:
        clear()

        if not first and b:
            if final_answer:
                offset.y = 5
                inp = cinput(f">>  {inp} = {final_answer}\n{blue('Press Enter To Continue')}\n\n{bold('>>')}  ", special=BOLD, string_len=offset)
            else:
                offset.y = 5
                inp = cinput(f">>  {inp}\n{blue('Press Enter To Continue')}\n\n{bold('>>')}  ", special=BOLD, string_len=offset)
        else:
            inp = cinput(bold(">>  "), special=BOLD)

        a, b = ans(inp)

        if b:
            if isinstance(a, tuple):
                if a[0] == IS_ADD_MEMORY:
                    memory += a[1]
                    final_answer = ''
                elif a[0] == IS_SUB_MEMORY:
                    memory -= a[1]
                    final_answer = ''
                elif a[0] == HELP:
                    final_answer = HELP_DOCUMENT
                    print("\n")
                    for help in HELP_DOCUMENT:
                        print(green(help))
            else:
                final_answer = f"{a:g}"
        else:
            final_answer = a
            print("\n" + final_answer)
              
        print(blue("\nPress Enter To Continue"))

        pkey = ' '
        while pkey != Key.enter:
            join()

        first = False

if __name__ == '__main__':
    main()
