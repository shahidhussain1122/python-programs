# write a python program that accepts an integer (n) and computes that value of n+nn+nnn
a = int(input("Enter an integer"))
n1 = int("%s" %a)
n2 = int("%s%s" %(a,a))
n3 = int("%s%s%s" %(a,a,a))
print(n1+n2+n3)

# Explanatio
# a = 2
# n1 = 2
#n2 = 22
# n3 = 222
# 2+22+222