from django.core.mail import send_mail
import string, random
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from users.models import CustomUser
from .serializers import CustomUserSerializer

@api_view(('GET',))
def email_valid(request):
    length = 10
    letters = string.ascii_letters
    confirmation_code = ''.join(random.choice(letters) for i in range(length))
    email = request.GET.get('email')
    if (email is not None) and (
            CustomUser.objects.filter(email=email).count() != 1):
        CustomUser.objects.create(email=email,
                                  confirmation_code=confirmation_code)
        send_mail(
            'Тема письма',
            f'Ваш код подтверждения {confirmation_code}.',
            'api_yamdb@mail.com',  # Это поле "От кого"
            [f'{email}'],  # Это поле "Кому" (можно указать список адресов)
            fail_silently=False,  # Сообщать об ошибках
        )
        serializer = CustomUserSerializer(CustomUser.objects.get(email=email))
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
