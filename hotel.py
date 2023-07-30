#Laço for

for i in range(21):
    if i == 0:
        print("Térreo")

    elif i != 13:
        print("Andar " , i)

#Laço while

i = 0
while(i <= 20):
    if i == 0:
        print("Térreo")

    elif(i != 13):
        print("Andar " , i)  
    i = i + 1

#Laço while true

i = 0
while True:
    if i == 0:
        print("Térreo")

    elif i != 13:
        print("Andar " , i)

    i = i + 1
    if(i == 21):
        break

#Ordem descrescente

for i in range(20,-1,-1):
    if i == 0:
        print("Térreo")
    elif i != 13:
        print("Andar " , i)
