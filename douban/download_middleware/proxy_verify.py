# -*-coding:utf-8-*-
# ��֤���¿��ô��� For http://www.5uproxy.net ���̰߳�
# by redice 2010.12.09

import sys
reload(sys)
sys.setdefaultencoding('gbk')


import urllib
import urllib2
from urllib2 import URLError, HTTPError

DEBUG = True

#htmlҳ�����غ���
def getHtml(url,post_data=None,cookie=None):
        """Fetch the target html
        url - URL to fetch
        post_data - POST Entity
        cookie - Cookie Header
        """
        if DEBUG:
            print "getHtml: ",url

        result =''
        
        try:
            #create a request
            request = urllib2.Request(url)

            #change User-Agent
            request.add_header('User-Agent','Mozilla/5.0')
            
            #change Referrer
            request.add_header('Referrer',url)
            
            #if has cookie,add cookie header
            if cookie:
               request.add_header('Cookie',cookie)

            #create a opener
            opener = urllib2.build_opener()            
           
            #if has post entity
            if post_data:
                #encode post data
                post_data = urllib.urlencode(post_data)
                
                response = opener.open(request,post_data)
            else:
                response = opener.open(request)
            
            result = response.read()
                
            response.close()

            #no content,don't save
            if not result or len(result)==0:
                return ''
            
            return  result
        except HTTPError, e:
            if DEBUG:
                print 'Error retrieving data:',e
                print 'Server error document follows:\n'
                #print e.read()
            return ''
        except URLError, e:
            if hasattr(e, 'reason'):
                if DEBUG:
                    print 'Failed to reach a server.'
                    print 'Reason: ', e.reason
                return ''
            elif hasattr(e, 'code'):
                if DEBUG:
                    print 'The server couldn\'t fulfill the request.'
                    print 'Error code: ', e.code
                return ''
        except Exception, e:
            if DEBUG:
                print e
            return ''
        

#��Ҫ��֤�Ĵ����б�
proxy_urls = []
proxy_urls.append({'url':'http://www.kuaidaili.com/free/inha/1/','type':'http_fast'})
# proxy_urls.append({'url':'http://www.5uproxy.net/http_anonymous.html','type':'http_anonymous'})
# proxy_urls.append({'url':'http://www.5uproxy.net/http_non_anonymous.html','type':'http_transparent'})
# proxy_urls.append({'url':'http://www.5uproxy.net/socks5.html','type':'socks5'})


import re
import socket
import time
import threading

result =[]


#�߳�ͬ����
lock = threading.Lock() 

def synchronous(f):
    def call(*args, **kwargs):
        lock.acquire()
        try:
            return f(*args, **kwargs)
        finally:
            lock.release()
    return call



#�Ȼ�ȡ���д���֤�Ĵ���
proxies = []

for proxy_url in proxy_urls:
    html = getHtml(proxy_url['url'])
    
    #����ƥ���ȡÿһ����
    rs = re.compile(r'''<tr .*?>[\s\S]*?<td .*?>\d+?</td>[\s\S]*?<td>(\S+?)</td>[\s\S]*?<td .*?>(\S+?)</td>[\s\S]*?<td .*?>(\S+?)</td>[\s\S]*?</tr>''',re.DOTALL).findall(html)
    
    for r in rs:
        proxy = {}
        
        #��������
        proxy['domain'] = r[0]
        #����˿�
        proxy['port'] = r[1]
        #�������
        proxy['state'] = r[2]
        #��������
        proxy['type'] = proxy_url['type']
        #��Ӧʱ��
        proxy['time'] = 0
        
        if not (proxy in proxies):
            proxies.append(proxy)



#��ȡһ������֤����
@synchronous
def getproxy():
    global proxies
    if len(proxies)>0:
        return proxies.pop()
    else:
        return ''


    
#������֤���
@synchronous
def saveresult(proxy):
    global result
    
    if not(proxy in result):
        result.append(proxy)


#�̺߳���
def verify():
    
    while 1:
        proxy = getproxy()
        #���д��������֤���
        if len(proxy)==0:
            return
        
        print "������֤��%s,%s" % (proxy['domain'],proxy['port'])
        
        #��֤����Ŀ�����
        #����һ��TCP�����׽���
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #����10��ʱ
        sock.settimeout(10)
        try:
            start = time.clock()
            
            #���Ӵ��������
            sock.connect((proxy['domain'], int(proxy['port'])))
            proxy['time'] = int((time.clock() - start) * 1000) 
            sock.close()
            
            saveresult(proxy)
            print "%s,%s ��֤ͨ������Ӧʱ�䣺%d ms." % (proxy['domain'],proxy['port'],proxy['time'])
        except Exception, e:
            if DEBUG:
                print e
            
            print "%s,%s ��֤ʧ��." % (proxy['domain'],proxy['port'])




#init thread_pool 
thread_pool = []

for i in range(20): 
    th = threading.Thread(target=verify,args=()) ; 
    thread_pool.append(th)

# start threads one by one         
for thread in thread_pool: 
    thread.start()

#collect all threads 
for thread in thread_pool: 
    threading.Thread.join(thread)


#�������Ӧʱ���С��������

result.sort(lambda x,y: cmp(x['time'], y['time']))  

fname = 'proxy_'+ time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())) +'.txt'
file = open(fname,'w')

print "��֤������£�"
for item in result:
     str = '%s:%s   %s,%s,%d' % (item['domain'],item['port'],item['type'],item['state'],item['time'])
     print str
     file.write(str+'\n')
    
file.close()

print "���д�������֤��ϣ�����%d����֤ͨ������֤ͨ���Ĵ����Ѵ���%s" % (len(result),fname)
    
