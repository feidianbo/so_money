# main
import urllib2

proxies = {}
proxy_handler = urllib2.ProxyHandler(proxies)
proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)

url = 'http://www.baidu.com'
req = urllib2.Request(url)
req.add_header('Referer', 'http://www.sina.com.cn')
r = urllib2.urlopen(req)
print r.read(500)
