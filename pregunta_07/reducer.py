#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    ordenar_data=[]
    for line in sys.stdin:

        key,fecha, val = line.strip().split('\t')
        val=int(val)
        ordenar_data.append((key,fecha,val))

    for sort in sorted(ordenar_data, key=lambda x: (x[0], x[2])):
        sys.stdout.write("{}  {}  {}\n".format(sort[0],sort[1],sort[2]))