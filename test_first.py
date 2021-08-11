import pytest
import yaml


def func(x):
    return x + 1


# 参数化，可将测试数据设置为外部参数，并传入
@pytest.mark.parametrize('x, y', yaml.safe_load(open('./testData/testData1.yml')))
def test_answer(x, y):
    assert func(x) == y


# 当一个方法加上pytest.fixture()，就可以在后续的测试方法中进行调用
@pytest.fixture()
def demo1():
    print("自我介绍")
    demo1 = "This is demo1"


class TestDemo:
    # 调用经过pytest.fixture()装饰过的方法，会先运行该方法，再运行测试方法
    def test_practice1(self, demo1):
        print(f'This is a demo')

    def test_practice2(self):
        print('This is a demo2')

    def test_practice3(self, demo1):
        print(f'This is a demo3')


# 在python解释器下运行pytest
# if __name__ == '__main__':
#     pytest.main(['test_first.py::TestDemo::test_practice1', '-v'])
