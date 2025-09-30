
from models.db import Db


class TrafficAlertLog(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'alerts', 'traffic_alert_log')
        self.crm_id = crm_id

    def log_alert(self, type, click_id, msg, **kw):
        self.insert([dict(type=type, click_id=click_id, message=msg, **kw)], return_id=True)


class ProcessingAlertLog(Db):
    def __init__(self, db, crm_id):
        Db.__init__(self, db, 'alerts', 'processing_alert_log')
        self.crm_id = crm_id

    def log_alert(self, type,  msg, **kw):
        self.insert([dict(type=type,  message=msg, **kw)], return_id=True, check_cols=True)