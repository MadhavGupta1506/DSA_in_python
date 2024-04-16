def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    sum=0
    dic={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        "IV":4,
        "IX":9,
        "XL":40,
        "XC":90,
        "CD":400,
        "CM":900
    }
    v1=0
    for i in range(len(s)-1,-1,-1):
        print(s[i-1],s[i],end="")
        if(i-1>-1) and(s[i-1]=="I" and s[i]=="V")and(s[i-1]=="I" and s[i]=="X")and(s[i-1]=="X" and s[i]=="L")and(s[i-1]=="X" and s[i]=="C")and(s[i-1]=="C" and s[i]=="D")and(s[i-1]=="C" and s[i]=="M"):
            val="".join([dic[s[i-1]],dic[s[i]]])
            print(val)
            v1+=dic[s[i-1]]
            print(v1)
        else:
            sum+=dic[s[i]]
        print()
    return sum-v1
s="MCMXCIV"
print(romanToInt(s))