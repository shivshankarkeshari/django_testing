# from mixer.backend.django import mixer
import pytest

# @pytest.mark.django_db
class TestModels:
    def test_pdt_is_in_stock(self):
        pass
        # pdt = mixer.blend('testing.models.Products', quantity=1)
        # assert pdt.is_in_stock == True
#
#         def test_pdt_is_not_in_stock(self):
#             pdt = mixer.blend('testing.models.Products', quantity=0)
#             assert pdt.is_in_stock == False
#
