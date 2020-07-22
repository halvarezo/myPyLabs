blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
height = 0
inlayer = 1
while inlayer <= blocks:
    # The body of the while loop.
    height += 1
    inlayer = height*(height+1)/2
    
height -= 1
   
#	

print("The height of the pyramid:", height)