


def convert(lines):
    flagOpers = ['addi', 'addr', 'muli', 'mulr', 'divi', 'divr']
    for index in range(len(lines)):
        adjust = [True for oper in flagOpers if oper in lines[index]]
        if 'subi' in lines[index] or 'subr' in lines[index]:
            line = lines[index].split(' ')[:-1]
            tmp1 = line[1]
            tmp2 = line[2]
            line[1] = tmp2
            line[2] = tmp1
            x = line
            new_line = '\nmove %s %s' % (x[-1], lines[index][-1])
            new_line = ' '.join(y for y in x) + new_line
            lines[index] = new_line
            lines[index] = new_line
        if True in adjust:
            line = lines[index].split(" ")
            x = line[:-1]
            new_line = '\nmove %s %s' % (x[-1], line[-1])
            new_line = ' '.join(y for y in x) + new_line
            lines[index] = new_line
    for l in lines:
        print(l)


