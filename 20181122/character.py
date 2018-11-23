#-*- coding:utf-8 -*-


'''输出单引号，双引号，转义字符'''

print("I'm ok")

print('he is "')

print('he is \" ')

'''输出换行，制表符，\本身转义'''

print('my name \n King.')

print('my name \t King.')

print('my name \\ King.\\')

'''特殊情况在单引号单加r表示单引号内不转义'''

print('my name \\ \t shanyang')

print(r'my name \\ \t shanyang')

print(r"my name \\ \t shanyang")

'''如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用...的格式表示多行内容--未试出'''

print('''line1\n12\n23\n3\n5\n7\n8\n9\n0\n-\n78\n678\n678\nline2\n123\n123\n23\n34\n54\nline3''')

print(r'''hello,\n world''')

