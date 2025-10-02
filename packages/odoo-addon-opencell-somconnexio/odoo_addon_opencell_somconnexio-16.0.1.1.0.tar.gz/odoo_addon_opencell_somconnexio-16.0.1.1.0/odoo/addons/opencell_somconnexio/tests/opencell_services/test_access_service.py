from mock import Mock, patch

from odoo.tests import TransactionCase
from ...opencell_services.access_service import AccessService


class AccesServiceTests(TransactionCase):
    def setUp(self):
        super().setUp()
        self.subscription = Mock(spec=["subscription"])
        self.subscription.subscription = Mock(spec=["code"])
        self.subscription.subscription.code = "SUBSCRIPTION_CODE"

    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.access_service.Access",  # noqa
        spec=["create"],
    )
    def test_create_access(self, MockAccess):
        AccessService(self.subscription).create_access("ACCESS_CODE")
        MockAccess.create.assert_called_once_with(
            **{"code": "ACCESS_CODE", "subscription": "SUBSCRIPTION_CODE"}
        )
        assert True

    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.access_service.Access",  # noqa
        spec=["delete"],
    )
    def test_terminate_access(self, MockAccess):
        AccessService(self.subscription).terminate_access("ACCESS_CODE")
        MockAccess.delete.assert_called_once_with("ACCESS_CODE", "SUBSCRIPTION_CODE")
