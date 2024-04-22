def roman(s):
    romanDict={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    result=0
    for iindex, val in enumerate(s):#val="I"
        
        zahl = romanDict.get(val)
        try: 
            nextZahl= romanDict.get( s[iindex+1])
            if zahl < nextZahl:
                result-=zahl
            else: 
                result +=zahl
        except:
            result+=zahl
    return result
print(roman("LVIII"))
aufgabe1="III"
aufgabe2="MCMXCIV"