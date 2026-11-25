import pytest

class Test_fixture_all_annote:
    
    @pytest.fixture(scope="class",autouse=True)
    def setup_before_class(self):
            print("before class")
            yield 
            print("after class")
    @pytest.fixture(autouse=True)
    def setup_before_method(self):
        print("before method")
        yield 
        print("after method")

    @pytest.mark.skip()
    def test_1(self):
        print("this is test 1")

    feature=True
    @pytest.mark.skipif(not feature,reason="feature not available")
    def test_3(self):
         print("this is test 3")
    def test_2(self):
        print("this is test 2")

    @pytest.mark.smoke
    def test_4(self):
         print("this is smoke test")

    @pytest.mark.regression
    def test_5(self):
           print("this is regression test")