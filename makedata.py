# Tool for making some dummy files for testing linux commands
# Russ Ferriday
# 2011-02-06
import random

first = """
    Randy Ariel Scott Ali Mary Kyle Faroqh Seb John Pat Joe Anna Kurt
    Nancy Gloria Dave Fritz Mo Chuck Ted Troy Florrie Doran Alexa"""
last = """Cunningham Jones Mir Davies McAllister Deboo Chang Perkeo Ettlinger
    Holla Tran Bacon"""
city = """Springfield Davis Homeville Panacea Harmony Coreville Appleton York 
    Bigville Grover VileVille Toyola Jonstown Cardiff Seattle Boots Saltpan 
    Gulchy Longman  Herod""" 
state = """AL CA OR WY VA FL AZ NY WA IA"""

first = first.split()
last = last.split()
city = city.split()
state = state.split()

def randate():
    day = random.sample(range(27),1)[0] + 1
    month = random.sample(range(11),1)[0] + 1
    year = random.sample(range(1940, 1990),1)[0] + 1
    return '%04d-%02d-%02d' % (year, month, day)

def ran(lst):
    return random.sample(lst,1)[0]
    
def ssn():
    return '%d%d%d-%d%d-%d%d%d%d' % tuple(random.sample(range(9),9))
    
fieldlist = 'first last city state ssn sal dob'.split()
fmt = "%8s %11s, %11s, %6s, %12s %6s %11s"

LISTLEN = 16
people = []
for person in range(LISTLEN):
    people.append( dict(first=ran(first), last=ran(last),
                city=ran(city), state=ran(state),
                dob=randate(),
                sal=str(ran(range(5000,10000))),
                ssn = ssn()) )
                
#create output files
tabbedfile = file('census-tabbed', 'w')
spacedfile = file('census-spaced', 'w')

#put headers in both
tabbedfile.write( '\t'.join(fieldlist) + '\n' ) 
spacedfile.write( fmt % tuple(fieldlist) + '\n' ) 

#add the data, in two different ways...
for person in people:        
    vals=[]
    for v in fieldlist:
        vals.append(person[v])
    tabbedfile.write( '\t'.join(vals) + '\n' )
    spacedfile.write( fmt % tuple(vals) + '\n' )

for f in tabbedfile, spacedfile:
    print 'created: %s' % f.name
    
tabbedfile.close()
spacedfile.close()
    
    
