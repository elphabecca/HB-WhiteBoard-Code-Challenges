

num_dict = {2 : ['A', 'B', 'C'],
            3 : ['D', 'E', 'F'],
            4 : ['G', 'H', 'I'],
            5 : ['J', 'K', 'L'],
            6 : ['M', 'N', 'O'],
            7 : ['P', 'Q', 'R', 'S'],
            8 : ['T', 'U', 'V'],
            9 : ['W', 'X', 'Y', 'Z']}

def numpad(numstr):

    pass

numbs = {'2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}

def combo(phnum):
    if len(phnum) == 1:
        return list(numbs[phnum]
    else:
        result = combo(phnum[:-1])
    
    return [(ch1+ch2) for ch1 in result for ch2 in numbs[phnum[-1]]]

print combo('234')

