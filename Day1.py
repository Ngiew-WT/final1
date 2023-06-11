'''
课堂练习
将用户的姓名存到一个变量中，并向用户显示一条信息
Hello 姓名 would you like to learn python today?
再来一个回复
'''

# username=input('Name: ').title()
# print('Hello '+username+' would you like to learn python today?')
# reply=input('yes or no')

name='Alice'
print('Hello '+name+' would you like to learn python today?')
reply=input('yes or no').lower()
print(reply)