# VLSI CAD Project
# Inputs: input_list, gate
# Outputs: output of the gate

# -1 is invalid gate
# empty inlist means output will be invalid (-1)


# Ashish
# High = 1, Low = 0, Undefined = -1
def logic_eval (inlist, gate):
    _GATE = {'0':0, '1':1, 'and':2, 'nand':3, 'or':4, 'nor':5, 'xor':6, 'xnor':7}

    if gate < 0 | gate >7:
        output = -1
    elif gate == 0:
        output = 0
    elif gate == 1:
        output = 1

    else:
        if len(inlist) == 0:
            output = -1
        elif -1 in inlist:
            output = -1
        else:
            # And gate
            if gate == 2:
                 output = 1;
                 for val in inlist:
                     output *= val
            # Nand gate
            if gate == 3:
                output = logic_not(logic_eval(inlist, _GATE['and']))

            # OR gate
            if gate == 4:
                output = 0;
                for val in inlist:
                    output += val

            # NOR gate
            if gate == 5:
                output = logic_not(logic_eval(inlist, _GATE['nand']))

            # XOR gate
            if gate == 6:
                output = 0
                for val in inlist:
                    if val == 1:
                        output = logic_not(output)

            # XNOR gate
            if gate == 7:
                output = 1
                for val in inlist:
                    if val == 1:
                        output = logic_not(output)
    return output

def logic_not(x):
    if x == 1:
        y = 0
    elif x == 0:
        y = 1
    else:
        y = -1
    return y
