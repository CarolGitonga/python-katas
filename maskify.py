"""
Usually when you buy something, you're asked whether your credit card number, 
phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want
that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.
"""

def maskify(cc):
    #check if the string length is equal or less than 4
    if len(cc) <= 4:
        #return the original string if its 4 or less characters
        return cc
    #replace all characters with '#' except the last 4
    masked_string = '#' * (len(cc) - 4) + cc[-4:]
    
    return masked_string

#example usage:
credit_card_number = '12345666954902'
masked_credit_card = maskify(credit_card_number)
print (masked_credit_card)
#example2 usage:
favourite_city = 'Nairobi'
masked_credit_card = maskify(favourite_city)
print (masked_credit_card)