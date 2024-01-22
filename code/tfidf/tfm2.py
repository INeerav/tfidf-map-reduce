import sys

# input format would be
# hello-123:1 
# so here we would split the term and the count from the id
for line in sys.stdin:    
    line = line.strip()    
    termbody, count = line.split(':', 1)
    term, id = termbody.split('-', 1)
    z = term + '-' + count
    print('%s:%s' % (id, z))
        
