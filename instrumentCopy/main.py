import csv
import os
import random
import time
import requests
from lxml import etree

category = ['piano', 'keyboard', 'strings', 'guitar', 'drum-percussion', 'amplifier-audio']
piano_category = ['grandpiano', 'uprightpiano']
keyboard_category = ['digitalpiano', 'digitalkeyboard']
strings_category = ['violin', 'viola', 'cello']
guitar_category = ['ukulele', 'classicalguitar', 'acousticguitar', 'electricguitar', 'electricbass']
drum_category = ['electricdrum']
amplifier_category = ['guitarpedals', 'bassamlifier', 'edrumamplifier', 'guitaramplifier']
all_cate = list()
all_cate.append(piano_category)
all_cate.append(keyboard_category)
all_cate.append(strings_category)
all_cate.append(guitar_category)
all_cate.append(drum_category)
all_cate.append(amplifier_category)
print(all_cate)

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    url = "https://www.parsonsmusic.com.cn/"
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    with open('./inst.html', 'w', encoding='utf-8') as fp:
            fp.write((page_text))

    for i in range(6):
        url = "https://www.parsonsmusic.com.cn/" + category[i] + '.aspx'
        page_text = requests.get(url=url, headers=headers).text
        tree = etree.HTML(page_text)
        div_list = tree.xpath('/html/body/div[1]/div[5]/ul/li')
        for div in div_list:
            href1 = div.xpath('./a/@href')[0]
            print(href1)
            url1 = "https://www.parsonsmusic.com.cn" + href1
            page_text1 = requests.get(url=url1, headers=headers).text
            tree1 = etree.HTML(page_text1)
            div1_list = tree1.xpath('//div[@class="productlist loadlist"]/ul/li')
            name1 = href1.split('.')[0].split('/')[-1]
            path1 = './pics/' + name1
            if not os.path.exists(path1):
                os.mkdir(path1)
                print('Create')
            for div1 in div1_list:
                img1 = 'https://www.parsonsmusic.com.cn' + div1.xpath('./div[1]/p/a/img/@src')[0]
                alt1 = div1.xpath('./div[1]/p/a/img/@alt')[0]
                print(alt1)
                print(name1)
                img_name = alt1 + '.jpg'
                img_name = img_name.replace('/', '')
                img_path = 'pics/' + name1 + '/' + img_name
                print(img_path)
                img_data = requests.get(url=img1, headers=headers).content
                with open(img_path, 'wb') as fp:
                    fp.write(img_data)
                time.sleep(random.randint(1, 2) / 3)
            # name1 = href1.split('.')[0].split('/')[-1] + '.html'
            # with open(name1, 'w', encoding='utf-8') as fp:
            #     fp.write((page_text1))
            time.sleep(random.randint(2, 5))
    print('PyCharm')

