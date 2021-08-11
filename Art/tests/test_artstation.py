import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse, resolve
import json
from django.http import HttpRequest


from Art.models import Post, Artes, Jobs
from Art.views import *
from django.contrib.auth import get_user_model
from Art.forms import PostForm, ArteForm, JobsForms, MensagemForms



User = get_user_model()

def createArt(autor):
    time = timezone.now()
    return Artes.objects.create(artistas='Evelin K.', titulo = 'Test Art', descricao = 'This is a test art description', created_date = time, autor = autor)

class ArtIndexViewTests(TestCase):
    def test_should_be_able_to_buy_one_art(self):

        user = User.objects.create(cpf = '123456789', username = 'evelin', email = 'evelin@evelin.com.br', password = '1123456789')
        art = createArt(user)
        self.assertIsNotNone(art)
        user2 = User.objects.create(cpf = '9876545321', username = 'evelin2', email = 'evelin2@evelin.com.br', password = '1123456789')
        self.client.force_login(user2)
        url = reverse('arts:confirm', kwargs={'pk':art.pk})
        response = self.client.post(url, data={'email':'evelin2@evelin.com.br'})
        self.assertEquals(response.status_code, 302)



    def test_should_be_able_to_create_one_new_art(self):

        user3 = User.objects.create(cpf = '555444666', username = 'evelin3', email = 'evelin3@evelin.com.br', password = '1123456789')
        self.client.force_login(user3)
        url = reverse('arts:post_new')
        response = self.client.post(url, {"titulo": 'Teste',"artistas": "Evelin K.","descricao": "Descricao teste"})
        self.assertEquals(response.status_code, 302)




if __name__ == '__main__':
  unittest.main()

