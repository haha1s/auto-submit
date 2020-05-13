import requests


def getCookies():
    # params = {
    #     'login_url': 'http://authserver.swun.edu.cn/authserver/login',
    #     'needcaptcha_url': 'http://authserver.swun.edu.cn/authserver/needCaptcha.html',
    #     'captcha_url': 'http://authserver.swun.edu.cn/authserver/captcha.html',
    #     'username': 'test',
    #     'password': 'test'
    # }

    params = {
        'login_url': 'https://jjjs.campusphere.net/iap/login',
        'needcaptcha_url': 'https://jjjs.campusphere.net/iap/checkNeedCaptcha',
        'captcha_url': 'https://jjjs.campusphere.net/iap/generateCaptcha',
        'username': 'test',
        'password': 'test'
    }
    res = requests.post('http://www.zimo.wiki:8080/wisedu-unified-login-api-v1.0/api/login', params)
    print(res.text)


if __name__ == '__main__':
    getCookies()
