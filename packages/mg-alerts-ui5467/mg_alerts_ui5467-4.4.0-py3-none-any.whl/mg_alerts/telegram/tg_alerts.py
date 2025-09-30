from .tg_base import Chat
import datetime as dt
from mg_alerts import alert_models as am


def traffic_alert_log(db, ref, method):
    def _alert_ins(crm_id, msg, **kw):
        try:
            am.TrafficAlertLog(db, crm_id).log_alert(**kw)
        except TypeError:
            print(' WARNING DB not referenced in Alerting Module')


def processing_traffic_alert(db, ref, method):
    def _alert_ins(crm_id, msg, click_id, **kw):
        try:
            am.ProcessingAlertLog(db, crm_id).log_alert(click_id=click_id, msg=msg, **kw)
        except TypeError:
            print(' WARNING DB not referenced in Alerting Module')


class Alert(Chat):
    def __init__(self, crm_id, msg, parse_mode=None, **kw):
        Chat.__init__(self, crm_id, msg, parse_mode, **kw)

    @staticmethod
    def parse_mid_number(mid_number):
        if isinstance(mid_number, list):
            if isinstance(mid_number[0], dict):
                return '\n          '.join([f"{m['crm_id']}: {m['mid_number']}" for m in mid_number])
            return ' '.join(mid_number)
        elif isinstance(mid_number, dict):
            return f"{mid_number['crm_id']}: {mid_number['mid_number']}"
        elif isinstance(mid_number, (int, float, str)):
            return mid_number

    @classmethod
    def gateway_disabled(cls, crm_id, gateway_id, mid_number='', reason='disabled', processor='', corporation_name='',
                         declines=[], **kwargs):
        decs = ''
        if declines:
            decs = 'recent declines \n' + '\n'.join(declines)

        msg = f"""<b>GATEWAY DISABLED</b>
<pre>{crm_id}
{corporation_name} {processor} 
gateway: {gateway_id} 
mid_number: {mid_number}
reason: {reason}
re-enable after review.

{decs}</pre>        
          """
        return cls(crm_id, msg, 'HTML')

    @classmethod
    def vaultx_cap(cls, crm_id, gateway_id, mid_number, reason, processor='', corporation_name='', declines=[],
                   **kwargs):
        decs = ''
        if declines:
            decs = 'recent declines \n' + '\n'.join(declines)

        msg = f"""VAULTX INITIAL HARD DECLINE
                  {crm_id}
                  {corporation_name} {processor} 
                  gateway: {gateway_id} 
                  mid_number: {mid_number}
                  reason: {reason}

        {decs}        
        """
        return cls(crm_id, msg)

    @classmethod
    def missing_gateways(cls, crm_id, gateway_ids, order_count, start_date, **kwargs):
        msg = f"""<b>MISSING GATEWAYS</b>
<pre>
gateways {','.join(gateway_ids)} are missing from corp structure. 
{order_count} subscriptions starting from {start_date} will not be processed until this is rectified.                  
</pre> 
        """
        return cls(crm_id, msg, 'HTML')

    @classmethod
    def missing_campaigns(cls, crm_id, campaign_ids, order_count, start_date, **kwargs):
        msg = f"""**MISSING CAMPAIGNS FROM OFFERS**
                        The following {','.join(campaign_ids)} not assigned to an offer. 
                      {order_count} subscriptions starting from {start_date} will not be processed until this is rectified.                  
            """
        return cls(crm_id, msg)

    @classmethod
    def dead_mid_cascade_alerts(cls, crm_id, gateway_ids, today_tot, total, **kwargs):
        msg = f"""CASCADE WARNING:                  
                   The following closed gateways {','.join(gateway_ids)} 
                   Will attempt {today_tot} cascades today.  {total} orders remain.
                   At the current cascade intake rate these cascades will complete on {dt.datetime.now() + dt.timedelta(days=int(total / today_tot))}

                """
        return cls(crm_id, msg)

    @classmethod
    def soft_cap_alert(cls, crm_id, **kwargs):
        msg = f"""
<b>{crm_id}  IS CAPPED FOR DAY</b>
<pre>Orders will continue to be processed until cap for month is full</pre>  
"""
        return cls(crm_id, msg, 'HTML')

    @classmethod
    def hard_cap_alert(cls, crm_id, gateway_id, cc_type=None, **kwargs):
        cc = f"for cc_type: {cc_type}" if cc_type else ""
        return cls(crm_id, f"""
<b>GATEWAY DISABLED HARD CAP</b>
<pre>
Gateway {gateway_id} on {crm_id} {cc} has reached max initials for the month and is disabled.
</pre> 
""", 'HTML')

    @classmethod
    def fraud_alert(cls, crm_id, order_id, msg, affid="", provider="", click_id="", c3=None, C3=None, **kwargs):
        msg = f"""
<b>FRAUD ALERT</b>
<pre>  
CRM:     {crm_id}
Order#:  {order_id}
Network: {provider}
Pub:     {affid}
 Sub Affiliate: {c3 if c3 else C3}  
Click ID: {click_id}
{msg}
</pre>        
        """
        return cls(crm_id, msg, 'HTML')

    @classmethod
    def bad_decline(cls, crm_id, order_id, decline_reason, provider="", offer_id="", **kwargs):
        return cls(crm_id, f"""
<b>BAD DECLINE ALERT</b>
<pre>
CRM:     {crm_id}
Order#:  {order_id}
Network: {provider}
OfferID: {offer_id}

{decline_reason}
</pre>        
        """, parse_mode='HTML')

    @classmethod
    def email_fraud(cls, crm_id, order_id, email, **kwargs):
        return cls.fraud_alert(crm_id, order_id, f" email address <b>{email}</b> is potential fraud", **kwargs)

    @classmethod
    def email_auto_decline(cls, crm_id, email, **kwargs):
        return cls.fraud_alert(crm_id, 'None', f" email address <b>{email}</b> was auto declined", **kwargs)

    @classmethod
    def invalid_price_alert(cls, crm_id, offer_id, price, **kwargs):
        return cls(crm_id, f"""
<b>ORDER AUTO DECLINED - INVALID PRICE</b>
<pre>
 CRM: {crm_id}
 Offer ID: {offer_id}
 price: {price}
</pre>
""",
                   'HTML'
                   )

    @classmethod
    def duplicate_customer(cls, crm_id, email, order_id='', auto_decline=False, **kwargs):
        return cls.fraud_alert(crm_id, 'None',
                               f"Customer {'Auto declined' if auto_decline else str(order_id)}: email address <b>{email}</b> has already purchased something.",
                               **kwargs)

    @classmethod
    def address_fraud(cls, crm_id, order_id, s_state, ip_state, **kwargs):
        return cls.fraud_alert(crm_id, order_id, f" ship state {s_state} and ip state {ip_state} differ", **kwargs)

    @classmethod
    def pub_blacklist(cls, crm_id, offer_id, provider, affid, c3=None, C3=None, **kwargs):
        return cls(crm_id, f"""
<b>SUBMISSION BY BLACKLISTED PUB</b>
<pre>
 CRM: {crm_id}
 Offer ID: {offer_id}
 Provider:{provider}
 Affid: {affid}
 Sub Affiliate: {c3 if c3 else C3}  
</pre>
""", 'HTML')

    @classmethod
    def sub_pub_blacklist(cls, crm_id, offer_id, provider, c3=None, C3=None, **kwargs):
        return cls(crm_id, f"""
    <b>SUBMISSION BY BLACKLISTED SUB AFFILIATE </b>
    <pre>
     CRM: {crm_id}
     Offer ID: {offer_id}
     Provider:{provider}
     Sub Affiliate: {c3 if c3 else C3} 
    </pre>
    """, 'HTML')

    @classmethod
    def circut_breaker_error(cls, crm_id, error, **kwargs):
        msg = f"""PROCESSING CIRCUIT BREAKER TRIGGERED
                      Processor Halted on {crm_id}
                      reason: {error}
                      please report to Developer
            """
        return cls(crm_id, msg)

    @classmethod
    def monthly_cap_pct(cls, crm_id, corporation_name, processor, mid_id, step, trigger_level, used_monthly_cap,
                        monthly_cap, mid_numbers, enable_initials, **kwargs):
        msg = f"""MONTHLY MID CAP LEVEL WARNING
                      {corporation_name} - {processor} 
                      mid_id {mid_id} - step {step}
                      {cls.parse_mid_number(mid_numbers)}
                      less than {trigger_level}% cap remaining.
                      Cap Used: {used_monthly_cap}
                      Total  Cap: {monthly_cap}
                      Enable Initials   {str(enable_initials)} 


            """
        return cls(crm_id, msg)

    @classmethod
    def daily_cap(cls, crm_id, mid_number, gateway_id, corporation_name, processor, mid_id, step, used_daily_cap,
                  **kwargs):
        msg = f"""DAILY REBILL CAP REACHED
                      {crm_id}
                      {corporation_name} - {processor} 
                      mid: {mid_id}  
                      step: {step}
                      Gateway: {gateway_id}
                      Mid Number: {mid_number}  
                      Cap Used: {used_daily_cap}
                      Remaining orders deferred 1 day
            """
        return cls(crm_id, msg)

    @classmethod
    def daily_transaction_cap(cls, crm_id, corporation_name, processor, mid_id, step, used_dtc,
                              **kwargs):
        msg = f"""DAILY Transaction CAP REACHED
                        {corporation_name} - {processor} 
                        mid_id {mid_id} - step {step}
                        Cap Used: {used_dtc}
                        Remaining orders deferred 1 day
              """
        return cls(crm_id, msg)

    @classmethod
    def global_monthly_cap_pct(cls, crm_id, trigger_level, used_monthly_cap, monthly_cap, **kwargs):
        msg = f"""MONTHLY COMBINED CAP LEVEL WARNING                          
                         less than {trigger_level}% cap remaining.
                         Cap Used: {used_monthly_cap}
                         Total Cap: {monthly_cap}                         
               """
        return cls(crm_id, msg)

    @classmethod
    def trailing_cc_type_cap(cls, crm_id, mid_numbers, corporation_name, processor, mid_id, step, cc_type,
                             trailing_30_cap, used_tc, **kwargs):
        msg = f"""<b>TRAILING 30 DAY CAP REACHED</b>
                    <pre>
                        {corporation_name} - {processor} 
                        mid_id {mid_id} - step {step}
                        {cls.parse_mid_number(mid_numbers)}
                        cc_type: {cc_type.upper()}
                        Cap Limit: {trailing_30_cap}
                        Cap Used: {used_tc}
                        Remaining orders deferred 1 day
                    </pre>
              """
        return cls(crm_id, msg, parse_mode='HTML')

    @classmethod
    def trailing_cap(cls, crm_id, mid_numbers, corporation_name, processor, mid_id, step, trailing_30_cap,
                     used_tc, **kwargs):
        msg = f"""<b>TRAILING 30 DAY CAP REACHED</b>
                    <pre>
                           {corporation_name} - {processor} 
                           mid_id {mid_id} - step {step}
                           {cls.parse_mid_number(mid_numbers)}                   
                           Cap Limit: {trailing_30_cap}
                           Cap Used: {used_tc}
                           Remaining orders deferred 1 day
                    </pre>
                 """
        return cls(crm_id, msg, parse_mode='HTML')

    @classmethod
    def database_lag(cls, crm_id, time):
        return cls(crm_id, f"""CRM LAG ALERT
                'CRM:' {crm_id}
                'Last Update' : {time}
                 Rebiller paused. 
        """)

    @classmethod
    def database_resume(cls, crm_id):
        return cls(crm_id, f"""CRM RESUMED ALERT
                 'CRM:' {crm_id}
                  Rebiller resumed. 
         """)

    @classmethod
    def orders_server_down(cls, email, crm_id, time):
        return cls(crm_id, f"""ORDER API SERVER IS DOWN!
         CRM: {crm_id}
         Email: {email}
         Date : {str(time.date())}
         Time : {str(time.time())}
         Please Contact Developers. 
         """)

    @classmethod
    def initials_cc_type_cap_mtd(cls, crm_id, cc, alert_level, remaining_mtd_cap, **kw):
        return cls(crm_id, f"""INITIALS MTD CAP ALERT
            cc: {cc}
            threshold: {int(alert_level)}
            remaining: {int(remaining_mtd_cap)} 
            """)

    @classmethod
    def test(cls, crm_id):
        return cls(crm_id, f"""THAT WAS A TEST ALERT

               """)

    @classmethod
    def low_initials_approval(cls, crm_id, gateway_id, corporation_name, processor, approval_rate, dly_min_approval,
                              **kwargs):
        return cls(crm_id, f""" <b>PAYMENT ROUTER LOW APPROVAL RATE</b>
                              <pre>
                              CRM: {crm_id}
                              {corporation_name} - {processor}                                 
                              Gateway ID: {gateway_id}
                              Minimum Approval%": {dly_min_approval}                   
                              Approval Rate: {approval_rate}
                              Gateway has been paused for the rest of the day. To re-enable  Daily Min Approval rate must be dropped first. 
                             </pre>
                    """, parse_mode='HTML')

    @classmethod
    def low_pub_approval(cls, crm_id, provider, affid, sub_affiliate, order_count, approval_rate, **kwargs):
        return cls(crm_id, f""" 
<b>FRAUD ALERT - POTENTIAL ATTACK - LOW PUB APPROVAL RATE - </b>
<pre>                         
Provider: {provider}
AFFID: {affid}
Sub AFF: {sub_affiliate}
24 Hour Order Count: {order_count}
Approval Rate: {approval_rate}
This might be an attack. Blacklist the pub or sub and review. 
</pre>
 """, parse_mode='HTML')

    @classmethod
    def out_of_processing(cls, crm_id, cc_type, decline, is_prepaid=False, **kw):
        if is_prepaid:
            ct = "prepaid Cards and bin pause"
        else:
            ct = "cards that are not prepaid"
        return cls(crm_id,
                   f"""
<b>URGENT: PAYMENT ROUTER OUT OF PROCESSING</b>
<pre>

    CRM: {crm_id}
    CC Type: {cc_type.upper()}
    Decline: {decline}
    Is Card Treated as Prepaid: {str(is_prepaid)}
    Orders are auto-declining for {ct}. Orders are not being saved or queued. Check the payment router settings to ensure you have enough mids for the outlined circumstance.
</pre>
""",
                   parse_mode='HTML'
                   )

    @classmethod
    def service_error_log_alert(cls, crm_id, status_code, function, end_point, error_text,
                                user_suggestion='Contact Support', trace_back='None', **kw):
        return cls(crm_id, f"""
<b>SERVICE DOWN</b>
<pre>
    Service: {function}
    Status Code: {status_code}
    Url: {end_point}
    Error: {error_text}      
    Recommended Action: {user_suggestion}
    Additional Info: {trace_back}    
</pre>
""",
                   parse_mode='HTML'
                   )

    @classmethod
    def service_error_log_alert_central(cls, crm_id, status_code, function, end_point, error_text,
                                        user_suggestion='Contact Support', trace_back_query=None, **kw):
        return cls(crm_id,
                   f"""<b><a href="https://console.cloud.google.com/logs/query;query={trace_back_query}"> Logging Traceback Information</a></b>    
<pre>
    <b>SERVICE ERROR</b>
    Service: {function}
    Status Code: {status_code}
    Url: {end_point}
    Error: {error_text}      
    Recommended Action: {user_suggestion}

</pre>
""",
                   parse_mode='HTML',
                   is_central=True,
                   is_client=False,

                   )
