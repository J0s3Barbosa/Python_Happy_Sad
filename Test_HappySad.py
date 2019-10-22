import pytest
import HappySad as HsControll

class TestClass:
    def test_HappyNumber(self):
        num = 7
        response = HsControll.isHappySadNumber(num)
        assert response == True

    def test_SadNumber(self):
        num = 99
        response = HsControll.isHappySadNumber(num)
        assert response == False
 



