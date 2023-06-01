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

        val, key = line.split("\t")
        key= list(key.strip().split(","))

        for letra in key:
            sys.stdout.write("{}\t{}\n".format(letra,val))