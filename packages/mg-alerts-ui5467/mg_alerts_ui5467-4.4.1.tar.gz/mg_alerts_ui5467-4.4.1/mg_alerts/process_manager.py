import api
from controllers.process_pool import ProcessPool, Pq
from .telegram import Alert


class ProcessManager(ProcessPool):
    def __init__(self, pub_callback=False):
        ProcessPool.__init__(self)
        self.pub_callback = pub_callback

    def _publish(self, method, data={}):
        if callable(self.pub_callback):
            self.pub_callback(api.PubResponse('alerts', method).data(data))

    async def gateway_disabled(self, data, **kwargs):
        msg = f'Gateway {data["gateway_id"]} disabled: {data["reason"]}'
        print(msg)
        self._publish('gateway_disabled', {**data, **kwargs})
        Alert.gateway_disabled(**data, **kwargs).send()
        #self.tg_bot.send_message()

    def save_alert(self, user, app):
        self.pub_callback(api.PubResponse('save_alert', data={'user': user, 'app': app}))

    def cap_alert(self):
        pass

    def high_decline_alert(self):
        pass

    def processor_stop_alert(self):
        pass

    def settings_alert(self):
        pass

