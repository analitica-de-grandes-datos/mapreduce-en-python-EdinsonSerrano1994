#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    val_max = 0
    val_min = 0

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:

            if val > val_max:
                val_max = val

            if val < val_min:
                val_min=val

        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, val_max,val_min))

            curkey = key
            val_max = val
            val_min = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey,val_max,val_min))