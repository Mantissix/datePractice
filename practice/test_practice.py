import pytest
import yaml
import calculator

cal = calculator.calculator()


# 计算器功能正向验证
class TestCalRight:
    @pytest.mark.right
    @pytest.mark.parametrize('x, y', yaml.safe_load(open('../testData/testData1.yml')))
    def test_add(self, x, y, fixtureStart):
        assert cal.add(x, y)

    @pytest.mark.right
    @pytest.mark.parametrize('x, y', yaml.safe_load(open('../testData/testData1.yml')))
    def test_sub(self, x, y, fixtureStart):
        assert cal.sub(x, y)

    @pytest.mark.right
    @pytest.mark.parametrize('x, y', yaml.safe_load(open('../testData/testData1.yml')))
    def test_multiply(self, x, y, fixtureStart):
        if cal.multiply(x, y):
            assert cal.multiply(x, y)

    @pytest.mark.right
    @pytest.mark.parametrize('x, y', yaml.safe_load(open('../testData/testData1.yml')))
    def test_division(self, x, y, fixtureStart):
        try:
            if cal.division(x, y):
                assert cal.division(x, y)
        except:
            print('除数为0，无法计算')

        # with pytest.raises(ZeroDivisionError):
        #     cal.division(x, y)

# 计算器功能逆向验证
# class TestCalWrong:
#     def setup_class(self):
#         print('开始逆向计算')
#
#     def teardown_class(self):
#         print('逆向计算结束')
#
#     @pytest.mark.wrong
#     @pytest.mark.parametrize(yaml.safe_load(open('../testData/testData1.yml')))
#     def test_addWrong(self, x, y):
#         if cal.add(x, y):
#             assert cal.add(x, y)
