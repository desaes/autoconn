from . global_vars import *
class Aranda:

    def __init__(self, api_endpoint: str, headers: dict, console_type: str, username: str, password: str, provider_id: str) -> None: 
        self.__body = {
            'consoleType': CONSOLE_TYPE[console_type],
            'userName': username,
            'password': password,
            'providerId': PROVIDER_ID[provider_id]
            }

    def auth(self):
        pass

    def reauth(self):
        pass

    def get_token(self):
        pass