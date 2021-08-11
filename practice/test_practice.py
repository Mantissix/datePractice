import pytest
import yaml
import calculator

cal = calculator.calculator()


class TestCalculator:
    def setup_class(self):
        print('开始计算')

    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize('x, y', yaml.safe_load(open('../testData/testData1.yml')))
    def test_add(self, x, y):
        assert cal.add(x, y)

    @pytest.mark.parametrize('x, y', yaml.safe_load(open('../testData/testData1.yml')))
    def test_sub(self, x, y):
        assert cal.sub(x, y)

    @pytest.mark.parametrize('x, y', yaml.safe_load(open('../testData/testData1.yml')))
    def test_multiply(self, x, y):
        assert cal.multiply(x, y)

    @pytest.mark.parametrize('x, y', yaml.safe_load(open('../testData/testData1.yml')))
    def test_division(self, x, y):
        assert cal.division(x, y)

