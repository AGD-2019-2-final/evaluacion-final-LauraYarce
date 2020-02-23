import sys
#
#  >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None

    for line in sys.stdin:
        key, value = line.split("\t")
        value = int(value)
        if key == curkey:
            if value > max:
                max = value
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, max))
            curkey = key
            max = value

    sys.stdout.write("{}\t{}\n".format(curkey, max))