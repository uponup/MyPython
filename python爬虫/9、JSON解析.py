import json

jsondata = '''
{
"Uin":0,
"UserName":"@c482d142bc698bc3971d9f8c26335c5c",
"NickName":"小帅b",
"HeadImgUrl":"/cgi-bin/mmwebwx-bin/webwxgeticon?seq=500080&username=@c482d142bc698bc3971d9f8c26335c5c&skey=@crypt_b0f5e54e_b80a5e6dffebd14896dc9c72049712bf",
"DisplayName":"",
"ChatRoomId":0,
"KeyWord":"che",
"EncryChatRoomId":"",
"IsOwner":0
}
'''

# json数据转换成对象
myFriend = json.loads(jsondata)

# 获取对象中的值
print(myFriend.get('KeyWord'))

# 将对象转换成json数据
jsondata2 = json.dumps(myFriend)
print(jsondata2)