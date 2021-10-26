s = "MCMXCIV"
result = 0
roman_dict = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
    'IX':9,
    'IV':4,
    'XL':40,
    'XC':90,
    'CD':400,
    'CM':900
}
i=0
while i < (len(s)-1):
    if (s[i]+s[i+1]) in roman_dict:
        result += roman_dict[s[i]+s[i+1]]
        i+=2
    else:
        result += roman_dict[s[i]]
        i+=1
    print("while ",result, i)
if i == len(s):
    print(result)
else:
    result+=roman_dict[s[len(s)-1]]

print(result)
    