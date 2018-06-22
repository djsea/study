from urllib import request


if __name__ == '__main__':

    url = "http://www.xitongzhijia.net/xtjc/20141223/33228.html"
    rsp = request.urlopen(url)

    html = rsp.read()
    print(type(html))

    print(html)
