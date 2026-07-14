#Encode and decode a string
alphabets='abcdefghijklmnopqrstuvwxyz'
encode='sbwkrq'
decode=''
for i in range(len(encode)):
    decode += alphabets[(alphabets.index(encode[i])-3)%26]
print(decode)                        