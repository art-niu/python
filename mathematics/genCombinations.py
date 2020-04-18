#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:57:45 2020

@author: arthurniu
"""

elements = ['a','b','c','d', 'e']
elements = ['a','b','c']


elementLength = len(elements)
combinationList = []

'''
Function insertIntoList is to insert element into specified list.
insertIntoList(List, String)

'''
def insertIntoList(list, element):
    
    tmpList = []
    
    listLen = len(list)
    l = listLen
    while l >= 0:
        newList = list.copy()
        newList.insert(l, element)
        #if newList not in combinationList:
        tmpList.append(newList)
        # end if
        l -= 1
    
    return tmpList
    #end while
#end def

'''
pits: ['a']
'''    
def generateCombinations(pits, seeds):

    pitsReplica = pits.copy()
        
    '''
    ridge 
    [['a']] : intiated
    [['a','b'], ['b','a']] : after one loop
    
    '''
    ridge = []
    ridge.insert(0,pitsReplica)
    
    ridgeLen = len(ridge)
    l = 0
    while seeds:
        '''
        pop out the first element of seeds, and eventually seeds will be empty
        '''
        pickedFromSeeds = seeds.pop(0)

        ridgeLen = len(ridge)
        n = 0
        ridgeTmp = []
        newPitsTmp = []

        '''
        [['a','b'],['b','a']]
        '''
        while n < ridgeLen :
            tmpPits = ridge[n]
            tmpPitsLen = len(ridge[n])
            m = 0
            
            '''
            ['a','b']
            '''
            while m < tmpPitsLen :
                ridgeTmp = insertIntoList(tmpPits, pickedFromSeeds)
                m += 1
                 
            ridgeTmpLen = len(ridgeTmp)
            
            '''
            append the new combinations for new ridge
            ['c', 'a', 'b'], ['a', 'c', 'b'], ['a', 'b', 'c']
            '''
            i = 0
            while i < ridgeTmpLen :
                newPitsTmp.append(ridgeTmp[i])
                i += 1
            # end while i
                
            n += 1
        

        '''
        Next loop should use to replace old ridge
        '''

        ridge = []
        
        for i in newPitsTmp :
            ridge.append(i)
        # end for
        ridge.sort()
        
        l += 1
    #end while seeds
    return ridge
#end def
    
p = 0
#while p < elementLength :
subElements = elements.copy()

pickedElements = subElements[0:1]
subElements.pop(0)
    
combination = generateCombinations(pickedElements, subElements)

print(combination)
print(len(combination))


seperator = ''
i = 0
while i < len(combination) :
    print(seperator.join(combination[i]))
    i += 1
# end while i
