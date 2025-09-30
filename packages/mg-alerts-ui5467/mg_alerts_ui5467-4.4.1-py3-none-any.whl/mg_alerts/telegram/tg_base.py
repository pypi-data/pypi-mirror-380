from mg_alerts.telegram import tg_config as tg_conf
import requests
import os


class Tg:
    def __init__(self, crm_id, parse_mode=None, api_key=None):
        try:
            self.set_base_uri(crm_id)
        except KeyError:
            self._base_uri = None
        self._post_data = {}
        if parse_mode:
            self._post_data['parse_mode'] = parse_mode

    def _send(self):
       return requests.get(self._base_uri, params=self._post_data)

    def send(self):
        return self._send()

    def set_base_uri(self, crm_id, api_key=None):
        try:
            self._base_uri = f"https://api.telegram.org/bot{api_key if api_key else tg_conf.API_KEY[crm_id]}"
        except KeyError:
            self._base_uri = None
        return self


class Chat(Tg):
    def __init__(self, crm_id, msg, parse_mode=None, is_central=False, is_client=True,  **kw):
        Tg.__init__(self, crm_id, parse_mode)
        if is_client:
            try:
                self._base_uri += "/sendMessage"
            except (AttributeError, TypeError):
                self.set_base_uri(crm_id)
                self._base_uri += "/sendMessage"
            self._post_data['chat_id'] = tg_conf.CHAT_ID[crm_id]
        self._post_data['text'] = msg
        self._is_central = is_central
        self._is_client = is_client

    def send(self):
        res = None
        if self._is_client:
            res = self._send()
        if self._is_central:
            self._post_data['chat_id'] = tg_conf.CENTRAL_CHAT_ID
            self._base_uri = f"https://api.telegram.org/bot{tg_conf.CENTRAL_API_KEY}/sendMessage"
            self._post_data['text'] = f"""
<b>PROJECT:</b> {os.environ.get('_PROJECT_ID')}
{self._post_data['text']}"""
            res = self._send()
        return res


class GetUpdates(Tg):
    def __init__(self, crm_id, api_key):
        Tg.__init__(self, crm_id, api_key=api_key)
        try:
            self._base_uri += "/getUpdates"
        except:
            self.set_base_uri(crm_id)
            self._base_uri = f"{str(self._base_uri)}/getUpdates"


    def get_chat_id(self):
        res = self._send()
        r = res.json()
        try:
            return [o for o in r['result'][0].values() if isinstance(o, dict)][0]['chat']['id']
        except Exception as e:
            print(str(e))
            return None

