'''
Created on Feb 20, 2014

@author: mherron

MAKE SURE RECORD_NUM IS UNIQUE!!! OR ELSE CARROT WILL COMPLAIN

Opens a delimited text file containing a record_num, description, and label, and generates an XML file according to the standard Carrot2 input format:

<?xml version="1.0" encoding="UTF-8"?>
<searchresult>
  <query>Globe</query>
  <document id="0">
    <title> </title>
    <url> </url>
    <snippet> </snippet>
  </document>
</searchresult>

'''
import re
import sys

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

def stripchars(txt):
    txt=re.sub('(\++|\&+|\!+|\(+|\)+|\{+|\}+|\[+|\]+|\^+|\"+|\'+|\~+|\*+|\?+|\:+|\\+|\/+|\%+|,+|<|>)',' ',txt)
    txt=re.sub('\s+',' ',txt)
    return txt

infilename=""
outfilename="[pathname].xml"
sep='|'

outfile = open(outfilename, "w")

outfile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<searchresult>\n  <query>all</query>\n")

line_counter=0
#uniques = []

with open(infilename) as infile:
    for line in infile:
        line = stripchars(removeNonAscii(line))
        (record_num,desc,unspsc) = line.lower().split(sep)
        
        desc = stripchars(desc)
        
        #if record_num not in uniques:
        #uniques.append(record_num)
        outfile.write("<document id=\"" + str(record_num) + "\">\n    <title>" + unspsc + "</title>\n    <url> </url>\n    <snippet>" + desc + "</snippet>\n</document>\n")
        line_counter+=1
        if line_counter%1000==0: 
            sys.stdout.write('.')
            sys.stdout.flush()
            if line_counter%10000==0:
                sys.stdout.write(str(line_counter) + '\n')
                sys.stdout.flush()
        
outfile.write("\n</searchresult>\n")
infile.close()
outfile.close()

print("\nProcessed " + str(line_counter) + " records written to " + outfilename)
