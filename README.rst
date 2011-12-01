========
Overview
========

**Easy to use, class based email for Django.**


The problem
===========
There is no unified way in our Django projects to send email. Django's own email functions require too much boilerplate
code and are not intelligent enough. They are also not class based.

Sending email should be as easy as creating an instance of the email class, provide one piece of text, and calling the
send() method. This is the easiest, most common case. It should also be possible to override base templates,
give separate text- and html versions, send the mail to a queue, etc.


What this class will do for you
===============================
- It will send text email if:

  1. there is a custom text template, or

  2. when using default templates, if text_body is set

- It will send html email if:

  1. there is a custom html template, or

  2. when using default templates, if html_body is set

- You can also force to send a text email when there is only a html_body. It will then convert html to text for you.

- You can also force to send a html email when there is only a text_body. It will then convert text to html for you.


What it doesn't do
==================
This email class doesn't know about mail queues. You can use a custom email backend or a project like
https://github.com/jtauber/django-mailer for that.


Installation
============
::

    $ pip install django-generic-mail


Usage
=====
::

    from generic_mail import Email

    # This will send text email only, uses the email/base_text_email.html template with the "body" template variable
    email = Email('to@example.com', 'Subject', 'Line one\n\nLine two')
    email.send()

    # This will send text- and html email, also with default template
    email = Email('to@example.com', 'Subject', 'Line one\n\nLine two', '<p>Line one</p><p>Line two</p>')
    email.send()

    # This will send text- and html email, will convert text to html using Markdown
    email = Email('to@example.com', 'Subject', 'Line one\n\nLine two')
    email.send(text=True, html=True)

    # This will send html email only
    email = Email('to@example.com', 'Subject', html_body='<p>Line one</p><p>Line two</p>')
    email.send()

    # This will send text- and html email, will convert html to text by removing html tags, converting paragraphs and breaks
    email = Email('to@example.com', 'Subject', html_body='<p>Line one</p><p>Line two</p>')
    email.send(text=True, html=True)

    # This will send text email only, since there is no body given, the text must be in the templates
    email = Email('to@example.com', 'Subject', text_template='email/my_text_email.html')
    email.send()

    # This will send html email only, since there is no body given, the text must be in the templates
    email = Email('to@example.com', 'Subject', html_template='email/my_html_email.html')
    email.send()

    # This will send text- and html email, since there is no body given, the text must be in the templates
    email = Email('to@example.com', 'Subject', text_template='email/my_text_email.html', html_template='email/my_html_email.html')
    email.send()

    # This will generate an error: when proving only one custom template, you can't send both email versions
    email = Email('to@example.com', 'Subject', html_template='email/my_html_email.html')
    email.send(text=True, html=True)

    # This will generate an error: when using default templates, you need to give at least one body (text or html)
    email = Email('to@example.com', 'Subject')
    email.send()


Subclassing
===========
If you want to create your own subclass that has different defaults (other templates, subject, etc), the best way to do
this is by changing the class properties instead of overriding the ``__init__`` method.
