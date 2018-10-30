# !/usr/bin/env python
# -*- coding:utf-8 -*-
#                                                           #
#                      _oo0oo_                              #
#                     o8888888o                             #
#                     88" . "88                             #
#                     (| -_- |)                             #
#                      0\ = /0                              #
#                  ____/'---'\____                          #
#                .   ' \\| |// '   .                        #
#               /   \\||| : |||//   \                       #
#              /  _||||| -:- |||||_  \                      #
#                 | | \\\ - /// | |                         #
#              |  \_| ''\---/'' | |                         #
#               \  .-\__ '-' ___/-.  /                      #
#             ___'. .' /--.--\ '. . __                      #
#          ."" '< '.___\_<|>_/___.' >'""                    #
#         | | : '- \'.;'\ _ /';.'/ - ' : | |                #
#           \ \ '-. \_ __\ /__ _/  .-' / /                  #
#   ======'-.____'-.___\_____/___.-'____.-'======           #
#                      '=---='                              #
#.....................................................      #
#    佛祖镇楼                       BUG辟易                 #
#   佛曰：                                                  #
#       写字楼里写字间，写字间里程序员；                    #
#       程序人员写程序，又拿程序换酒钱。                    #
#       酒醒只在网上坐，酒醉还来网下眠；                    #
#       酒醉酒醒日复日，网上网下年复年。                    #
#       但愿老死电脑间，不愿鞠躬老板前；                    #
#       奔驰宝马贵者趣，公交自行程序员。                    #
#       别人笑我忒疯癫，我笑自己命太贱；                    #
#       不见满街漂亮妹，哪个归得程序员？                    #
#                                                           #

from PIL import Image


def pic2ascii(pic, asciis, zoom, vscale):
    img = Image.open(pic)
    # 打开图片并转换为灰度模式
    out = img.convert("L")
    # 获取图片的宽度和高度
    width, height = out.size
    # 由于字符的宽度并不会等于高度，所以需要进行调整
    out = out.resize((int(width * zoom), int(height * zoom * vscale)))
    ascii_len = len(asciis)
    texts = ''

    for row in range(out.height):
        for col in range(out.width):
            gray = out.getpixel((col, row))
            texts += asciis[int((gray / 255) * (ascii_len - 1))]
        texts += '\n'

    return texts


def main():
    pic = input("请输入待转换的图片名称：")
    # 10个字符表示按“灰度级别”从高到低排序
    asciis = "@%#*+=-:. "
    # 设置缩放系数
    zoom = 0.5
    # 设置垂直比例系数
    vscale = 0.75
    texts = pic2ascii(pic, asciis, zoom, vscale)

    with open("ascii.txt", "w") as file:
        file.write(texts)


if __name__ == "__main__":
    main()
