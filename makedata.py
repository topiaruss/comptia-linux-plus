# Tools for making some dummy files for testing linux commands
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
     
LISTLEN = 16
people = []
for person in range(LISTLEN):
    data = dict(first=ran(first), last=ran(last),\
                city=ran(city), state=ran(state),
                dob=randate(),
                sal=ran(range(5000,10000)),
                ssn = ssn())
    vals=[]
    for v in 'first last city state ssn sal dob'.split():
        vals.append(data[v])
    print "%13s %13s, %13s, %3s, SSN: %13s %6s %11s" % tuple(vals)
    
    
