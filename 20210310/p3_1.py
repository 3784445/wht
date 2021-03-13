# -*- coding:utf8 -*-


print ('Hello python test1')

info={
    'name':'egon',
    'hobbies':['play','sleep'],
    'company_info':{
        'name':'Oldboy',
        'type':'education',
        'emp_num':40,
    }
}
# print(info['company_info']['name']) #取公司名


students=[
    {'name':'alex','age':38,'hobbies':['play','sleep']},
    {'name':'egon','age':18,'hobbies':['read','sleep']},
    {'name':'wupeiqi','age':58,'hobbies':['music','read','sleep']},
]
print(students[2]['hobbies'][1]) #取第二个学生的第二个爱好

# 字典相关的嵌套、取值

numbers={'shu':1,'shu1':2}

# print numbers[0]


#print type(numbers['shu'])

def num(a,b):
    if a > b:
        print('a is big number!')
    elif a == b:
        print('a,b is equally!')
    else:
        print('b is big number!')

num(numbers['shu'],numbers['shu1'])


###213j12l3kj12l3k1jl23i


###回来