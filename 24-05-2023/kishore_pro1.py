l=[10,20,[30,40],50]
print(l[0])
print(l[1])
print(l[2])
print(l[2][0])
print(l[2][1])
print(l[:2] + [l[2][0]])
print([l[0], l[1], l[2][0]])
print( l[:2] + l[2][:1])
print(l[:2] + l[2][:-1])