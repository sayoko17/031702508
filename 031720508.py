import re
import json
import string
tel = ''
province = ''
zxprovince = ''
city = ''
city1= ''
district = ''
zhixia=['北京','天津','上海','重庆']
dic={}
def namenum(lista):
    line1 = lista[1].split(",")
    adda = re.sub(r'1\d{10}','',line1[1])
    tel = re.findall(r'1\d{10}',line1[1])
    dic['姓名']=line1[0]
    dic['手机']=tel[0]
    return adda
line = input()
line0 = line.split("!")
if(line0[0]=='1'):
    add = namenum(line0)
    PATTERN = r'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州|市|盟|自治州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州|市|旗)){0,1}([\u4e00-\u9fa5]{2,7}?(?:村|镇|街道|乡)){0,1}'
    pattern = re.compile(PATTERN)
    m = pattern.search(add)
#如果是直辖
    if (add[0:2] in zhixia):
        zxprovince = add[0:2]
        if m.lastindex >= 1:
            if m.group(1)!=None:
                province = m.group(1)
        if m.lastindex >= 2:
            if m.group(2)!=None:
                city = m.group(2)
        if m.lastindex >= 3:
            if m.group(3)!=None:
                city1 = m.group(3)
        if m.lastindex >= 4:
            if m.group(4)!=None:
                district = m.group(4)
        result = zxprovince+province+city+city1+district
        result1 = province+city+city1+district
        last = re.sub(result1,'',add,1)
        last1 = last.split('.')
        finaladd=[zxprovince,province,city,district,last1[0]]
#不是直辖
    else:
        if m.lastindex >= 1:
            if m.group(1)!=None:
                province = m.group(1)
        if m.lastindex >= 2:
            if m.group(2)!=None:
                city = m.group(2)
        if m.lastindex >= 3:
            if m.group(3)!=None:
                city1 = m.group(3)
        if m.lastindex >= 4:
            if m.group(4)!=None:
                district = m.group(4)
        result = province+city+city1+district
        last = re.sub(result,'',add)
        last1 = last.split('.')

        finaladd=[province,city,city1,district,last1[0]]
if(line0[0]=='2'):
    add = namenum(line0)
    PATTERN = r'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州|市|盟|自治州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州|市|旗)){0,1}([\u4e00-\u9fa5]{2,7}?(?:村|镇|街道|乡)){0,1}([\u4e00-\u9fa5]{2,7}?(?:路|大街|巷)){0,1}([0-9]{1,5}?(?:号)){0,1}'
    pattern = re.compile(PATTERN)
    m = pattern.search(add)
    if (add[0:2] in zhixia):
        zxprovince = add[0:2]
        if m.lastindex >= 1:
            if m.group(1)!=None:
                province = m.group(1)
        if m.lastindex >= 2:
            if m.group(2)!=None:
                city = m.group(2)
        if m.lastindex >= 3:
            if m.group(3)!=None:
                city1 = m.group(3)
        if m.lastindex >= 4:
            if m.group(4)!=None:
                district = m.group(4)
        if m.lastindex >= 5:
            if m.group(5)!=None:
                daolu = m.group(5)
        if m.lastindex >= 6:
            if m.group(6)!=None:
                hao = m.group(6)
        result = zxprovince+province+city+city1+district+daolu+hao
        result1 = province+city+city1+district+daolu+hao
        last = re.sub(result1,'',add,1)
        last1 = last.split('.')
        finaladd=[zxprovince,province,city,district,daolu,hao,last1[0]]
#不是直辖
    else:
        if m.lastindex >= 1:
            if m.group(1)!=None:
                province = m.group(1)
        if m.lastindex >= 2:
            if m.group(2)!=None:
                city = m.group(2)
        if m.lastindex >= 3:
            if m.group(3)!=None:
                city1 = m.group(3)
        if m.lastindex >= 4:
            if m.group(4)!=None:
                district = m.group(4)
        if m.lastindex >= 5:
            if m.group(5)!=None:
                daolu = m.group(5)
        if m.lastindex >= 6:
            if m.group(6)!=None:
                hao = m.group(6)
        result = province+city+city1+district+daolu+hao
        last = re.sub(result,'',add)
        last1 = last.split('.')

        finaladd=[province,city,city1,district,daolu,hao,last1[0]]
if(line0[0]=='3'):
    add = namenum(line0)
    PATTERN = r'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州|市|盟|自治州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州|市|旗)){0,1}([\u4e00-\u9fa5]{2,7}?(?:村|镇|街道|乡)){0,1}([\u4e00-\u9fa5]{2,7}?(?:路|大街|巷)){0,1}([0-9]{1,5}?(?:号)){0,1}'
    pattern = re.compile(PATTERN)
    m = pattern.search(add)
    if (add[0:2] in zhixia):
        zxprovince = add[0:2]
        if m.lastindex >= 1:
            if m.group(1)!=None:
                province = m.group(1)
        if m.lastindex >= 2:
            if m.group(2)!=None:
                city = m.group(2)
        if m.lastindex >= 3:
            if m.group(3)!=None:
                city1 = m.group(3)
        if m.lastindex >= 4:
            if m.group(4)!=None:
                district = m.group(4)
        if m.lastindex >= 5:
            if m.group(5)!=None:
                daolu = m.group(5)
        if m.lastindex >= 6:
            if m.group(6)!=None:
                hao = m.group(6)
        result = zxprovince+province+city+city1+district+daolu+hao
        result1 = province+city+city1+district+daolu+hao
        last = re.sub(result1,'',add,1)
        last1 = last.split('.')
        finaladd=[zxprovince,province,city,district,daolu,hao,last1[0]]
#不是直辖
    else:
        if m.lastindex >= 1:
            if m.group(1)!=None:
                province = m.group(1)
        if m.lastindex >= 2:
            if m.group(2)!=None:
                city = m.group(2)
        if m.lastindex >= 3:
            if m.group(3)!=None:
                city1 = m.group(3)
        if m.lastindex >= 4:
            if m.group(4)!=None:
                district = m.group(4)
        if m.lastindex >= 5:
            if m.group(5)!=None:
                daolu = m.group(5)
        if m.lastindex >= 6:
            if m.group(6)!=None:
                hao = m.group(6)
        result = province+city+city1+district+daolu+hao
        last = re.sub(result,'',add)
        last1 = last.split('.')

        finaladd=[province,city,city1,district,daolu,hao,last1[0]]
dic['地址']=finaladd
json = json.dumps(dic,ensure_ascii=False,indent=4)
print (json)
#print("电话：",tel)
#print("地址：",add)
    
