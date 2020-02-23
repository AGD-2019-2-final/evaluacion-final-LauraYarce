import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    t = 0
    count = 1
    for line in sys.stdin:
        key, value = line.split("\t")
        value = float(value)
        if key == curkey:
            t = t + value
            count += 1
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, t , t/count))
                count = 1
            curkey = key
            t = value
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, t , t/count))