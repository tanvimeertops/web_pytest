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

    feature_available=True
    @pytest.mark.skipif(not feature_available,reason="feature not available")
    def test4(self):
        print("test 3")

    def test2(self):
        print("TEst 2")

    @pytest.mark.smoke
    def test3(self):
        print("smoke test")

    
    