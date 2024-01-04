def check(S):
    
    if("a" in S and  "e" in S and  "i" in S and  "o" in S and  "u" in S):
        return 1
    return 0
def count_vowel_pairs(S):
    count=0
    if("a" in S and  "e" in S and  "i" in S and  "o" in S and  "u" in S):
        pass
    else: return 0
    newstr=""
    vowel="aeiou,"
    for a in S:
        if(a in vowel):
            newstr+=(a)
    colle=newstr.split(',')   
    for i,word1 in enumerate(colle):
        for j,word2 in enumerate(colle):
            if(i<j):
                cocat=word1+word2
#                print(str(i)+" "+ cocat)
                if(check(cocat)):
                    count+=1
                    
        
        
    return count
    #write your code here

S = str(input())

print (count_vowel_pairs(S))
