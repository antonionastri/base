frutta = ["mela", "pera","mango"]

for fr in frutta:
    print(fr)
    print("----")

for x in range(10):
    print("gigi " + str(x))
    
for i in range(3,10):
    print(i)
    
print("-------------------")

for i in range(3,10, 2):
    print(i)
    

# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for f in fruits:
    if "a" in f:
        newlist.append(f)

print(newlist)

# alternativo al ciclo sopra (lezione n.3)
newlist = [f.upper() for f in fruits if "a" in f]


    
# while
i = 1
while i < 6:
    print(i)
    i += 1
    
    
# break
i = 1
    
while i < 6:
    print(i)
    if i == 3:
        break
    
    i += 1
    
# continue

i = 1
    
while i < 6:
    i += 1 
    
    if i == 3:
        continue
       
    print(i)
    
# print("CTRL+C per uscire..")    
# while True:
#     i += 1
    
