class RootoiBaseUnverifiedError(Exception):
    def __init__(self,message = "The Rootoi is not verified Please check your key"):
        self.err = message
        super().__init__(self.err)
class RootoiKeyUnverifiedError(Exception):
    def __init__(self,message = "The Rootoi Admin Key is not verified Please check your key"):
        self.err = message
        super().__init__(self.err)
class RootoiDictError(Exception):
    def __init__(self,message = "there should be an dictionary"):
        self.err = message
        super().__init__(self.err)
