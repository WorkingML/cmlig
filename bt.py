
import easygui
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'simhei'

if easygui.ynbox('''欢迎使用cml饼图生成器
本程序可以将你的数据转换为饼图


                                  ''','欢迎 - cmlpc v1.0',('开始使用','回到主菜单')):

    while True:

        mode = easygui.buttonbox('请选择功能模式','选择模式',choices = ('极简模式','简洁模式','一般模式','高级模式','模式说明'))
        if mode == '高级模式':
            flag = True
            while flag:
                easygui.msgbox('请输入数据\n格式：a b c d e ... (其中a等字母指代数字)', '输入数据', '确定')
                data = input('请在此处输入数字:')
                d1 = data.split()
                w1 = []
                easygui.msgbox('请为数据匹配标签\n格式：a b c d e ... (其中a等字母指代标签)', '输入标签', '确定')
                word = input('请在此处输入标签:')
                w1 = word.split()
                if len(w1) == len(d1):
                    flag = False
                else:
                    easygui.msgbox('数据数与标签数不一致！(E1)', '请重新输入', '确定')

            auto = easygui.buttonbox('是否显示百分占比值？', '显示占比值',
                                     choices=('以整数+百分号显示', '以浮点数(小数)+百分号显示' ))
            if auto == '以整数+百分号显示':
                atp = '%d%%'
            if auto == '以浮点数(小数)+百分号显示':
                atp = '%f%%'

            rad = easygui.buttonbox('请设置饼图在输出图片中的大小', '设置大小', choices=('小(0.5)', '中(1)', '大(1.5)'))
            if rad == '小(0.5)':
                rdu = 0.5
            if rad == '中(1)':
                rdu = 1
            if rad == '大(1.5)':
                rdu = 1.5

            color = []
            easygui.msgbox('请自定义饼图颜色', '自定义颜色', '确定')
            easygui.msgbox('检测到您输入了' + str(len(d1)) + '个数据，所以请输入' + str(len(d1)) + '种颜色所对应的英语单词','输入颜色', '确定')
            for i in range(len(d1)):
                color.append(input('请输入第' + str(i + 1) + '种颜色:'))

            easygui.msgbox('请输入输出文件的宽与高（像素）\ntips:输入文字会报错', '输入大小', '开始输入')
            # 1英寸=100像素

            wid = input('请在此处输入宽:')
            hei = input('请在此处输入高:')
            wid = int(wid)
            hei = int(hei)

            plt.figure(figsize=(wid / 100, hei / 100))
            plt.pie(d1, labels=w1, radius=rdu, colors=color, autopct=atp)

            easygui.msgbox('我们即将展示你的图片\n随后点击弹出窗口左下角以保存', '展示图片', '展示')
            plt.show()

            if easygui.ynbox('感谢使用，是否退出？', '选择', ('回到主菜单', '继续制作')):
                break
            else:
                continue

        elif mode == '极简模式':

            easygui.msgbox('请输入数据\n格式：a b c d e ... (其中a等字母指代数字)', '输入数据', '确定')
            data = input('请在此处输入数字:')
            d1 = data.split()

            rad = easygui.buttonbox('请设置饼图在输出图片中的大小', '设置大小', choices=('小(0.5)', '中(1)', '大(1.5)'))
            if rad == '小(0.5)':
                rdu = 0.5
            if rad == '中(1)':
                rdu = 1
            if rad == '大(1.5)':
                rdu = 1.5

            easygui.msgbox('请输入输出文件的宽与高（像素）\ntips:输入文字会报错', '输入大小', '开始输入')
            # 1英寸=100像素

            wid = input('请在此处输入宽:')
            hei = input('请在此处输入高:')
            wid = int(wid)
            hei = int(hei)

            plt.figure(figsize=(wid / 100, hei / 100))
            plt.pie(d1, radius=rdu)

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
                data = input('请在此处输入数字:')
                d1 = data.split()
                w1 = []
                easygui.msgbox('请为数据匹配标签\n格式：a b c d e ... (其中a等字母指代标签)', '输入标签','确定')
                word = input('请在此处输入标签:')
                w1 = word.split()
                if len(w1) == len(d1):
                    flag = False
                else:
                    easygui.msgbox('数据数与标签数不一致！(E1)', '请重新输入', '确定')

            auto = easygui.buttonbox('请选择百分占比值显示方式', '显示占比值', choices = ('以整数+百分号显示', '以浮点数(小数)+百分号显示'))
            if auto == '以整数+百分号显示':
                atp = '%d%%'
            if auto == '以浮点数(小数)+百分号显示':
                atp = '%f%%'

            rad = easygui.buttonbox('请设置饼图在输出图片中的大小', '设置大小', choices=('小(0.5)', '中(1)', '大(1.5)'))
            if rad == '小(0.5)':
                rdu = 0.5
            if rad == '中(1)':
                rdu = 1
            if rad == '大(1.5)':
                rdu = 1.5

            easygui.msgbox('请输入输出文件的宽与高（像素）\ntips:输入文字会报错', '输入大小', '开始输入')
            # 1英寸=100像素

            wid = input('请在此处输入宽:')
            hei = input('请在此处输入高:')
            wid = int(wid)
            hei = int(hei)

            plt.figure(figsize=(wid / 100, hei / 100))
            plt.pie(d1, labels=w1, radius=rdu, autopct=atp)

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
                data = input('请在此处输入数字:')
                d1 = data.split()
                w1 = []
                easygui.msgbox('请为数据匹配标签\n格式：a b c d e ... (其中a等字母指代标签)', '输入标签', '确定')
                word = input('请在此处输入标签:')
                w1 = word.split()
                if len(w1) == len(d1):
                    flag = False
                else:
                    easygui.msgbox('数据数与标签数不一致！(E1)', '请重新输入', '确定')


            rad = easygui.buttonbox('请设置饼图在输出图片中的大小', '设置大小', choices=('小(0.5)', '中(1)', '大(1.5)'))
            if rad == '小(0.5)':
                rdu = 0.5
            if rad == '中(1)':
                rdu = 1
            if rad == '大(1.5)':
                rdu = 1.5

            easygui.msgbox('请输入输出文件的宽与高（像素）\ntips:输入文字会报错', '输入大小', '开始输入')
            # 1英寸=100像素

            wid = input('请在此处输入宽:')
            hei = input('请在此处输入高:')
            wid = int(wid)
            hei = int(hei)

            plt.figure(figsize=(wid / 100, hei / 100))
            plt.pie(d1, radius=rdu,labels=w1)

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
            
            
            
                               ''','模式说明','确定')











