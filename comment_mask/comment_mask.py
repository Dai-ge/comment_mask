import tkinter
import random

#TODO:完成UI设计
#TODO：对用户输入内容进行设定
mask_char = ['\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305', '\u0306', '\u0307', '\u0308', '\u0309', '\u030a', '\u030b', '\u030c', '\u030d', '\u030e', '\u030f', '\u0310', '\u0311', '\u0312', '\u0313', '\u0314', '\u0315', '\u0316', '\u0317', '\u0318', '\u0319', '\u031a', '\u031b', '\u031c', '\u031d', '\u031e', '\u031f', '\u0320', '\u0321', '\u0322', '\u0323', '\u0324', '\u0325', '\u0326', '\u0327', '\u0328', '\u0329', '\u032a', '\u032b', '\u032c', '\u032d', '\u032e', '\u032f', '\u0330', '\u0331', '\u0332', '\u0333', '\u0334', '\u0335', '\u0336', '\u0337', '\u0338', '\u0339', '\u033a', '\u033b', '\u033c', '\u033d', '\u033e', '\u033f', '\u0340', '\u0341', '\u0342', '\u0343', '\u0344', '\u0345', '\u0346', '\u0347', '\u0348', '\u0349', '\u034a', '\u034b', '\u034c', '\u034d', '\u034e', '\u034f', '\u0350', '\u0351', '\u0352', '\u0353', '\u0354', '\u0355', '\u0356', '\u0357', '\u0358', '\u0359', '\u035a', '\u035b', '\u035c', '\u035d', '\u035e', '\u035f', '\u0360', '\u0361', '\u0362', '\u0363', '\u0364', '\u0365', '\u0366', '\u0367', '\u0368', '\u0369', '\u036a', '\u036b', '\u036c', '\u036d', '\u036e']#标注字符对应的Utf-8 code
mask_foundation=['t','k','y']

def generate_mask(intense,message):
    '''生成掩码的函数，原理是从mask_foundation中抽取一个基本字符，然后加组合字符输出，这个mask会放在message中每个字符后面一个位置'''
    result = message.copy()
    index_insert_time = 0
    for index_message,ch in enumerate(message):
        mask=random.choice(mask_foundation)
        mask_time = random.randint(0,intense)
        index_insert = index_message + index_insert_time + 1

        for i in range(mask_time):
            char_time=random.randint(1,5)
            for j in range(char_time):
                mask_c = random.choice(mask_char)
                mask = mask + mask_c

        index_insert_time=index_insert_time+1+char_time
        result.insert(index_insert,mask)
    return result

if __name__ == '__main__':
    mes = list(input("输入信息："))
    inte = int(input("输入强度： "))
    re=generate_mask(inte,mes)
    print(''.join(re))