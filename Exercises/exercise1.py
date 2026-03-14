# you = 0
# me = []
# while you < 21:
#     me.append(you)
#     print(me)
#     you+=1

# import keyword
# print(keyword.kwlist)

#ns1 = [2, 3, 7, 8, 9, 1]
#ns2 = []
# for i in ns1:
#     ns2.append(i * 2)
a = 1
while a < 11:
   # print(a)
    a+=1
Sentence = "This boy is doing WELL."
Sen = "Okay now"
# METHODSS IN PYTHON
Lower = Sentence.lower()
print(Lower)

G = "FM"
print(G.zfill(4))
Upper = Sentence.upper()
print(Upper)

import keyword
for R in keyword.kwlist:
    Y = len(R)
    print(R)
    print(Y)
W = Sentence.split()
P = len(W)
print(W)
print(P)

con = Sentence.join(Sen)
print(f'{con}',)