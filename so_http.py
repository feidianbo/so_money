#coding:utf-8
'''
    下载网页内容
    @author: fc_lamp
    @blog:fc-lamp.blog.163.com
'''
import urllib2
import httplib
import urlparse
import cookielib
import time
import socket

socket.setdefaulttimeout(30)

class spider():
    '''
        下载网页内容
    '''
    header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'',
        'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2',
        'Referer':''
        }

    def __init__(self):
        '''
            初始化
        '''
        cookie = cookielib.CookieJar()
        cookieProc = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(cookieProc)
        urllib2.install_opener(opener)

    def http1(self,url,method='GET'):
        '''
            httplib 方式
        '''
        host = urlparse.urlparse(url)
        sleep_time = 0
        while True:
            if sleep_time >15:
                res = False
                break
            try:
                http = httplib.HTTPConnection(host.netloc)
                http.request(method,host.path)
                res = http.getresponse().read()
                break
            except Exception as e:
                #print str(e) 有可能网络原因
                sleep_time+=5
                time.sleep(sleep_time)
                continue
            finally:
                #释放
                http.close()
                http = None

        return res


    def http2(self,url):
        '''
            urllib2 方式
        '''
        res_host = urlparse.urlparse(url)
        header = self.header
        header['Host'] = res_host.netloc
        header['Referer'] = res_host.netloc

        req = urllib2.Request(
                url=url,
                headers = header
            )
        sleep_time = 0
        while True:
            if sleep_time >15:
                res = False
                break
            try:
                res_q = urllib2.urlopen(req)
                res = res_q.read()
                break
            except Exception as e:
                #print str(e) #有可能网络原因
                sleep_time+=5
                time.sleep(sleep_time)
                continue
            finally:
                #关闭资源
                res_q.close()
                res_q = None

        return res
