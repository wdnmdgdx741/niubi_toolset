import string 
def shift_right(text, num): 
    return text[num:] + text[:num] 
cipher = 'NmSgNv{m09f718v9kr8gk7p66ncv38nr0i44640}' 
key = 'virginia' 
upper_case = string.ascii_uppercase 
lower_case = string.ascii_lowercase 
lower_case_table = [shift_right(lower_case, i) for i in range(26)] 
upper_case_table = [shift_right(upper_case, i) for i in range(26)] 
flag = '' 
cnt = 0 
for c in cipher: 
    if c.isalpha(): 
        if c in upper_case: 
            flag += upper_case[upper_case_table[upper_case.index(key[cnt%len(key)].upper())].index(c)] 
        else:
            flag += lower_case[lower_case_table[lower_case.index(key[cnt%len(key)].lower())].index(c)] 
        cnt += 1 
    else:
        flag += c 
print(flag) 
