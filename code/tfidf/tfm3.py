import sys
import os


# input expected 
# hello-123:1-6
for rowline in sys.stdin:    
    rowline = rowline.strip()    
    wf, nN = rowline.split(':',1)
    w, f = wf.split('-', 1)
    z = f + '-' + nN + '-' + str(1)
    print('%s:%s' % (w,z))

        
