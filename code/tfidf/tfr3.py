from operator import itemgetter
import sys

prev_term = None
count = 1 
term = None
idf={}
line1=[]


# expected out from the reducer
# term-id:f-N-count
# so that in the final tfidf we'd have all the values for
# tfidf = (termcount/doccount)*log( totaldoc (10) /documents Containing terms)
# todo : try except if fails
for rowline in sys.stdin:
    rowline = rowline.strip()
    w, z = rowline.split(':', 1)
    f, nNc = z.split('-',1)
    n, Nc = nNc.split('-',1)
    N, c = Nc.split('-',1)
    if prev_term == w:
        # todo: if this fails put it in tryparse
        count = count + int(c)
    else:
        if prev_term != None:
            q = n + '-' + N + '-' + str(count)
            idf[prev_term] = q
            j= prev_term + '-' + f
            line1.append(j)
        count=1
        prev_term = w

       
q = n + '-' + N + '-' + str(count)
idf[prev_term] = q
j = prev_term + '-' + f
line1.append(j)

for h in line1:
   w, f= h.split('-',1)
   for d in idf:
       if w == d:
          print('%s:%s' % (h, idf[d]))
