spaces =4
spaces2=4

for k in range(1,2):
    print(spaces2*" "+k*'*'+spaces2*" ")

for i in range(1,6):
    print(spaces*" "+(i*2)*"*"+spaces*" ")
    spaces = spaces-1

spaces1= 0

for j in range(5,0,-1):
    print((spaces*1)*" " + (j*2) * "*"+(spaces*1)*" ")
    spaces = spaces+1


for k1 in range(1,2):
    print(spaces2*" "+k1*'*'+spaces2*" ")