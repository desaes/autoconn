import requests

class ArandaApiRequest():

    def __init__(self, url, headers, verify=False):
        self.__url = url
        self.__headers = headers
        self.__verify = verify

    def do_request(self, url, headers, verify=False):
        self.__url = url
        self.__headers = headers
        self.__verify = verify
        return requests.get(url, headers, verify)

