from global_vars import *

class Auth():
    def __init__(self, api_endpoint: str, headers: dict, console_type: str, username: str, password: str, provider_id: str) -> None: 
        self.__body = {
            'consoleType': CONSOLE_TYPE[console_type],
            'userName': username,
            'password': password,
            'providerId': PROVIDER_ID[provider_id]
            }

    def auth():
        pass

    def reauth():
        pass

    def get_token():
        pass