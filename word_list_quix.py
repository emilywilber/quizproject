with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()

print(words[0:10])
print()

count = 0
for w in words:
    count += 1
print(count)

count = 0
for w in words:
    if len(w) == 5:
        count += 1
print(count)

count = 0
for w in words:
    if len(w) > 7:
        count +=1
print(count)

count = 0
for w in words:
    if w[0] == w[-1]:
        count += 1
print(count)

bigboy = 0
for w in words:
    if bigboy < len(w):
        bigboy = len(w)
print(bigboy)

count = 0
for w in words:
    count += len(w)
print(count)

count = 370099
for i in words:
    if 'e' in i:
        count -= 1
print(count)

'''
count = 0
for w in words:
    if 'q' in w:
        count += 1
for w in words:
    if 'qu' in w:
        count -= 1
print(count)

count = 0
def find_q(w):
    for w in words:
        if 'q' in w:
            count += 1
        elif 'qu' in w:
            count -= 1
    return count
print(count)


count = 0
for w in words: 
     if 'q' in w and not 'u' in w:
         count += 1
print(count)
'''
count = 0
for w in words:
    for i in w:
        if i == q and i+1 != u:
            count += 1
        else:
            
