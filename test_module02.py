class Test_module02():

    def test_type(self):
        assert type(2) == int

    def test_str(self):
        assert str.upper("python") == 'PYTHON'
        assert "hello".capitalize() == "Hello"