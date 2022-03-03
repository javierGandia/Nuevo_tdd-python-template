from app.rot13 import rot13


class TestClass:
    def test_rot13(self):
        assert rot13("aviones") == "nivbarf"
