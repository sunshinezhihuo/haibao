import random,qrcode
from PIL import Image, ImageDraw, ImageFont
'''
pip install qrcode
pip install pillow
https://www.jianshu.com/p/8ba0c3e2381b
https://blog.csdn.net/mi2006/article/details/106073963
https://www.cnblogs.com/win-lin08/p/10951066.html
https://www.cnblogs.com/gdjlc/archive/2019/09/01/11444132.html
'''

def rand_name():
    xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖控蛮荆而引瓯越物华天宝龙光射牛斗之墟人杰地灵徐孺饯子'
    name = random.choice(xing)+''.join(random.sample(ming,2))
    if name not in names:
        names.append(name)
        return name
    return None

def get_qrcode(name):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4
    )
    qr.add_data(name)
    qr.make(fit=True)
    name_code = qr.make_image()
    name_code = name_code.resize((210, 210), Image.ANTIALIAS)
    return name_code

def get_pic(img,name):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype("simhei.ttf", size=100)
    text_size = myfont.getsize(name)
    text_coordinate = int((im.size[0]-text_size[0])/2), int((im.size[1]-text_size[1])/2)*0.8
    draw.text(text_coordinate, name, font=myfont, fill='black')
    line_size = (text_coordinate[0],text_coordinate[1]+text_size[1]*1.2,
                 text_coordinate[0]+text_size[0],text_coordinate[1]+text_size[1]*1.2)
    draw.line(line_size, fill = (255,0,0), width = 5)
    return img

if __name__=='__main__':
    im = Image.open(r"./55d61cfc9cc25b143ddf8d6853c8be65.jpg")
    num = 20
    names = []
    name_list = ["张三", "李四", "王五", "赵六", "黄一"]
    num = len(name_list)
    for i in range(num):
        # name = rand_name()
        # while name is None:
        #     name = rand_name()

        name = name_list[i]
        print(f'海报--{name}--正在生成，当前进度{round((i+1)/num,2)}')
        im_copy = get_pic(im.copy(),name)
        im_copy.paste(get_qrcode(name),(230,2080))
        # im_copy.show()
        im_copy.save(f"./result/{name}.png", 'PNG')
