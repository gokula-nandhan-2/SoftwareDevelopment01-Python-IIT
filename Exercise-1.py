# Exercise-1

# 1
nums = [1,2,4,15]

nums[len(nums)-1] = 16
print(nums)

nums.insert(3,8)
print(nums)

nums.append(32)
print(nums)

print(sum(nums))

reversed(nums)
print(nums)
print("\n")


# 2
text = "concatenation"
print(text[4])
print(text[-3])
print(text[0:3])
print(text[3:6])
print(text[-6:])
print("\n") 


# 3,4
r = range(1, 10)
print(r)          
print(type(r))

r = list(r)
print(r)
print(type(r))
print("\n")     


# 5
evenNumsBelow25 = list(range(2, 25, 2))
print(evenNumsBelow25)