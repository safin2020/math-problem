data = [1,2,3,1,2,3]

def no_duplicates(duplicates):
    no_dup=[]
    for element in duplicates:

        if element not in no_dup:
            no_dup.append(element)
    return no_dup
print('after removing duplicate the list is = ', no_duplicates(data) )      
