#bitwise & 
#1 only if both bits are 1
'''
A B A&B
0 0  0
0 1
'''

print(5&3)
print(6&2)

'''
real life :
permission system , masking operations
checking flags
'''

#bitwisw OR
# 1 if any one bit is 1
'''
A  B  A/B
0  0  0
0  1  1
1  1  1
1  0  1
'''

#Example:
print(5|3) #7
'''
5---->0101
3---->
'''
print(12|4)
#bitwise XOR ---> imp interviews
#same bits ---> 0
#different bits ---->1
#1 if both bits are different
'''
A  B  A^B
0  0   0
0  1   1
1  1   0
1  0   1
'''
print(6^2)

# swap the numbers without using a 3rd variable

#input = 5 , 4
#output = 4 ,5

a = 5+3
b = 8-3
a = 8-5

print(a, b)

#perform  the same operation using XOR

'''
a = a^b
#a = 5^3 -->6
b = a^b
#b = 6 ^ 3 --> 5
a = a^b
a = 6 ^ 5 -->3
'''

a = a^b
b = a^b
a = a^b
print(a, b)

#Bitwise 

# 0 ---> 1
# 1 --> 0

print(~5) # -6

# ~n = -(n+1)

print(~10)

#low level memory operations

# << left shift operation

#rule --> shift the bits to left

print(5<<1) #10

'''
5 ---> 0 1 0 1
<< --> 1 0 1 0----> 10
'''

#formula ==> n<<k  = n*2^k

#Right shift : shift the bits to right

print(8>>1)
'''
8 ---> 1 0 0 0
       0 1 0 0 -->4

'''

# formula = n>>k = n/2^k
print(16>>2)
print(12>>6)


print(13>>7)
print(17>>8)