from pyopencell.resources.access import Access


class AccessService:
    """
    Model to execute the bussines logic of Som Connexio
    working with the Access model of PyOpenCell
    """

    def __init__(self, subscription):
        self.subscription = subscription

    def create_access(self, access_code):
        subscription_code = self.subscription.subscription.code
        Access.create(**{"code": access_code, "subscription": subscription_code})

    def terminate_access(self, access_code):
        subscription_code = self.subscription.subscription.code
        Access.delete(access_code, subscription_code)
