from app import app
from . import server


@app.task
def send_sms(method, sign, content, phones):
    try:
        result = False
        if method == 'ali':
            sv = server.AliServer(sign=sign, content=content, phones=phones)
            result = sv.send_sms()
        if result:
            return "短信发送成功"
        else:
            return "短信发送失败"
    except Exception as e:
        return "短信发送失败：%s" % e
