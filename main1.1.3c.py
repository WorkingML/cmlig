from PIL import Image
import wordcloud
import jieba
import easygui
import matplotlib.pyplot as plt
import winsound

print('''CML Image generator alpha 1.1.3 compatibility edition x86 
Copyright © 2022-2023  CreamML. All rights reserved.''')


while True:
    winsound.PlaySound('C:\Windows\Media\Windows Background.wav',flags = 1)
    a = easygui.buttonbox(
        '''
        
        
        欢迎使用cml图片文件生成程序，请选择一个选项：
        
        
        
''',
        'WELCOME-CMLIG x86 Copyright © 2022-2023 CreamML. All rights reserved.',
        choices =('退出','折线图生成','条形图生成','饼图生成','词云生成','说明书'),
        )
    if a == '词云生成':
        if easygui.ynbox('''欢迎使用cml词云生成器\n本软件可以将您输入的文本转换为词云图
                          
                                                  
                                                  
                                                  
                                                  
                                                  
                                                                                            ''', '欢迎 - cmlwc v1.1',
                         ('开始使用', '回到主菜单')):
            while True:
                
                text = easygui.enterbox('请输入文本（建议粘贴，内容不可过少）\n！！！目前只支持中文和英文！！！',
                               '输入文本')

                if easygui.ynbox('刚刚输入的文本是否包含中文？', '语言辨别', ('是', '否')):
                    lst = jieba.lcut(text)
                    m = ' '.join(lst)
                else:
                    m = text

                sto = ['']
                if easygui.ynbox('是否添加屏蔽词（您不希望在此词云图中出现的词语）？', '添加屏蔽词', ('是', '否')):

                    sto = []
                    count = 0
                    flag = True
                    while flag:
                        count += 1
                        sto.append(easygui.enterbox('请在弹命令框内输入第' + str(count) + '个屏蔽词', '输入屏蔽词'))
                        if easygui.ynbox('是否再添加一个屏蔽词?', '添加屏蔽词', ('是', '否')):
                            flag = True
                        else:
                            if easygui.ynbox('是否确认添加完成?', '添加屏蔽词', ('是', '否')):
                                flag = False
                            else:
                                flag = True

                
                bjys = easygui.buttonbox('请选择一个背景颜色\n颜色翻译（自左到右）：黑色，白色，棕色，蓝色，粉色，金色', '确定背景颜色',choices=('black','white','brown',
                                                                 'blue','pink','gold','其他（自行输入）'))
                if bjys == '其他（自行输入）':
                    easygui.enterbox('请输入自定义颜色\n（理论上任何一个你知道的颜色单词均可，若报错则表示不支持）','输入颜色')

                ztsx = easygui.buttonbox('请选择一个字体色系', '确定字体色系',choices=('gnuplot','plasma','prism',
                                                                 'hsv','rainbow','Blues','其他（自行输入）'))
                if ztsx == '其他（自行输入）':
                    easygui.enterbox('请输入自定义色系','输入色系')
               

                flag = True
                while flag:
                    flag = True
                    easygui.msgbox('在点击“确定”后，输入将输出的图片的大小', '输入图片大小', '输入')
                    wid = int(easygui.enterbox('请输入图片的宽','输入图片的宽'))
                    hei = int(easygui.enterbox('请输入图片的高','输入图片的高'))
                    if int(wid) * int(hei) > 2560 * 1440:
                        winsound.PlaySound('C:\Windows\Media\Windows Critical Stop.wav',flags = 1)
                        if easygui.ynbox('检测到您输入的分辨率像素总数大于2560*1440，制作过程可能较慢，是否继续?',
                                         '图片大小确认', ('是', '否')):
                            flag = False
                    else:
                        flag = False

                nam = easygui.enterbox('请输入此词云图的名称', '输入图片名称')
                

                if easygui.ynbox('保存为JPG格式还是PNG格式？', '保存格式', ('JPG', 'PNG')):
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
                    background_color=bjys,
                    colormap=ztsx,
                    stopwords=sto
                )
                w.generate(m)
                w.to_file(nam + form)

                winsound.PlaySound('C:\Windows\Media\Windows Background.wav',flags = 1)
                if easygui.ynbox('词云图片已生成,已保存在软件目录,是否展示图片？', '展示图片', ('是', '否')):
                    p = Image.open(nam + form)
                    p.show()
                    print('图片展示完成')
                if easygui.ynbox('感谢使用，是否退出？', '选择', ('回到主菜单', '继续制作')):
                    break
                else:
                    continue





    elif a == '饼图生成':


        plt.rcParams['font.sans-serif'] = 'simhei'

        if easygui.ynbox('''
欢迎使用cml饼图生成器
本程序可以将你的数据转换为饼图


                                          ''', '欢迎 - cmlpc v1.1', ('开始使用', '回到主菜单')):

            while True:

                mode = easygui.buttonbox('请选择功能模式', '选择模式',
                                         choices=('极简模式', '简洁模式', '一般模式', '高级模式', '模式说明'))
                if mode == '高级模式':
                    flag = True
                    while flag:
                        easygui.msgbox('请输入数据\n格式：a b c d e ... (其中a等字母指代数字)', '输入数据', '确定')
                        data = easygui.enterbox('请输入数据','输入数据')
                        d1 = data.split()
                        w1 = []
                        easygui.msgbox('请为数据匹配标签\n格式：a b c d e ... (其中a等字母指代标签)', '输入标签', '确定')
                        word = easygui.enterbox('请为数据匹配标签','匹配标签')
                        w1 = word.split()
                        if len(w1) == len(d1):
                            flag = False
                        else:
                            winsound.PlaySound('C:\Windows\Media\Windows Critical Stop.wav',flags = 1)
                            easygui.msgbox('数据数与标签数不一致！(E1)', '请重新输入', '确定')

                    auto = easygui.buttonbox('是否显示百分占比值？', '显示占比值',
                                             choices=('以整数+百分号显示', '以浮点数(小数)+百分号显示'))
                    if auto == '以整数+百分号显示':
                        atp = '%d%%'
                    if auto == '以浮点数(小数)+百分号显示':
                        atp = '%f%%'

                    rad = easygui.buttonbox('请设置饼图在输出图片中的大小', '设置大小',
                                            choices=('小(0.5)', '中(1)', '大(1.5)'))
                    if rad == '小(0.5)':
                        rdu = 0.5
                    if rad == '中(1)':
                        rdu = 1
                    if rad == '大(1.5)':
                        rdu = 1.5

                    color = []
                    easygui.msgbox('请自定义饼图颜色', '自定义颜色', '确定')
                    easygui.msgbox(
                        '检测到您输入了' + str(len(d1)) + '个数据，所以请输入' + str(len(d1)) + '种颜色所对应的英语单词',
                        '输入颜色', '确定')
                    for i in range(len(d1)):
                        color.append(easygui.enterbox('请输入第' + str(i + 1) + '种颜色:','输入颜色'))

                    easygui.msgbox('请输入输出文件的宽与高（像素）\ntips:输入文字会报错', '输入大小', '开始输入')
                    # 1英寸=100像素

                    wid = easygui.enterbox('请在此处输入宽:','输入宽')
                    hei = easygui.enterbox('请在此处输入高:','输入高')
                    wid = int(wid)
                    hei = int(hei)

                    plt.figure(figsize=(wid / 100, hei / 100))
                    plt.pie(d1, labels=w1, radius=rdu, colors=color, autopct=atp)

                    easygui.msgbox('准备就绪，可以开始制作', '准备制作', '开始制作')
                    
                    winsound.PlaySound('C:\Windows\Media\Windows Background.wav',flags = 1)
                    easygui.msgbox('我们即将展示你的图片\n随后点击弹出窗口左下角以保存', '展示图片', '展示')
                    plt.show()

                    if easygui.ynbox('感谢使用，是否退出？', '选择', ('回到主菜单', '继续制作')):
                        break
                    else:
                        continue

                elif mode == '极简模式':

                    easygui.msgbox('请输入数据\n格式：a b c d e ... (其中a等字母指代数字)', '输入数据', '确定')
                    data = easygui.enterbox('请在此处输入数字:', '输入数字')
                    d1 = data.split()

                    rad = easygui.buttonbox('请设置饼图在输出图片中的大小', '设置大小',
                                            choices=('小(0.5)', '中(1)', '大(1.5)'))
                    if rad == '小(0.5)':
                        rdu = 0.5
                    if rad == '中(1)':
                        rdu = 1
                    if rad == '大(1.5)':
                        rdu = 1.5

                    easygui.msgbox('请输入输出文件的宽与高（像素）\ntips:输入文字会报错', '输入大小', '开始输入')
                    # 1英寸=100像素

                    wid = easygui.enterbox('请在此处输入宽:','输入宽')
                    hei = easygui.enterbox('请在此处输入高:','输入高')
                    wid = int(wid)
                    hei = int(hei)

                    plt.figure(figsize=(wid / 100, hei / 100))
                    plt.pie(d1, radius=rdu)
                    
                    easygui.msgbox('准备就绪，可以开始制作', '准备制作', '开始制作')

                    winsound.PlaySound('C:\Windows\Media\Windows Background.wav',flags = 1)
                    easygui.msgbox('我们即将展示你的图片\n随后点击弹出窗口左下角以保存', '展示图片', '展示')
                    plt.show()

                    if easygui.ynbox('感谢使用，是否退出？', '选择', ('回到主菜单', '继续制作')):
                        break
                    else:
                        continue

                elif mode == '一般模式':
                    flag = True
                    while flag:
                        easygui.msgbox('请输入数据\n格式：a b c d e ... (其中a等字母指代数字)', '输入数据', '确定')
                        data = easygui.enterbox('请输入数据','输入数据')
                        d1 = data.split()
                        w1 = []
                        easygui.msgbox('请为数据匹配标签\n格式：a b c d e ... (其中a等字母指代标签)', '输入标签', '确定')
                        word = easygui.enterbox('请为数据匹配标签','匹配标签')
                        w1 = word.split()
                        if len(w1) == len(d1):
                            flag = False
                        else:
                            winsound.PlaySound('C:\Windows\Media\Windows Critical Stop.wav',flags = 1)
                            easygui.msgbox('数据数与标签数不一致！(E1)', '请重新输入', '确定')

                    auto = easygui.buttonbox('请选择百分占比值显示方式', '显示占比值',
                                             choices=('以整数+百分号显示', '以浮点数(小数)+百分号显示'))
                    if auto == '以整数+百分号显示':
                        atp = '%d%%'
                    if auto == '以浮点数(小数)+百分号显示':
                        atp = '%f%%'

                    rad = easygui.buttonbox('请设置饼图在输出图片中的大小', '设置大小',
                                            choices=('小(0.5)', '中(1)', '大(1.5)'))
                    if rad == '小(0.5)':
                        rdu = 0.5
                    if rad == '中(1)':
                        rdu = 1
                    if rad == '大(1.5)':
                        rdu = 1.5

                    easygui.msgbox('请输入输出文件的宽与高（像素）\ntips:输入文字会报错', '输入大小', '开始输入')
                    # 1英寸=100像素

                    wid = easygui.enterbox('请在此处输入宽:','输入宽')
                    hei = easygui.enterbox('请在此处输入高:','输入高')
                    wid = int(wid)
                    hei = int(hei)

                    plt.figure(figsize=(wid / 100, hei / 100))
                    plt.pie(d1, labels=w1, radius=rdu, autopct=atp)
                    
                    easygui.msgbox('准备就绪，可以开始制作', '准备制作', '开始制作')
                    
                    winsound.PlaySound('C:\Windows\Media\Windows Background.wav',flags = 1)
                    easygui.msgbox('我们即将展示你的图片\n随后点击弹出窗口左下角以保存', '展示图片', '展示')
                    plt.show()

                    if easygui.ynbox('感谢使用，是否退出？', '选择', ('回到主菜单', '继续制作')):
                        break
                    else:
                        continue

                if mode == '简洁模式':

                    flag = True
                    while flag:
                        easygui.msgbox('请输入数据\n格式：a b c d e ... (其中a等字母指代数字)', '输入数据', '确定')
                        data = easygui.enterbox('请输入数据','输入数据')
                        d1 = data.split()
                        w1 = []
                        easygui.msgbox('请为数据匹配标签\n格式：a b c d e ... (其中a等字母指代标签)', '输入标签', '确定')
                        word = easygui.enterbox('请为数据匹配标签','匹配标签')
                        w1 = word.split()
                        if len(w1) == len(d1):
                            flag = False
                        else:
                            winsound.PlaySound('C:\Windows\Media\Windows Critical Stop.wav',flags = 1)
                            easygui.msgbox('数据数与标签数不一致！(E1)', '请重新输入', '确定')

                    rad = easygui.buttonbox('请设置饼图在输出图片中的大小', '设置大小',
                                            choices=('小(0.5)', '中(1)', '大(1.5)'))
                    if rad == '小(0.5)':
                        rdu = 0.5
                    if rad == '中(1)':
                        rdu = 1
                    if rad == '大(1.5)':
                        rdu = 1.5

                    easygui.msgbox('请输入输出文件的宽与高（像素）\ntips:输入文字会报错', '输入大小', '开始输入')
                    # 1英寸=100像素

                    wid = easygui.enterbox('请在此处输入宽:','输入宽')
                    hei = easygui.enterbox('请在此处输入高:','输入高')
                    wid = int(wid)
                    hei = int(hei)

                    plt.figure(figsize=(wid / 100, hei / 100))
                    plt.pie(d1, radius=rdu, labels=w1)

                    easygui.msgbox('准备就绪，可以开始制作', '准备制作', '开始制作')
                    
                    winsound.PlaySound('C:\Windows\Media\Windows Background.wav',flags = 1)
                    easygui.msgbox('我们即将展示你的图片\n随后点击弹出窗口左下角以保存', '展示图片', '展示')
                    plt.show()

                    if easygui.ynbox('感谢使用，是否退出？', '选择', ('回到主菜单', '继续制作')):
                        break
                    else:
                        continue

                if mode == '模式说明':
                    easygui.msgbox('''
模式说明

极简模式——仅包含图像主体

简洁模式——在前一个模式的基础下可以加入标签

一般模式——默认以及推荐模式,在前一个模式的基础下可以加入百分比

高级模式——不推荐新手使用此模式,在前一个模式的基础下可以自定义图像颜色        



                                       ''', '模式说明', '确定')













    elif a == '退出' or a == None:
        break
    elif a == '说明书':
        winsound.PlaySound('C:\Windows\Media\Windows Background.wav',flags = 1)
        easygui.msgbox('''
    ！本程序为alpha1.1.3 兼容 版本！（x86）
    （可用鼠标滚轮下滑）
        
1.此程序为CreamML开发的基于Windows平台的Python开源桌面应用程序，目的为让用户在用Python制作图表时免去写代码的烦恼，或让从未学过以及入门Python的用户体验自己能达到的水平，也能当作工具使用，未经许可，请勿复制代码！
        
2.若你选择的功能报错，程序会自动回到主菜单（严重错误可能会导致该程序停止运行）。发现错误可以通过lzy.20081229@qq.com或qq3219461147来告诉作者。
        
3.本程序支持将您的数据转化为图表（片），对于Excel小白以及想快速出图的人极其友好，且能制作一些复杂的图表，不推荐电脑小白使用此程序。
        
4.本程序能在32位Windows7及以上系统运行(注：我们暂时会提供win7兼容版，预计在2024年9月1日结束支持)，推荐在32位Windows10及以上系统运行(注意此副本为x86版本)，否则可能会导致程序出错，作者很少会修复该程序在Windows7或8.x系统上的bug(毕竟已经停止支持了)。
        
5.若你的电脑性能不够，请勿在词云生成中输出大于2560*1440的图片！极有可能出错！

6.图片制作过程中，若要退出，请点命令框的‘X’按钮(注：退出可能会导致程序异常(但这概率极低))

7.2025年10月14日后，作者对32位版本的升级与维护将停止(还有两年多呢，急什么急)

8.本程序部分版本自带“清除空格”程序，可以快速去掉文本空格与段落，在使用词云图转换器时，更快的完成准备过程
        
   
   
    祝您使用愉快！
    CreamML
    2023.8.15
    
                                                                       
        
        
        ''','说明书','下一页')
        easygui.msgbox('''
    ！本程序为alpha1.1.3版本！（x86）
    （可用鼠标滚轮下滑）
        
    更新日志：
    2023
    
    1.24 alpha1.1
    加入饼图生成器，并整合在主程序中
    优化了版权信息
    增加了说明书内容
    确定2025年10月14日结束32位支持
    
    1.28 alpha1.1.1
    增加win7兼容版，并确定于2024年9月结束该版本支持
    
    7.29 alpha1.1.2
    增加说明书翻页功能
    
    8.17 alpha1.1.3（仅制作兼容版）
    优化词云生成器与饼图生成器的使用体验，且两者版本号均变为1.1，预计在接下来的版本不会启用命令行显示
                       
    详细版本&版权信息：
    CML Image generator alpha 1.1.3 x86
    Copyright © 2022-2023 CreamML. All rights reserved.
    
                                                                       
        
        
        ''','说明书','确定')
    else:
        winsound.PlaySound('C:\Windows\Media\Windows Background.wav',flags = 1)
        easygui.msgbox('此项功能暂未开放，请下次再使用:D','暂未开放','回到主菜单')
