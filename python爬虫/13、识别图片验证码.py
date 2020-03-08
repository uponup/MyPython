
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

captcha = Image.open("./python爬虫/1024.png")
result = pytesseract.image_to_string(captcha)
print(result)


captcha_1 = Image.open("./python爬虫/1024_1.png")
result = pytesseract.image_to_string(captcha_1)
print(result)


# 这张图处理起来就出错了，因为是彩色图片，噪点太多
captcha_2 = Image.open("./python爬虫/1024_2.png")
result = pytesseract.image_to_string(captcha_2)
print(result)

# 1、我们首先需要将上述图片灰度处理一下，
# result = captcha_2.convert('L')
# result.show()

# 2、其次还需要对其进行二值化


# 完成方法：先灰度化，然后在进行二值化
def convert_img(image, threshold):
    img = image.convert('L')
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img
img = convert_img(captcha_2, 140)
img.show()

result = pytesseract.image_to_string(img)
print(result)
