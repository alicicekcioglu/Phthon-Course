def double(x):
    return x*2

map(double,[1,2,3,4,5,6,7]) # her bir liste elemanına double fonksiyonunu uyguluyor.

a = list(map(double,[1,2,3,4,5,6,7]))
print(a)

map(lambda x: x*2,(1,2,3,4,5,6,7)) #lamda ile yazımı
print(list(map(lambda x: x*2,(1,2,3,4,5,6,7))))

# ne kadar işlem yapacaksak o kadar liste/demet ekleyebiliriz.

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

map(lambda x,y: x*y,liste1,liste2,)
print(list(map(lambda x,y: x*y,liste1,liste2,)))

map(lambda x,y,z: x*y+z,liste1,liste2,liste3)
print(list(map(lambda x,y,z: x*y+z,liste1,liste2,liste3)))