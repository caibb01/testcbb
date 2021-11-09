import json
import requests


class HttpRequest(object):
    def sendPost(self, url, data, headers=None):
        print(url)
        result = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(result.content.decode('utf8'))
        return json.loads(result.content)

    def sendGet(self, url, headers=None):
        print(url)
        result = requests.get(url=url, headers=headers)
        print(result.content.decode('utf8'))
        return json.loads(result.content)

    def sendDelete(self, url, headers=None):
        print(url)
        result = requests.delete(url=url, headers=headers)
        print(result.content.decode('utf8'))
        return json.loads(result.content)
