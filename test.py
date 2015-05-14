import so_http

spider = so_http.spider()
spider.header['Referer'] = 'http://www.baidu.com'
print spider.http2('http://www.baidu.com')
