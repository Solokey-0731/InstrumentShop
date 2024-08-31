import os
import random

str0 = "INSERT INTO `shangpinxinxi` (`id`, `addtime`, `shangpinmingcheng`, `shangpinfenlei`, `tupian`, `biaoqian`, `pinpai`, `shangpinxiangqing`, `clicktime`, `clicknum`, `price`) VALUES\n"
with open('1.txt', 'a+') as fp:
    fp.write(str0)

root_path = './pics/'
fold_list = os.listdir(root_path)
index = 1
for fold in fold_list:
    pic_path = root_path + fold + '/'
    pic_list = os.listdir(pic_path)
    print(pic_list)
    time = "\'2024-08-31 20:00:00\',"
    for pic_category in pic_list:
        img_path = pic_path + pic_category
        img_list = os.listdir(img_path)
        for img in img_list:
            price = random.randint(200000, 9000000) / 100
            price = str(price)
            str1 = '(' + str(index) + "," + time + "\'" +  img.split(".jpg")[0] + "\'," + "\'" + fold + "\'," + "\'" \
                + 'http://localhost:8080/wangshangshangchengB/upload/' + img_path.split("./")[1] + "/" + img + "\'," + "\'" + pic_category + "\'," + "\'" + img.split(' ')[0] + "\'," \
                + "\'" + img.split(".jpg")[0] + "\'," + time + '1,' + price + ')'
            if index != 221:
                str1 += ",\n"
            index += 1
            with open('1.txt', 'a+') as fp1:
                 fp1.write(str1)

with open('1.txt', 'a+') as fp2:
    fp2.write(';')