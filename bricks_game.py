N = int(input())
motu = 0
patlu = 0
br = N
i = 1
pos = ""
while(N != 0):
    motu = 0
    patlu = 0
    if N >= i + i*2:
        patlu = patlu + i
        motu = motu + i*2
        pos = "m"
        N = N - i - i*2
        i += 1
    elif N >= i:
        patlu = patlu + i
        N = N - i
        pos = "p"
        while(N > 0):
            motu = motu + 1
            N = N - 1
            pos = "m"
    else:
        while(N > 0):
            patlu = patlu + 1
            N = N - 1
            pos = "p"
if pos == "m":
    print("MOTU")
else:
    print("PATLU")
print("\n")


# x=1
# j=1
# i=1
# n=int (input ())
# while x < n:
#           x=3*j
#           i+=1
#           j=j+i+1
# if x==n:
#     print ('motu')
# else:
#     print ('patlu')

# Patlu and Motu works in a building construction, they have to put some number of bricks N from one place to another, and started doing their work. They decided , they end up with a fun challenge who will put the last brick.
#
# They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.
#
# There are only N bricks, you need to help find the challenge result to find who put the last brick.
#
# Input:
#
# First line contains an integer N.
#
# Output:
#
# Output "Patlu" (without the quotes) if Patlu puts the last bricks ,"Motu"(without the quotes) otherwise.
#
# Constraints:
#
# 1 ≤ N ≤ 10000
#
# SAMPLE INPUT
# 13
# SAMPLE OUTPUT
# Motu
# Explanation
# Sample Explanation:
#
# 13 bricks are there :
#
# Patlu Motu
#
# 1 2
#
# 2 4
#
# 3 1 ( Only 1 remains)
#
# Hence, Motu puts the last one.