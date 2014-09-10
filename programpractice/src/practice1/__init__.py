# solution to problem found at http://www.reddit.com/r/dailyprogrammer/comments/2cld8m/8042014_challenge_174_easy_thuemorse_sequences/

def complement(n):
    num='0'
    for i in n:
        if i=='0':
            newval='1'
        else:
            newval='0'
        num+=newval
    return num

startnum= 0
iterationnum=0
loopnum= int(input("Enter how many times to do Thue-Morse Sequence \n"))
print("nth \t Sequence")
print("===========================================================================")
for j in range(0, loopnum, 1):
    print(str(iterationnum) +  "\t" + str(startnum))
    num2=complement(str(startnum))
    startnum=str(startnum)+ str(num2)
    iterationnum = iterationnum + 1

        
