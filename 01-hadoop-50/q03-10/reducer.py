import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    value = 0

    for line in sys.stdin:
        key, val = line.split("\t")
        if curkey is not None:
            sys.stdout.write("{},{}\n".format(value.replace("\n",""), curkey))
        curkey = key
        value = val

    sys.stdout.write("{},{}".format(value.replace("\n",""), curkey))