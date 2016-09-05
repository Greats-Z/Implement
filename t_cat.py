#灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像

from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度分别映射到ascii_char的字符上
def get_char(r,b,g,alpha=256):#alpha是什么鬼
    if (alpha == 0) or (r>240 and b>240 and g>240):# 白色或者png底色置为空格
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    a = int(gray/unit)
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    imgname = input('输入文件名')
    image = Image.open(imgname)
    WIDTH, HEIGHT = image.size
##    WIDTH = int(WIDTH/10)
##    HEIGHT = int(HEIGHT/10)
    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*image.getpixel((j,i)))
        txt += '\n'


    print(txt)
    filename = imgname.split('.')[0] + '.txt'
    #输出到文件
    with open(filename,'w') as f:
        f.write(txt)

