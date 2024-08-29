from PIL import Image, ImageDraw, ImageFont

# get an image
with Image.open("C:/Users/samoe/Desktop/watermark_test/watermark_test.PNG").convert("RGBA") as pic:

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", pic.size, (255, 0, 0, 0))

    # get a font
    fnt = ImageFont.truetype("arial.ttf", 70)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity


    x, y = 10, 10
    width, height = pic.size
    step_x, step_y = 400, 90

    for i in range(0, height, step_y):
        for j in range(0, width, step_x):
            d.text((j, i), "Watermark", font=fnt, fill=(255, 255, 255, 40))




    out = Image.alpha_composite(pic, txt)

    out.save('C:/Users/samoe/Desktop/watermark_test/watermark_done.png')

    out.show()