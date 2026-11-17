import pytest

class TestPytestAllAnnotation:

    @pytest.fixture(scope="class",autouse=True)
    def setup_beforeclass(self):
         print("before class")
         yield
         print("after class")

    @pytest.fixture(autouse=True)
    def setup_method_level(self):
        print("before method")
        yield
        print("after method")

    @pytest.mark.skip
    def test1(self):
        print("Test 1")


    def test2(self):
        print("TEst 2")

    