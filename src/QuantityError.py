class QuantityError(Exception):
    def __init__(self, massege=None):
        super().__init__(massege)