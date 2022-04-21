import json
import requests


class HttpRequest(object):
    def sendPost(self, url, data, headers=None):
        # print(url)
        try:
            requests.packages.urllib3.disable_warnings()
            result = requests.post(url=url, data=json.dumps(data), headers=headers)
            timeConsuming = result.elapsed.total_seconds()
            print("========:",result.headers.get("Set-KolAuthorization"))
            print(result.content.decode('utf8'))
        except Exception as e:
            print("errorResult:", result)
            return result
        return json.loads(result.content),timeConsuming , result.headers

    def sendGet(self, url, headers=None):
        # print(url)
        try:
            requests.packages.urllib3.disable_warnings()
            result = requests.get(url=url, headers=headers)
            timeConsuming = result.elapsed.total_seconds()
            print(result.content.decode('utf8'))
        except Exception as e:
            #result = {"code": 2, "error:": e}
            print("errorResult:", result)
            return result
        return json.loads(result.content),timeConsuming, result.headers

    def sendDelete(self, url, headers=None):
        print(url)
        result = requests.delete(url=url, headers=headers)
        print(result.content.decode('utf8'))
        return json.loads(result.content)
