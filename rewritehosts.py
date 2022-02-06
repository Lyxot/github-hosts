# -*- coding: UTF-8 -*-
import requests,os

urls = ['github.com','codeload.github.com','github.global.ssl.fastly.net','codeload.github.com','api.github.com','nodeload.github.com','raw.github.com','training.github.com','assets-cdn.github.com','documentcloud.github.com','help.github.com']
githubusercontent_urls = ['raw.githubusercontent.com','pkg-containers.githubusercontent.com','cloud.githubusercontent.com','gist.githubusercontent.com','marketplace-screenshots.githubusercontent.com','repository-images.githubusercontent.com','user-images.githubusercontent.com','desktop.githubusercontent.com','avatars.githubusercontent.com','avatars0.githubusercontent.com','avatars1.githubusercontent.com','avatars2.githubusercontent.com','avatars3.githubusercontent.com','avatars4.githubusercontent.com','avatars5.githubusercontent.com','avatars6.githubusercontent.com','avatars7.githubusercontent.com','avatars8.githubusercontent.com']

def get_ip(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59'}
    html = requests.get('https://ipaddress.com/website/'+url,headers=headers).text
    ip = html[html.find('<ul class="comma-separated"><li>') + 32:]
    ip = ip[:ip.find('</li>')]
    return ip

def rewrite_hosts(result):
    if os.name == 'nt':
        path='C:\\Windows\\System32\\drivers\\etc\\hosts'
    elif os.name == 'posix':
        path='/etc/hosts'
    with open(path,'r+') as f:
        context=f.read()
        for i in urls+githubusercontent_urls:
            context=context.replace(context[context[:context.find(i)+len(i)].rfind('\n'):context.find(i)+len(i)],'')
        context=context+'\n'+result
        f.seek(0,0)
        print(context)
        f.write(context)

if __name__ == "__main__":
    try:
        result=''
        for i in urls:
            result=result+(get_ip(i))+' '+i+'\n'
        result=result+'''185.199.108.133 raw.githubusercontent.com
185.199.108.154 pkg-containers.githubusercontent.com
185.199.108.133 cloud.githubusercontent.com
185.199.108.133 gist.githubusercontent.com
185.199.108.133 marketplace-screenshots.githubusercontent.com
185.199.108.133 repository-images.githubusercontent.com
185.199.108.133 user-images.githubusercontent.com
185.199.108.133 desktop.githubusercontent.com
185.199.108.133 avatars.githubusercontent.com
185.199.108.133 avatars0.githubusercontent.com
185.199.108.133 avatars1.githubusercontent.com
185.199.108.133 avatars2.githubusercontent.com
185.199.108.133 avatars3.githubusercontent.com
185.199.108.133 avatars4.githubusercontent.com
185.199.108.133 avatars5.githubusercontent.com
185.199.108.133 avatars6.githubusercontent.com
185.199.108.133 avatars7.githubusercontent.com
185.199.108.133 avatars8.githubusercontent.com'''
        rewrite_hosts(result)
        print('Done!')
    except IOError:
        print('Please run as administrator\n请以管理员身份运行')
    except:
        print('Error')
