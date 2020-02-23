import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    for line in sys.stdin:
        letter = line.split(',')[0]
        value = line.split(',')[1]
        value = int(value)
        sys.stdout.write("{}\t{}\n".format(value, letter))