str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"

str1ToNum = int(str1, 16)
str2ToNum = int(str2, 16)

XORresult = str1ToNum ^ str2ToNum

final = hex(XORresult)
print(final)
