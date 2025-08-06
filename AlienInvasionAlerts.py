class OutOfShipsAlert(Exception):
    """An alert treated like an error to say Out of ships"""
    def __init__(self, message='Game over. Out of ships!'):
        self.message = message
        super().__init__(self.message)
        