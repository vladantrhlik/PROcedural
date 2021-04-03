from PIL import Image, ImageDraw, ImageFont

fnt = ImageFont.truetype('arial.ttf', 40)

W, H = (50,50)

im = Image.new("RGBA",(W*10,H),"white")
draw = ImageDraw.Draw(im)

for i in range(10):
    msg = str(i)
    w, h = draw.textsize(msg, font=fnt)
    draw.text((i*W+(W-w)/2,(H-h)/2), msg, fill="black", font=fnt)

im.save("hello.png", "PNG")
