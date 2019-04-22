


def convert(lines):
    flagOpers = ['addi', 'addr', 'subr', 'muli', 'mulr', 'divi', 'divr']
    for index in range(len(lines)):
        adjust = [True for oper in flagOpers if oper in lines[index]]
        if 'subi' in lines[index]:
            top_line = lines[index-2].split(" ")
            f_line = lines[index-1].split(" ")
            line = lines[index].split(" ")
            n_line = lines[index + 1].split(" ")

            reg = f_line[2]
            tmp = top_line[2]
            f_line[2] = tmp
            top_line[2] = reg
            line = line[:-1]
            n_line[1] = tmp
            f_line = " ".join(x for x in f_line)
            top_line = " ".join(x for x in top_line)
            line = " ".join(x for x in line)
            n_line = " ".join(x for x in n_line)

            lines[index - 2]= top_line
            lines[index - 1] = f_line
            lines[index] = line
            lines[index + 1] = n_line
        elif True in adjust:
            f_line = lines[index-2].split(" ")
            line = lines[index].split(" ")
            n_line = lines[index + 1].split(" ")
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


