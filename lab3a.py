def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''

    biggest_key = None
    
    for key in aDict.keys():
        if biggest_key is None or \
            len(aDict[biggest_key]) < len(aDict[key]):
                biggest_key = key
            
    return biggest_key 
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))
    
