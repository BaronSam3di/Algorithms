"""
----- Vialid Ip Addresses : Medium -----

------ BRIEF ------
You're given a string of length 12 or smaller, containing only digits. 
Write a function that returns all the possible IP addresses that can be create by inserting three "." in the string.

An IP address is a sequence of four positive integers that are separated by "."s 
where each individual integer is within the range 0- 255, inclusively.

An IP address isn't valid if any of the individual integers contains leading 0s. For example , "192.168.0.1" 
is a valid IP address, but "192.168.00.1" and "192.168.0.01" aren't, because they contain "00" and "01", respectively.
Another example of a valid IP address is "99.1.1.10"; conversley, "991.1.1.0" isn't valid, because "991" is greater than 255.

Your function should return the IP addresses in string format and in no particular order. 
If no valid IP addresses can be created from the string, your function should return an empty list.


A valid IP address will ... 
- be delimited by three full stops "." 
- have 4 separate sections eg "192.192.192.192"
- have each section will be at most 255
- have no leading zeros in a section eg : ".039"
- CAN have trailing zeros eg: "192.168.00.168
- can NOT have more than 12 digits 
- need a minimum of 4 digits "0.0.0.0"

------ Hints ------


------ Complexity ------ 


------ Approach ------
This problem is simple in theory but complex to implement. 
The best way to tackle this is to try and place all of the full stops in different places.
We would then check that the Ip address meets valid requirements above. 

"""

####################################################
## Time and Space : O(1)
####################################################

def validIPAddresses(string):
	ipAddressesFound = []

    # check the location for the first period
    for i in range(1, min(len(string), 4)):         # Place the first period from after the first digit and the 4, because we cannot have sections greater than 3
        currentIpAddressParts = ['','','','']       # this will store the ipp address parts we have to add to a our vaid 
        
        currentIpAddressParts[0] = string[:i]
        if not isValidPart(currentIpAddressParts[0]):
            continue
        
        # check the location for the second period
        for j in range(i + 1, i + min(len(string)-i, 4 )): # start by placeing the period past the first period
            currentIpAddressParts[1] = string[i:j]         # the start of the string to the 
            if not isValidPart(currentIpAddressParts[1]):
                continue
            
            # check the location for the third period
            for k in range(j + 1 , j + min(len(string) -j, 4)):
                currentIpAddressParts[2] = string[j:k]
                currentIpAddressParts[3] = string[k:] 
                
                # Only if the third and fourth parts are valid will we add them to ipAddressesFound
                if isValidPart(currentIpAddressParts[2]) and isValidPart(currentIpAddressParts[3]):
                    ipAddressesFound.append('.'.join(currentIpAddressParts))

    return ipAddressesFound

def isValidPart(string):
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False

    return len(string) == len(str(stringAsInt))     # trying to remove leading zeros with this conversion