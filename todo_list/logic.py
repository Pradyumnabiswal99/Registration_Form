from django.core.mail import send_mail,EmailMultiAlternatives


def mail_sending(reciver_mail,name):
    subject = "Registration on STACKFUSION"
    from_email = "STACKFUSION"
    to_email = [reciver_mail]
    mail_message = """Dear {},\nYOUR REGISRATION ON STACKFUSION IS SUCCESSFUL.""".format(name)

    #text_content = 'Welcome to To Do App'

    # message=EmailMultiAlternatives(subject=subject,body=text_content,from_email=from_email,to=to_email)
    # html_template=get_template('message.html').render()
    # message.attach_alternative(html_template,"text/html")
    # message.send()
    send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=mail_message,fail_silently=False)