from urllib.request import urlopen

# url = 'http://hq.sinajs.cn/list=s_sh600000'
url = 'http://hq.sinajs.cn/list=sh600000'

request = urlopen(url)
content = request.read()
content = content.decode('gbk')

print(content)

content = content.split(',')
price = content[3]
print(price)