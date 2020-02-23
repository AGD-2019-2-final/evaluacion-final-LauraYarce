import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
    curkey = None
    for line in sys.stdin:
        key, value = line.split("\t")
        value = float(value)
        if key == curkey:
            if value > max:
                max = value
            else:
                if value < min:
                    min = value
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max, min))
            curkey = key
            max = value
            min = value
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, max, min))