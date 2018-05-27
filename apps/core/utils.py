import uuid
from django.template.loader import get_template
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from django.utils import timezone
from .serializers import ChangePasswordSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from .models import Confirmed


def mailing(email, user):
    ruta_confirmation = 'http://169.60.181.218:8000/api/v1/'
    template = 'mailing/emil_content.html'

    hash_send = get_random_string(length=32)
    Recover.objects.create(
        email=email,
        hash_time=hash_send
    )

    contexto = {
        'link': ruta_confirmation,
        'user': user,
    }

    template = get_template(template)
    html_content = template.render(contexto)
    msg = EmailMessage(
        u'Recuperacion de Contraseña',
        html_content,
        to=[email, ]
    )
    msg.content_subtype = "html"
    try:
        msg.send()
        return {'proccess': True}
    except Exception as e:
        return {'proccess': False, 'error:': str(e)}


def recover_pass(hash_uuid, request):
    if hash_uuid[-1] == '/':
        hash_uuid = hash_uuid[:-1]

    try:
        recover = Confirmed.objects.get(hash_time=hash_uuid)
    except Confirmed.DoesNotExist:
        return Response(
            {'error': 'Link no designado para confirmacion de apuesta'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if recover.created + timezone.timedelta(days=2) < timezone.localtime() \
            or not recover.is_active:
        return {'proccess': False, 'error': False}

    password = request.data.get('new_password', '')
    repeat_password = request.data.get('confirm_password', '')

    change_serializer = ChangePasswordSerializer(data={
        'password': password,
        'repeat_password': repeat_password,
    })

    if change_serializer.is_valid():
        recover.is_active = False
        recover.save()

        try:
            user = get_object_or_404(User, email=recover.email)
        except User.DoesNotExist:
            return Response(
                {'error': 'Erro en identificacion de usuario'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(repeat_password)
        user.save()
        return Response(
            {'message': 'Contraseña actualizada'}, status=status.HTTP_200_OK
        )
    else:
        return Response(
            {'error': 'Campo nulo o no coincidencia detectada'},
            status=status.HTTP_400_BAD_REQUEST
        )
