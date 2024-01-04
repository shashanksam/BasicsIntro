IAP
Level 1
00
Hours
:
06
Minutes

Question List
Vowel Pairs
20%
Streak Number
0%
Balanced words
0%

Problem Statement
Given a number N having L digits, write a program to find the streak number using the following rules:

O=Σ(Ni*2) where Ni represents the digit at odd position and (Ni*2)<L
E=ΣNj where Nj represents the digit at even position
Streak(S)=k where S is O+E and k is the smallest whole number when S+k is not divisible by k+1
Input Format

  

Read the input from standard input stream

 

Output Format

 

Print the streak number to the standard output stream

 

Sample Input	Sample Output	Explanation
56789112	3	In the given input, the digits 5,7,9 and 1 are at the odd positions and its doubled value correspondingly would be 10,14,18 and 2. 10,14 and 18 are greater than the length of the given input number i.e. 8. Hence O= 2. Similarly, E= 6+8+1+2. Now the S is 19 for which the streak number must be identified. When the value of k=0, 19+0 is divisible by 1+0, when k=1,19+1 is divisible by 1+1, and so on. When k=3, 19+3 is not divisible by 3+1. Hence the streak number for 19 is 3.
98979	2	NA


)
def validate_number(input_number): 
    leg=length(str(input_number))
    print(leg)
    pass 
​
    #Remove pass and write your code here 
​
input_number = int(input()) 
​
print(validate_number(input_number)) 

          


No.	Input	Expected Output	User Output	Time Taken (s)	Status	Download
1	98979	2	Traceback (most recent call last):
File "file.py", line 10, in
print(validate_number(input_number))
File "file.py", line 2, in validate_number
leg=length(str(input_number))
NameError: name 'length' is not defined
  Runtime Error	
2	56789112	3	Traceback (most recent call last):
File "file.py", line 10, in
print(validate_number(input_number))
File "file.py", line 2, in validate_number
leg=length(str(input_number))
NameError: name 'length' is not defined
  Runtime Error	




##TO DO

def validate_number(input_number): 
    leg=len(str(input_number))
    O=0
    E=0
    pos=1
    for i in str(input_number):
        if(pos%2==0):
            E+=int(i)
        elif(int(i)*2<leg):
            O+=int(i)*2
        pos+=1
    
    print(O)
    print(E)
        
    pass 

    #Remove pass and write your code here 

input_number = int(input()) 

print(validate_number(input_number)) 
