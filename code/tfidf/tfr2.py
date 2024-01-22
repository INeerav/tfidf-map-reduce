from operator import itemgetter
import sys

current_term = None
prev_body = None
current_count = 0
term = None
N=0
idf={}
line1=[]

# input from the tfm1 would term and the count
# this would append the idf score with - separator
# end result is term-id:rowcount-doccount
for line in sys.stdin:
    line = line.strip()
    line1.append(line)
    body, termcount = line.split(':', 1)
    term, count = termcount.split('-', 1)
    # todo: if fails put it under try parse int
    count = int(count)
    # term per body count 
    if prev_body == body:
        N=N + count
    else:
       if prev_body != None:
            idf[prev_body]=N
       N=0
       prev_body = body
idf[prev_body]=N

# put the separator for term-id:count-doccount
for hspace in line1:
    body, termcount = hspace.split(':', 1)
    term, count = termcount.split('-', 1) 
    for i in idf:
        if body == i:
           wf = term + '-' + body
           nN = count + '-' + str(idf[i])
           print('%s:%s' % (wf,nN))
    
