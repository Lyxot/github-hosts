# -*- coding: UTF-8 -*-
from requests import get,Session,exceptions
from requests.adapters import HTTPAdapter
from os import name

urls = ['github.com','github.global.ssl.fastly.net','codeload.github.com','raw.githubusercontent.com']

def get_ip(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59'}
    html = get(url,headers=headers)
    html.encoding = 'utf-8'
    html = html.text
    ip = html[html.find('www.ipaddress.com/ipv4/') + 23:html.find('\\',html.find('www.ipaddress.com/ipv4/'))]
    return ip

def rewrite_hosts(result):
    if name == 'nt':
        try:
            with open('C:\\Windows\\System32\\drivers\\etc\\hosts','r') as r:
                lines=r.readlines()
            with open('C:\\Windows\\System32\\drivers\\etc\\hosts','w') as w:
                for l in lines:
                    if urls[0] in l or urls[1] in l or urls[2] in l or urls[3] in l or l == '\n':
                        continue
                    w.write(l)
            with open('C:\\Windows\\System32\\drivers\\etc\\hosts','a') as hosts:
                hosts.write(result)
            print('Success! 成功!\nPlease reset the HOSTS file if there are any exceptions below 如有以下异常请重置hosts文件\nSlow Loading github.com,Unable to connect github.com      Github访问慢,无法访问Github')
        except IOError:
            print('Fail,please try to run this script as an administrator 失败,请以管理员身份运行这个脚本')
        except:
            print('Unknown error,please create an issue 未知错误，请创建issue')
    elif name == 'posix':
        try:
            with open('/etc/hosts','r') as r:
                lines=r.readlines()
            with open('/etc/hosts','w') as w:
                for l in lines:
                    if urls[0] in l or urls[1] in l or urls[2] in l or urls[3] in l or l == '\n':
                        continue
                    w.write(l)
            with open('/etc/hosts','a') as hosts:
                hosts.write(result)
            print('Success! 成功!\nPlease reset the HOSTS file if there are any exceptions below 如有以下异常请重置hosts文件\nSlow Loading github.com,Unable to connect github.com      Github访问慢,无法访问Github')
        except IOError:
            print('Fail,please try to run this script as root 失败,请以root用户运行这个脚本')
        except:
            print('Unknown error,please create an issue 未知错误，请创建issue')

try:
    if __name__ == "__main__":
        Session().mount('https://',HTTPAdapter(max_retries=3))
        if name == 'nt':
            print('System: Windows')
            ip = get_ip('https://' + urls[0] + '.ipaddress.com')
            result = ip + ' ' + urls[0]
            print('url: ' + urls[0] + ' ip: ' + ip)
            ip = get_ip('https://fastly.net.ipaddress.com/' + urls[1])
            result = result + '\r\n' + ip + ' ' + urls[1]
            print('url: ' + urls[1] + ' ip: ' + ip)
            ip = get_ip('https://github.com.ipaddress.com/' + urls[2])
            result = result + '\r\n' + ip + ' ' + urls[2]
            print('url: ' + urls[2] + ' ip: ' + ip)
            ip = get_ip('https://githubusercontent.com.ipaddress.com/' + urls[3])
            result = result + '\r\n' + ip + ' ' + urls[3]
            print('url: ' + urls[3] + ' ip: ' + ip)
        elif name == 'posix':
            print('System: Linux/Unix')
            ip = get_ip('https://' + urls[0] + '.ipaddress.com')
            result = ip + ' ' + urls[0]
            print('url: ' + urls[0] + ' ip: ' + ip)
            ip = get_ip('https://fastly.net.ipaddress.com/' + urls[1])
            result = result + '\n' + ip + ' ' + urls[1]
            print('url: ' + urls[1] + ' ip: ' + ip)
            ip = get_ip('https://github.com.ipaddress.com/' + urls[2])
            result = result + '\n' + ip + ' ' + urls[2]
            print('url: ' + urls[2] + ' ip: ' + ip)
            ip = get_ip('https://githubusercontent.com.ipaddress.com/' + urls[3])
            result = result + '\n' + ip + ' ' + urls[3]
            print('url: ' + urls[3] + ' ip: ' + ip)
        else:
            print('Unsupported system! 不支持的系统!')
            exit()
        rewrite_hosts(result)
except KeyboardInterrupt:
    print('User termination 用户终止')
except (exceptions.ConnectionError,exceptions.HTTPError,exceptions.UnrewindableBodyError,exceptions.RetryError,exceptions.SSLError,exceptions.ConnectTimeout,exceptions.Timeout,exceptions.URLRequired,exceptions.TooManyRedirects,exceptions.MissingSchema,exceptions.InvalidSchema,exceptions.InvalidURL,exceptions.InvalidHeader,exceptions.ChunkedEncodingError,exceptions.StreamConsumedError,exceptions.ContentDecodingError):
    print('Fail,please check your network connection 失败,请检查你的网络连接')
except:
    print('Unknown error,please create an issue 未知错误，请创建issue')