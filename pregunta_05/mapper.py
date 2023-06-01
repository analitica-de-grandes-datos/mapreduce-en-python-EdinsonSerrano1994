#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:

        fecha = line.strip().split('  ')[1]
        mes = fecha.strip().split('-')[1]
        sys.stdout.write("{}\t1\n".format(mes))