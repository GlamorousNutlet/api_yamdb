from django.shortcuts import render
from django.core.mail import send_mail
import string, random
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from django.contrib.auth.models import User

@api_view(('GET',))
def email_valid(request):
    length = 10
    letters = string.ascii_letters
    confirmation_code = ''.join(random.choice(letters) for i in range(length))
    email = request.GET.get('email')
    if (email is not None) and (User.objects.filter(email=email).count() != 1):
        User.objects.create(email=email)
        send_mail(
            'Тема письма',
            f'Ваш код подтверждения {confirmation_code}. Его необходимо отправить на /auth/token/',
            'api_yamdb@mail.com',  # Это поле "От кого"
            [f'{email}'],  # Это поле "Кому" (можно указать список адресов)
            fail_silently=False,  # Сообщать об ошибках («молчать ли об ошибках?»)
        )

        return Response(status=status.HTTP_201_CREATED)
    Usr = User.objects.get(email=email)
    Usr.delete()
    return Response(status=status.HTTP_400_BAD_REQUEST)
