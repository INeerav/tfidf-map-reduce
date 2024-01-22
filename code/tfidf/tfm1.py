import sys
import os

# taken from the list ref: https://www.ranks.nl/stopwords
# to simply prevent such stopwords coming in between the spam detection
stopwords= ['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by',
            'can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers',
            'him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my',
            'neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so',
            'some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what',
            'when','where','which','while','who','whom','why','will','with','would','yet','you','your']

# input comes from STDIN (standard input)
# expected input stream from hadoop streamin jar would be in
########################
# (id)     (email body)
# 123   qwerty qwertysome
###########################
# so it is clean tab separated and space seperation between the line
# logic is for every mapper output will have the `:` separator, 
# why? because space separator behaves erratic at times
for line in sys.stdin:    
    if len(line) != 1 and line != '\n':
        id, email_body = line.split('\t', 1)
        # remove leading and trailing whitespace
        text = email_body.strip()
        # split the body into terms
        terms = email_body.split()
        
        for term in terms:
            # lower
            term = term.lower()
            # strip ends
            term = term.strip()

            if term not in stopwords:
                z = term + '-' + id
                print('%s:%s' % (z, 1))
