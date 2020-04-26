from django.test import RequestFactory
from django.urls import reverse
# from mixer.backend.django import mixer
from django.contrib.auth.models import User, AnonymousUser
from testing.views import pdt_dtls



class TestViews:
    def test_pdt_dtl_auth(self):
        path = reverse('details', kwargs={'pk': 1})
        request = RequestFactory().get(path)
        # request.user = mixer.blend('User')
        # response = pdt_dtls(request, pk=1)
        # assert response.status_code == 200

    def test_pdt_dtl_unauth(self):
        pass


# Generate a few pieces
# messages = mixer.cycle(4).blend('someapp.message')
