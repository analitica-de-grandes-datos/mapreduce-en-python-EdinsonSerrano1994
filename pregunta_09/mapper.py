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

        linea_cambio = line.strip().split('  ')
        letra = linea_cambio[0].strip()
        fecha = linea_cambio[1].strip()
        valor = linea_cambio[-1].strip()
        sys.stdout.write("{}\t{}\t{}\n".format(letra,fecha,valor))