from operator import itemgetter
import sys

# defaults flags for the reduce 1 step
current_term = None
current_count = 0
term = None

def represents_int(s):
    # to perform the try parse int
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

# expected input format from hadoop streaming : 
# qwerty-123:1
# qwertysome-456:1
# so on...
for line in sys.stdin:    
    line = line.strip()    
    term, count = line.split(':', 1)

    # convert count (currently a string) to int
    if represents_int(count):
        count = int(count)  
    else:
        # safely ignore the line
         continue    

    # Hadoop sorts map output before passing to reducer
    if current_term == term:
        current_count += count        
    else:
        if current_term:
            # write result to STDOUT
            print('%s:%s' % (current_term, current_count))
        current_count = count
        current_term = term

# to tackle the end term
if current_term == term:
    print('%s:%s' % (current_term, current_count))
