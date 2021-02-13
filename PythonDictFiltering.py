### one liners 
''' Here we have some data ''' 

names = {   1:"Alice",
            2:"Bob",
            3:"Carl",
            4:"Ann",
            5:"Liz"}

newDict = dict()

################################
## The basic way approach people can normally take is to use the below to filter a dictionary
################################
# for key, value in names.items():
#     # if key%2 == 1:
#     if len(value)< 5:
#         newDict[key] = value
# print()
# print(newDict)
################################


################################
# More efficient - This function abstracts away the filtering of a dictionary as 
# you pass in the dictionary and the function you want to use
################################
# def filter_dict(unfiltered ,function):
#     newDict = dict()
#     for key, value in unfiltered.items():
#         # if key%2 == 1:
#         if function(key,value):
#             newDict[key] = value
#     return(newDict)

# print(filter_dict(names, lambda k,v: k%2==1))               # is the value it odd 
# print(filter_dict(names, lambda k,v: k%2==0))               # is the value even
# print(filter_dict(names, lambda k,v: v.startswith('A')))    # does is the value start with an A


## ----- Filter Method
'''The dict has an inbuilt filter function which is pythonic and structured as follows: 

dict(filter(function, iterable)). 

Below in the function x[1] will be the value of each dictionary key value pair
'''
print(dict(filter(lambda x : x[1].startswith('A') , names.items())))




### --  Filter a dictionary with comprehension - The most pythonic way
'''
print({expression for (k,v) in names.items() if condition}) 
'''

print({k:v for (k,v) in names.items() if v.startswith('A')})
print({k:v for (k,v) in names.items() if k%2==1}) # all odd keys
print({k:v for (k,v) in names.items() if k%2==0}) # all even keys
