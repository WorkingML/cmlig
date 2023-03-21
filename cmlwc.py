from PIL import Image
import wordcloud
import jieba
import easygui
import os

if easygui.ynbox('欢迎使用cmlwc词云生成器\n本软件可以将您输入的文本转换为词云图', '欢迎', ('开始使用', '回到主菜单')):
    while True:
        easygui.msgbox('请在弹出的命令框内输入文本（可粘贴，内容不可过少）\n！！！目前只支持中文和英文！！！','输入文本','输入')
        print('请输入在此处：')
        text = input()

        if easygui.ynbox('刚刚输入的文本是否包含中文？','语言辨别',('是','否')):
            lst = jieba.lcut(text)
            m = ' '.join(lst)
        else:
            m = text

        sto = []
        if easygui.ynbox('是否添加屏蔽词（您不希望在此词云图中出现的词语）？', '添加屏蔽词', ('是', '否')):

            count = 0
            flag = True
            while flag:
                count += 1
                easygui.msgbox('请在弹命令框内输入第'+str(count)+'个屏蔽词','输入屏蔽词', '输入')
                sto.append(input('请输入第'+str(count)+'个屏蔽词:'))
                if easygui.ynbox('是否再添加一个屏蔽词?', '添加屏蔽词', ('是', '否')):
                    flag = True
                else:
                    if easygui.ynbox('是否确认添加完成?', '添加屏蔽词', ('是', '否')):
                        flag = False
                    else:
                        flag = True

        easygui.msgbox('在点击“确定”后，在命令框输入你想要的背景颜色\n（我们会提供备选方案）','确定背景颜色', '输入')
        print('''预选方案：
        black——黑色
        white——白色
        brown——棕色
        blue——蓝色
        pink——粉色
        gold——金色
        若要选择一种颜色，输入该颜色所代表的英语单词即可
        （理论上任何一个你知道的颜色单词均可，若报错则表示不支持）
        ''')
        bjys = input()

        easygui.msgbox('在点击“确定”后，在命令框输入你想要的字体色系\n（我们会提供备选方案）','输入字体色系','输入')
        print('''预选方案：
        gnuplot
        plasma
        prism
        hsv
        rainbow
        Blues          （不是蓝调！！！）
        若要选择一种色系，输入该色系所代表的英语单词即可
        （这些词语翻译很奇怪，这里不进行翻译）
        （注意大小写！）
        ''')
        ztsx = input()

        flag = True
        while flag:
            flag = True
            easygui.msgbox('在点击“确定”后，输入将输出的图片的大小','输入图片大小','输入')
            wid = int(input('输入图片的宽:'))
            hei = int(input('输入图片的高:'))
            if int(wid)*int(hei) > 2560*1440:
                if easygui.ynbox('检测到您输入的分辨率像素总数大于2560*1440，制作过程可能较慢，是否继续?', '图片大小确认', ('是', '否')):
                    flag = False
            else:
                flag = False

        easygui.msgbox('在点击“确定”后，输入此词云图的名称','输入图片名称','输入')
        nam = input('输入图片名:')

        if easygui.ynbox('保存为JPG格式还是PNG格式？','保存格式',('JPG','PNG')):
            form = '.jpg'
        else:
            form = '.png'

        easygui.msgbox('准备就绪，可以开始制作', '准备制作', '开始制作')

        print('开始制作词云，请稍候...')
        w = wordcloud.WordCloud(
            width=wid,
            height=hei,
            font_path='simhei.ttf',
            # 使用参数background_color设置图片背景
            # 使用参数colormap设置字体色系
            background_color = bjys,
            colormap = ztsx,
            stopwords = sto
        )
        w.generate(m)
        w.to_file(nam+form)

        if easygui.ynbox('词云图片已生成,已保存在软件目录,是否展示图片？','展示图片',('是','否')):
            p = Image.open(nam+form)
            p.show()
            print('图片展示完成')
        if easygui.ynbox('感谢使用，是否退出？','选择',('回到主菜单','继续制作')):
            break
        else:
            continue






