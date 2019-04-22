


def convert(lines):
    flagOpers = ['addi', 'addr', 'subi', 'subr', 'muli', 'mulr', 'divi', 'divr']
    for index in range(len(lines)):
        adjust = [True for oper in flagOpers if oper in lines[index]]
        if True in adjust:
            f_line = lines[index-2].split(" ")
            line = lines[index].split(" ")
            n_line = lines[index + 1].split(" ")

            #reg = line[3]
            reg = f_line[2]
            line = line[:-1]
            n_line[1] = reg
            f_line = " ".join(x for x in f_line)
            line = " ".join(x for x in line)
            n_line = " ".join(x for x in n_line)
            lines[index - 2]= f_line
            lines[index] = line
            lines[index + 1] = n_line
    for l in lines:
        print(l)


