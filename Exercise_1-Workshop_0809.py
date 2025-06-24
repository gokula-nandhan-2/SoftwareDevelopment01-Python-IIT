#1
pun = 'Eating a clock is very time consuming!!!'
print(pun)
#2
print(pun[23:])
#3
pun = pun.rstrip('!')
print(pun)
#4
print(pun.count('i'))
#5
punWords = pun.lower().split()
print(punWords)
print('\n')

#6
scores = {'Mary' : [22, 23, 36], 'Fred' : [20, 21, 29]}

#7
print(scores['Mary'])
#8
print(scores['Fred'][1])
#9
scoreKeys = scores.keys()
print(scoreKeys)
#10
scores['Jane'] = [21, 24, 30]
#11
scores['Fred'][2] = 39
print(scores)

#12
HDs = [name for name in scores if sum(scores[name]) >= 80]
print(HDs)
print('\n')

#13,14,15
set1 = {4,2,6,3,6,2,7}
# set2 = set(9,1,0,2,4,1,4,6)
set2 = set([9,1,0,2,4,1,4,6])
print(set1)
print(set2)

#16
print(set1 | set2)
print(set1 & set2)