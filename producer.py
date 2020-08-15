from sms.tasks import send_sms

if __name__ == '__main__':
    send_sms.delay('ali', 'sign', 'content', 'phones')
    send_sms.apply_async(args=('ali', 'sign', 'content', 'phones'), countdown=10)