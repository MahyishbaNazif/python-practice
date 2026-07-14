#Given password is valid or not
'''Write a pyhton to validate the password based on the following conditions;
1) It should be at least 6 and at most 30 characters
2) It should start with an uppercase alphabet
3) It can contain numbers
4) It can contain characters !, @, #, $, %, ^, &, _, * and .
5) It should not have the characters /, =, ', ", and spaces'''
pwd = input()
valid = False
if 6 <= len(pwd) <= 30:
    if 'A' <= pwd[0] <= 'Z':
        if not('/' in pwd or '=' in pwd or "'" in pwd or '\"' in pwd or ' ' in pwd): 
         valid = True
print(valid)        
