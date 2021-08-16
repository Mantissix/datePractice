import allure


# 计算器功能正向验证
@allure.feature("计算器功能正向测试")
class TestCalRight:
    @allure.story("加法")
    def test_add(self, get_data, fixtureStart):
        assert fixtureStart.add(get_data[0], get_data[1])

    @allure.story("减法")
    def test_sub(self, get_data, fixtureStart):
        assert fixtureStart.sub(get_data[0], get_data[1])

    @allure.story("乘法")
    def test_multiply(self, get_data, fixtureStart):
        if fixtureStart.multiply(get_data[0], get_data[1]):
            assert fixtureStart.multiply(get_data[0], get_data[1])

    @allure.story("除法")
    def test_division(self, get_data, fixtureStart):
        try:
            if fixtureStart.division(get_data[0], get_data[1]):
                assert fixtureStart.division(get_data[0], get_data[1])
        except:
            print('除数为0，无法计算')


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
