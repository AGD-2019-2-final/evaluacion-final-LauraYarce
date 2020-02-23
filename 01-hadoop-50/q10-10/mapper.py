import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    vec =[]
    for line in sys.stdin:
        value = line.split('\t')[0]
        letter = line.split('\t')[1]
        for i in letter.split(','):
            vec.append((value,i))
    for line in vec:
        sys.stdout.write("{}\t{}\n".format(line[1].strip(), line[0].strip()))