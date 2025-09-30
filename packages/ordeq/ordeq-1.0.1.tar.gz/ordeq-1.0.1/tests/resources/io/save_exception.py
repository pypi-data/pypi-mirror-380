from ordeq import Output


class MockExceptionIO(Output):
    def save(self, df):
        raise Exception("Some save exception")


mock = MockExceptionIO()
mock.save(None)
