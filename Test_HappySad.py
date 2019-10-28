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

    def test_funHappyNumber(self):
        num = 7
        response = HsControll.fun(num)
        assert response["bool"] == True

    def test_funHappyNumberStringResult(self):
        num = 7
        response = HsControll.fun(num)
        assert response["string"] == '{}!'.format(str(num) + " is a happy number") 

    def test_funSadNumber(self): 
        num = 99
        response = HsControll.fun(num)
        assert response["bool"] == False

    def test_funSadNumberStringResult(self):
        num = 99
        response = HsControll.fun(num)
        assert response["string"] == '{}!'.format(str(num) + " is not a happy number") 




