"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher. Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
"""

#function that takes a singe parameter 'text'
def rot13(text):
    #initialize an empy list called 'result'
    result = []
    #iterate thro each character in the input 'text' using loop
    for char in text:
        #check if it is a lowercase btn a and z or uppecase btn A and Z
        if 'a' <= char <= 'z':
            #if its lowercase calculate the offset value using 'ord('a')'
            offset = ord('a')
            #apply the ROT13 transformation by subtracting the offset,
            # adding 13, taking the modulo 26 to ensure the wraparound, 
            # and then adding the offset back.
            result.append(chr((ord(char) - offset + 13) % 26 + offset ))
            #do the same with uppercase
        elif 'A'  <= char <='Z':
            offset = ord('A')
            result.append(chr((ord(char) - offset + 13) % 26 + offset ))
            #If the character is neither lowercase nor uppercase letter, append it to the 'result'
        else:
            result.append(char)
            #combine all the individual characters in the result list into a single string.
    return ''.join(result) 

#example
input_text = 'Hello, world! This is a test 123.'
ciphered_text = rot13(input_text)   
print (ciphered_text)






