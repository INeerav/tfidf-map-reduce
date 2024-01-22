import sys
import os
from math import log,sqrt

# assignment needs just top 10 spam/ham
D=10.0

def represents_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

# final step : to extract all the '-' separated fields to 
# calculate tf idf score and append it to terms in comma separated
# TODO : try except : done
# put all the ifs file size is small hence too many zeros
for line in sys.stdin:    
    line = line.strip()    
    try:
        wf, nNm = line.split(':')
        term, id = wf.split('-')
        n, N, m = nNm.split('-')
        tfidf = 0        
        if represents_int(n) and represents_int(N) and represents_int(m) and n != 0 and N != 0 and m != 0:
            n = float(n)
            N = float(N)
            m = float(m)
            # tfidf = (termcount/doccount)*log( totaldoc (10) /documents Containing terms)
            tfidf = round((n/N)*log(D/m),3)
        else:
            tfidf = 0
        # comma separated for hive tables
        print('%s,%s,%s' % (id, term, tfidf))
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as e:
        print(e)

        
