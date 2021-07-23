import json
import traceback
from tkinter import COMMAND

import pymysql
# 打开数据库连接
from pymysql import err

username = ""  # 用户名
password = ""  # 连接密码
localhost = ""  # 连接地址
database = ""  # 数据库名

connection2 = pymysql.connect(host='',
                              user='root',
                              password='',
                              database='test',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor,)

connection = pymysql.connect(host=localhost,
                             user=username,
                             password='',
                             database='facerecognition',
                             charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

data =[-0.14086597743961546,0.078781312952439, 0.039479597161213555, -0.10006206234296162, -0.10533259643448724, -0.09947221808963352, -0.013476612874203257, -0.11947387208541234, 0.1300511790646447, -0.11635424776209725, 0.1945297055774265, -0.12649859322441948, -0.277184870507982, -0.08605559998088413, -0.04814669614036878, 0.2007980595032374, -0.14260176652007633, -0.09598391420311397, -0.1220781695511606, -0.014117592014372349, 0.10527887360917197, 0.0406792267329163, 0.016573474354421098, 0.0393916643742058, -0.014440463648902046, -0.4027448892593384, -0.08489878310097589, -0.03450178003145589, -0.019216160910824936, -0.04292089160945681, -0.07713280783759223, 0.07365855243470934, -0.18132138748963675, -0.13311017056306204, 0.041449144275652036, 0.10784688923094007, -0.015878886812263064, -0.0804746730460061, 0.17404362062613168, -0.01898882496688101, -0.2231664839718077, 0.00817365287285712, 0.09404335667689641, 0.23411175939771864, 0.1706855313645469, 0.05295879766345024, 0.04661106069882711, -0.1602770768933826, 0.12640092190768984, -0.20434194968806374, 0.007831107825040817, 0.11787292692396376, 0.08200827489296596, 0.036284590139985085, 0.02283021600710021, -0.1467862907383177, 0.025439905727075204, 0.15618336035145652, -0.1627032375997967, -0.02050600987341669, 0.13090265873405668, -0.12074418862660725, -0.09257794668277104, -0.11200777524047428, 0.268041772974862, 0.08411922388606602, -0.15046581625938416, -0.13116325520806843, 0.12502752989530563, -0.11402554230557548, -0.04112706354094876, -0.004025210109021928, -0.16906186110443538, -0.15588500764634874, -0.28480396336979336, 0.04583647516038683, 0.38746998376316494, 0.09695716119474834, -0.18453392055299547, 0.04405712646742662, -0.08406273523966472, 0.047591092685858406, 0.15051766402191585, 0.1553322689400779, -0.013853528536856174, 0.02533568090034856, -0.07120931810802883, 0.0341114088272055, 0.1772402028242747, -0.08068817688359155, -0.018927356900854245, 0.19046467708216774, 0.02573579487701257, 0.09919602341122097, 0.007633495299766461, -0.014415009865640767, -0.09465839051538044, 0.008579252753406763, -0.1549010624488195, 0.03374082098404566, 0.05660003133945995, -0.03382061007950041, 1.506543614798122e-05, 0.09287552452749676, -0.11984590192635854, 0.09475319584210713, -0.011732526123523712, 0.017841347286270723, 0.019905002011607092, -0.08899494757254918, -0.04542445888121923, -0.06613815410269631, 0.0782669915093316, -0.18852099941836464, 0.1829485081964069, 0.1776902990208732, 0.032423983017603554, 0.15723960101604462, 0.1133712844716178, 0.08405332846773995, 0.04135320459802946, 0.010379429078764386, -0.22475294768810272, -0.015671319535209075, 0.18292729887697431, 0.0195245576194591, 0.10484886666138966, -0.027534874570038583, '马清杰']


def SelectDatabase(uid):


    c = connection.cursor()
    try:
        c.ping()
        print("ok")
    except:
        c = connection.cursor()

    sql = "SELECT	* FROM `user` WHERE uid = %s" % uid

    # print(sql)
    import time


    c.execute(sql)
    results = c.fetchall()
    # 提交到数据库执行
    # print(results)
    re1 = json.dumps(results[0], ensure_ascii=False)
    # print(re1.uid)
    # Convert string to Python dict
    dict = json.loads(re1)
    # print(dict)
    # 转换成字典来后，要访问其中的值，可以使用字典的key来访问
    # print(dict['uid'])
    # print(dict['administor'])
    administor = dict['administor']
    connection.commit()

    # 关闭数据库连接
    # c.connection.close()
    print(administor)
    return administor
# uid = 1101
# administor = SelectDatabase(None,uid=uid)
# print(administor)
def fun(i):
    global c
    try:
        c.ping()   # 采用连接对象的ping()函数检测连接状态
        print('connect-%d ok' % i)

    # 出现异常重新连接
    except:
        c = connection()

def encode(facedata): #编码
    import  base64
    import  json
    # str = ', '.join(str(i) for i in facedata)
    # result_list = facedata.findall(r"[(](.*?)[)]", "(123)")
    # str = ",".join(facedata)+

    data =  json.dumps(facedata)

    facedata_base64  = base64.b64encode(data.encode('utf-8'))
    # print(facedata_base64)
    # temp = base64.b64decode(facedata_base64)
    # print(temp)
    return facedata_base64

def decode(data):#解码
    import base64
    # decode_data =base64.b64decode(data)
    decode_dict = base64.b64decode(data)

    # print(decode_dict)
    #字符串按照逗号分为list

    s = str(decode_dict, encoding='utf-8')
    decode_dict1 = s.rstrip('a')
    decode = decode_dict1.lstrip('b')

    return  decode


def facewritedatabese(face,name,id):
    # 创建connection连接
    c = connection.cursor()
    try:
        c.ping()
        print("ok")
    except:
        c = connection.cursor()
    # 获取cursor对象
    # cs1 = c.cursor()
    # 执行sql语句
    # print(sql)
    import time
    sql = 'insert into face(face, name, ID) values(%s, %s, %s)'
    # print(sql)
    face = face
    name = name
    ID = id
    values = (face, name, ID)
    # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
    c.execute(sql,values)
    connection.commit()
    # c.connection.close()

def kaoqinwritedatabese(data,name,id):
    # 创建connection连接
    c = connection.cursor()
    try:
        c.ping()
        print("ok")
    except:
        c = connection.cursor()
    # 获取cursor对象
    # cs1 = c.cursor()
    # 执行sql语句
    # print(sql)
    import time

    sql = 'insert into date(date, name, ID) values(%s, %s, %s)'
    # print(sql)

    date = data
    name = name
    ID = id
    values = (date, name, ID)
    # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
    c.execute(sql,values)
    connection.commit()
    # c.connection.close()
def infowritedatabese(id,name):
    # 创建connection连接
    c = connection.cursor()
    try:
        c.ping()
        print("ok")
    except:
        c = connection.cursor()
    # 获取cursor对象
    # cs1 = c.cursor()
    # 执行sql语句
    # print(sql)
    import time

    sql = 'insert into user(uid, name, administor) values(%s, %s, %s)'
    # print(sql)

    uid = id
    name = name
    administor = 0
    values = (uid, name, administor)
    # 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
    c.execute(sql,values)
    connection.commit()
    # c.connection.close()

def Selectuid(name):


    c = connection.cursor()
    try:
        c.ping()
        print("ok")
    except:
        c = connection.cursor()

    sql = "SELECT	* FROM `user` WHERE name = '%s' " %name
    print(sql)

    # print(sql)
    import time


    c.execute(sql)
    results = c.fetchall()
    # 提交到数据库执行
    # print(results)
    re1 = json.dumps(results[0], ensure_ascii=False)
    # print(re1.uid)
    # Convert string to Python dict
    dict = json.loads(re1)
    # print(dict)
    # 转换成字典来后，要访问其中的值，可以使用字典的key来访问
    # print(dict['uid'])
    # print(dict['administor'])
    id = dict['uid']
    connection.commit()

    # 关闭数据库连接
    # c.connection.close()
    print(id)
    return id

