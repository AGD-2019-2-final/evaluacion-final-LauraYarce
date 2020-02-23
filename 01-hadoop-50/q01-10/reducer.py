import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':
    curkey = None
    t = 0
    for line in sys.stdin:
        key, value = line.split("\t")
        value = int(value)
        if key == curkey:
            t += value
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, t))
            curkey = key
            t = value

    sys.stdout.write("{}\t{}\n".format(curkey, t))