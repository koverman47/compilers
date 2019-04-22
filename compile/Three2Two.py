


def convert(lines):
    flagOpers = ['addi', 'addr', 'subr', 'muli', 'mulr', 'divi', 'divr']
    for index in range(len(lines)):
        adjust = [True for oper in flagOpers if oper in lines[index]]
        if 'subi' in lines[index]:
            line = lines[index].split(' ')[:-1]
            next_line = lines[index + 1].split(' ')
            tmp1 = line[1]
            tmp2 = line[2]
            line[1] = tmp2
            line[2] = tmp1

            next_line[1] = tmp1

            line = " ".join(x for x in line)
            next_line = " ".join(x for x in next_line)

            lines[index] = line
            lines[index + 1] = next_line
        elif True in adjust:
            line = lines[index].split(" ")
            n_line = lines[index + 1].split(" ")
            reg = line[3]
            line = line[:-1]
            n_line[1] = reg
            line = " ".join(x for x in line)
            n_line = " ".join(x for x in n_line)
            lines[index] = line
            lines[index + 1] = n_line
    for l in lines:
        print(l)


