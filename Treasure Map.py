# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","️⬜️","️⬜️"]
row3 = ["⬜️","️⬜️","️⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#23
#Write your code below this row 👇

dikey = int(position[1])
yatay = int(position[0])

row = map[yatay-1]
row[dikey-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
