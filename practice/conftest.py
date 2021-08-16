import pytest
import yaml

import calculator


# conftest.py文件放在项目下全局数据共享的地方，最好是放在项目根目录下
# 一般来说，conftest.py一般用来存放项目中的fixture方法
# conftest.py文件名字一定不能更换
# conftest.py文件就近生效（即如果在不同文件夹下，采取就近调用原则）
@pytest.fixture()
def fixtureStart():
    print("开始正向计算")
    # 在pytest当中，相当于激活了fixture的teardown操作，在yield后面的操作步骤，将被认为是teardown操作，
    # yield相当于return，能够返回数据，同时记录了上一次的执行位置，下一次继续执行
    cal = calculator.calculator()
    yield cal
    print("正向计算结束")


def getTestData():
    with open('../testData/testData1.yml') as data:
        data1 = yaml.safe_load(data)
        return data1


@pytest.fixture(params=getTestData())
def get_data(request):
    return request.param
