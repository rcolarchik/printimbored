from time import sleep
from random import *

time = .05

##################################################################################################################################
def letterspace(word,space):
    mword = word
    for i in range(len(word)):
        x = i+i
        #print(x)
        mword = mword[:x]+ ' ' + mword[x:]
        final = y+mword[1:]
        print(final)
        sleep(time)
    print(final)
    print(final)
    print(final)
    return final
def letterlessspace(word,space):
    mword = word
    x = 0
    abc = ''
    #print("***",mword,"***")
    #exit()
    for i in range(len(phrase)):
        x+=1
        remove = len(mword)-x
        beginning = mword[:remove][:-1]
        ending = mword[-x:]
        mword =  beginning + ending 
        final = space + mword
        #print(beginning)
        #Sprint(ending)
        print(final)
        #exit()
        sleep(time)
def outwards(phrase, num):
    x = 0
    space = ''
    while x<num:
        x += 1
        space += ' '
        statement = space + phrase
        print(statement)
        sleep(time)
    return [space,statement]
def inwards(phrase,num,spacestr):
    y = 0
    space = spacestr
    while y<num:
        y += 1
        space = space[1:]
        statement = space + phrase
        print(statement)
        sleep(time)
    return statement
#################################################################################

z = 0 
phrase = "I'm Bored"
depth1 = randint(1,100)
depth2 = randint(1,100)
num = 3
znum = randint(1,10)
rannum = randint(1,10)
while z<znum:
    z+=1
    print(phrase)
    sleep(time)
z=0
while  z<znum:
    z+=1  
    numspacesout = outwards(phrase,depth1)
    statement1 = numspacesout[1]
    statement = inwards(phrase,depth1, numspacesout[0])
lenstmt = len(statement)
#print(lenstmt)
lenib = len(phrase)
#print(lenib)
numspace = lenstmt-lenib
#print(numspace)
if numspace == 0:
    y = ''
else: 
    y = statement[:numspace]
#print(y)
#exit()
z = 0 
while  z<znum:
    z += 1
    spaced = letterspace(phrase,y)
    spaced = spaced[numspace:]
    unspaced = letterlessspace(spaced,y)
z = 0 
while z<znum:
    z+=1
    print(phrase)
    sleep(time)
z=0
while  z<znum:
    z+=1  
    numspacesout = outwards(phrase,depth2)
    statement = numspacesout[1]
    if z<znum:
        statement = inwards(phrase,depth2, numspacesout[0])   
    else:
        pass
lenstmt = len(statement)
#print(lenstmt)
lenib = len(phrase)
#print(lenib)
numspace = lenstmt-lenib
#print(numspace)
if numspace == 0:
    y = ''
else: 
    y = statement[:numspace]
#print(y)
#exit()
z = 0 
while  z<znum:
    z += 1
    spaced = letterspace(phrase,y)
    spaced = spaced[numspace:]
    unspaced = letterlessspace(spaced,y)
    