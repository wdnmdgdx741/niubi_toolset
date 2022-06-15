import base64
 
text = [
    '96',
    '65',
    '93',
    '123',
    '91',
    '97',
    '22',
    '93',
    '70',
    '102',
    '94',
    '132',
    '46',
    '112',
    '64',
    '97',
    '88',
    '80',
    '82',
    '137',
    '90',
    '109',
    '99',
    '112']
text = text[::-1]
 
def decode():
    code = ''
    for i in range(24):
        if(i%2 == 0):
            a = int(text[i]) - 10
        else:
            a = int(text[i]) + 10
        a = i ^ a
        code = code + chr(a)
    print(code)
    
decode()
