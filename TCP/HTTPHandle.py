# coding=utf-8
import httplib

#建立连接并发送get请求
import urllib

try:
     http_client = httplib.HTTPConnection("localhost",80, timeout=30)
     http_client.request("GET", "/phpwind/index.php")
     r1 = http_client.getresponse()
     print r1.status, r1.reason
     data1 = r1.read()

     http_client.request("GET", "/index.php?c=thread&fid=2")
     r2 = http_client.getresponse()
     print r2.status, r2.reason
     data2 = r2.read()
except Exception as e:
     print e
finally:
     if http_client:
         http_client.close()

#建立连接并发送post请求
try:
    params = urllib.urlencode({'username': 'admin', 'password': '520167'})
    headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Cookie": "_ac_079fa326=1; csrf_token=4a8b0d986643e4be; iUg_visit_referer=fid_2_page_1; iUg_visitor=cX5%2FfnaJZbY8QtmjnRvk3UDUie5LlN7RCurATHwjJnh6WbM7; iUg_lastvisit=1276%091463715182%09%2Fphpwind%2Findex.php%3Fm%3Dverify%26a%3Dget%26rand%3D1463715181; iUg_Pw_verify_code=b21e761decf945197a76781442997c6a; PHPSESSID=jfkdegojdq4cajercksm8ndai7"}

    http_Client = httplib.HTTPConnection("localhost", 80, timeout=30)
    http_Client.request("POST", "/phpwind/admin.php?a=login", params, headers)

    response = http_Client.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息
except Exception, e:
    print e
finally:
    if http_Client:
        http_Client.close()





