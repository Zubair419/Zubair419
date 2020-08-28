print ('''


 __                  __   __                 __       __                               
|  \                |  \ |  \               |  \     /  \                              
| $$       ______  _| $$_| $$ _______       | $$\   /  $$  ______  __     __   ______  
| $$      /      \|   $$ \\$ /       \      | $$$\ /  $$$ /      \|  \   /  \ /      \ 
| $$     |  $$$$$$\\$$$$$$  |  $$$$$$$      | $$$$\  $$$$|  $$$$$$\\$$\ /  $$|  $$$$$$\
| $$     | $$    $$ | $$ __  \$$    \       | $$\$$ $$ $$| $$  | $$ \$$\  $$ | $$    $$
| $$_____| $$$$$$$$ | $$|  \ _\$$$$$$\      | $$ \$$$| $$| $$__/ $$  \$$ $$  | $$$$$$$$
| $$     \\$$     \  \$$  $$|       $$      | $$  \$ | $$ \$$    $$   \$$$    \$$     \
 \$$$$$$$$ \$$$$$$$   \$$$$  \$$$$$$$        \$$      \$$  \$$$$$$     \$      \$$$$$$$
                                                                                       
                                                                                       
Welcome to our services   

Kindly select your apartment size from the following options:

1. 1K
2. 2DK
3. 2LDK
4. 3DK
                                               
''')

x = input ("answer: ")
x = int (x)


y = input ("How far do you want to move from your current location? ")
y = float (y)

v = input ("What is the total volume of your equipments in metre cube? ")
v = float (v)

w = input ("What is the total weight of your equipments in kg? ")
w = float (w)

if (v>20):
    print ("Truck size is large: ")
elif (w>100):
    print ("Truck size is large:")
else:
    print ("Truck size is small")

t = x*10000 + y*1000 + v*1000 + w*1000

line = "Your total cost is {} yen".format (t)


print (line) 



    
