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
line = input()
line0 = line.split("!")
if(line0[0]=='1'):
    line1 = line0[1].split(",")
    add = re.sub(r'1\d{10}','',line1[1])
    tel = re.findall(r'1\d{10}',line1[1])
    dic['姓名']=line1[0]
    dic['手机']=tel[0]
    PATTERN = r'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:村|镇|街道|乡)){0,1}'
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
        finaladd=[zxprovince,province,city,district,last]
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
        finaladd=[province,city,city1,district,last]

dic['地址:']=finaladd
json = json.dumps(dic,ensure_ascii=False,indent=4)
print (json)

#print("电话：",tel)
#print("地址：",add)
    
