from random import randint


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView
from form import form

from ITW.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm
from userextend.models import UserExtend


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = UserExtend
    form_class = UserExtendForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        # TRIMITEM MAIL CU TAMPLATE UL FACUT DE NOI

        if form.is_valid() and not form.errors:
            new_user = form.save()

            detailst_user = {
                'user': new_user,
                'username': new_user.username
            }
            subject = 'Creatd a new account!'
            message = get_template('userextend/mail_create_new_user.html').render(detailst_user)
            from_email = EMAIL_HOST_USER
            email_to = [new_user.email]

            email = EmailMessage(subject, message, from_email, email_to)
            email.content_subtype = 'html'  # main content is now text/html
            email.send()

        return redirect('homepage')

        # SCRIEM DOAR UN TEXT IN MAILUL TRIMIS CATRE USER

        # if form.is_valid() and not form.errors:
        #     new_user = form.save(commit=False)    # sa nu-mi salveze pana cand nu standardizez modul cum e scris
        #                                             # numele utilizatorului
        #     new_user.first_name = new_user.first_name.title  # daca userul cand creeaza cont isi scrie numele cu litera
        #                                              # mica, title imi va salva in baza de date numele cu litera mare
        #     new_user.last_name = new_user.last_name.title
        #     new_user.save()     # imi va salva datele in tabela
        #
        #     subject = 'Created a new account!'
        #     message = f'Hello, {new_user.first_name} {new_user.last_name}. Your account was successfully created.'
        #     from_email = EMAIL_HOST_USER
        #     to_email = [new_user.email]
        #
        #     send_mail(subject, message, from_email, to_email)
        #
        # return redirect('homepage')

# PENTRU A GENERA AUTOMAT UN USERNAME DUPA CE UTILIZATORUL ISI TRECE FIRST NAME SI LAST NAME

    # if form.is_valid() and not form.errors:
    #     new_user = form.save(commit=False)
    #     new_user.first_name = new_user.first_name.title() # cu litera mare la inceput
    #     new_user.last_name = new_user.last_name.title()
    #     new_user.username = f'{new_user.first_name.lower()}{new_user.last_name.lower()}_{randint(100000,1000000)}'
    #     form.save()
    #
    #     subject = 'Created a new account!'
    #     message = f'Hello, {new_user.first_name} {new_user.last_name}.' \
    #             f'Your account is created with user: {new_user.username}'
    #     from_email = EMAIL_HOST_USER
    #     email_to = [new_user.email]


