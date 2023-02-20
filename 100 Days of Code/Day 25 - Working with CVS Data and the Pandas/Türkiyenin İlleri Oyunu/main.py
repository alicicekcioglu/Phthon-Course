import turtle
import pandas

screen = turtle.Screen()

screen.title("Türkiyenin İlleri")

# Gif dosyasını turtle'a ekleme
image = "6e258d2d2790db9adf0961bc3a12d45a.gif"
turtle.addshape(image)
turtle.shape(image)

ili_sor = screen.textinput(title="İli tahmin et", prompt="Şehrin adı nedir?")
print(ili_sor)


# görsele tıklayınca x,y cordinatını çıktı olarak alma
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onclick(get_mouse_click_coor)

turtle.mainloop()
