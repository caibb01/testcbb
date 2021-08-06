import json
import requests


class HttpRequest(object):
    def sendPost(self,url,data,headers=None):
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        return json.loads(result.content)

    def sendGet(self,url,headers=None):
        result = requests.get(url=url,headers=headers)
        return json.loads(result.content)

    def sendDelete(self,url,headers=None):
        result = requests.delete(url=url,headers=headers)
        return json.loads(result.content)