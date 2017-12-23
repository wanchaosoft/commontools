# coding=utf-8

"""django.email usage"""

from django.core.mail import send_mail

FROM_EMAIL = 'huacnlee@foxmail.com'

MAIL_FOOT = u'''<br/><br/><br/>
Me.<br/>
<a href="http://www.example.com">example.com</a>'''


def send_register_success_mail(userinfo):
    """

    :param userinfo:
        {
            'username': '',
            'password': '',
            'email': '',
            'realname': '',
        }
    :return:
    """
    subject = u'注册成功'
    body = u'''你好！<b>%s</b><br />
    你已经成功注册成为Tmitter用户<br />
    以下是您的信息：<br />
    <ul>
        <li>用户名：%s </li>
        <li>密码:%s</li>
    </ul>''' % (userinfo['realname'], userinfo['username'], userinfo['password'])
    recipient_list = [userinfo['email']]
    send(subject, body, recipient_list)


def send(subject, body, recipient_list):
    body += MAIL_FOOT
    """send_mail parameter example."""
    send_mail(subject, body, FROM_EMAIL, recipient_list, fail_silently=True)


def test(request):
    send_register_success_mail(
        {
            'username': 'huacnlee',
            'password': '123123',
            'email': 'huacn@qq.com',
            'realname': 'Jason Lee',
        }
    )