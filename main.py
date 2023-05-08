def p1():
    from PIL import Image
    name = "Cat.jpg"
    with Image.open(name) as img:
        img.load()

    img.show()
    width, height = img.size
    format = img.format
    mode = img.mode
    print("Ширина: ", width)
    print("Высота: ", height)
    print("Формат: ", format)
    print("Цветовая модель: ", mode)

def p2():
    from PIL import Image
    name = "Cat.jpg"
    with Image.open(name) as img:
        img.load()

    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("Cat2.jpg")
    new_img.show()

    new_img = img.rotate(180)
    new_img.save("Cat3.jpg")
    new_img.show()

def p22():
    from PIL import Image
    img = Image.open("Cat.jpg")
    new_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.save("Cat4.jpg")
    new_img.show()

def p3():
    from PIL import Image, ImageFilter
    name = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

    for file in name:
        with Image.open(file) as img:
            img.load()
        new_img = img.filter(ImageFilter.CONTOUR)
        new_img.show()
        new_img.save("grrr" + file)

def p4():
    from PIL import Image
    name = "watermark.png"
    with Image.open(name) as img_name:
        img_name.load()

    img_name = Image.open(name)
    img_name = img_name.resize((img_name.width // 1, img_name.height // 1))

    name2 = "Cat.jpg"
    with Image.open(name2) as img:
        img.load()

    img.paste(img_name, (60, 30), img_name)
    img.save("Watermark_Cat.jpg")

p22()
