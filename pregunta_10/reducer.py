#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    numbers=[]
  
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        
        if key == curkey:
            
            numbers.append(val)
            
        else:

            if curkey is not None:
                
                numbers.sort()
                sys.stdout.write("{}\t{}\n".format(curkey, ','.join(str(x) for x in numbers)))

            curkey = key
            numbers= [val]

    numbers.sort()
    sys.stdout.write("{}\t{}\n".format(curkey, ','.join(str(x) for x in numbers)))