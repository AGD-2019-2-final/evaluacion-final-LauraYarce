import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
    v1=[]
    for line in sys.stdin:
        letter, value = line.split("\t")
        value = int(value)
        v1.append((letter,value))
    v1.sort(key=lambda orden: (orden[0], orden[1]))
    curkey = None
    for line in v1:
        if curkey == line[0]:
            sys.stdout.write(",{}".format(line[1]))
        else:
            if curkey is not None:
                sys.stdout.write("\n{}\t{}".format(line[0],line[1]))
                curkey = line[0]
            else:
                sys.stdout.write("{}\t{}".format(line[0],line[1]))
                curkey = line[0]