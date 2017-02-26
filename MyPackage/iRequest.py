import urllib.parse,urllib.request

class iRequest:
    def post(url,iStrPostData):
        iStrPostData = urllib.parse.urlencode(iStrPostData).encode(encoding='UTF8')
        header = {
                  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
                }
        req= urllib.request.Request(
                   url,
                   iStrPostData,
                   headers = header)
        return urllib.request.urlopen(req).read().decode("UTF8")

    def get(url):
        header = {
                  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
                }
        req= urllib.request.Request(
                   url,
                   headers = header)
        return urllib.request.urlopen(req).read().decode("UTF8")

