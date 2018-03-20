# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re
from hazm import *

normalizer = Normalizer()
file = open("int.txt",'w')
file.close()
file2 = open("ghazal.txt",'w')
file.close()
file = open("int.txt",'a')
text1 = open("monzavi.txt",'r').read()
text2 = open("shahriar.txt",'r').read()
text3 = open("bahmani.txt",'r').read()
text4 = open("bahar.txt",'r').read()
text5 = open("ebtehaj.txt",'r').read()
file.write(text1)
file.write(text2)
file.write(text3)
file.write(text4)
file.write(text5)
file.close()
text = open("int.txt",'r').read()
#text = re.sub(' من ',' ',text)
text = re.sub(' در ',' ',text)
text = re.sub(' با ',' ',text)
text = re.sub(' به ',' ',text)
text = re.sub(' برای ',' ',text)
text = re.sub(' این ',' ',text)
text = re.sub(' چون ',' ',text)
text = re.sub(' از ',' ',text)
text = re.sub(' را ',' ',text)
text = re.sub(' تا ',' ',text)
text = re.sub(' هر ',' ',text)
text = re.sub(' بر ',' ',text)
text = re.sub(' چه ',' ',text)
text = re.sub(' چو ',' ',text)
text = re.sub(' ای ',' ',text)
text = re.sub(' آن ',' ',text)
text = re.sub(' و ',' ',text)
text = re.sub(' که ',' ',text)
#text = re.sub(' ز ',' ',text)
text = re.sub(' اگر ',' ',text)
text = re.sub(' گر ',' ',text)
text = re.sub(' هم ',' ',text)
text = re.sub(' بی ',' ',text)


text = re.sub('،','',text)
text = re.sub('؟','',text)
text = re.sub(':','',text)
text = re.sub('  ',' ',text)

#print(text)
text = normalizer.normalize(text)
#text = re.sub(' ','\n',text)

file2 = open("ghazal.txt",'a')
file2.write(text)
file2.close()
file.close()

###################################################################

from collections import Counter

with open("ghazal.txt") as file:
    wordcount = Counter(file.read().split()).most_common(20)
    print(wordcount)