from odoo.tests import TransactionCase
from mock import Mock, patch, ANY
from faker import Faker
from ...opencell_services.crm_account_hierarchy_create_service import (
    CRMAccountHierarchyFromContractCreateService,
)
from ...opencell_services.opencell_exceptions import PyOpenCellException
from odoo.addons.somconnexio.tests.factories import ContractFactory
from ..factory import PartnerFactory, OpenCellConfigurationFactory
from pyopencell.exceptions import PyOpenCellAPIException


class OpenCellCustomerResource:
    """
    Represents an OpenCell Customer Resource.
    """

    def __init__(self, code, email=None, iban=None, customerAccounts=None):
        fake = Faker("es-ES")
        self.code = code
        self.email = email or fake.email()
        self.iban = iban or fake.iban()
        self.customerAccounts = customerAccounts or {
            "customerAccount": [
                {
                    "code": self.code,
                    "contactInformation": {
                        "email": self.email,
                    },
                    "methodOfPayment": [{"bankCoordinates": {"iban": self.iban}}],
                }
            ]
        }


class CRMAccountHierarchyFromContractCreateServiceTests(TransactionCase):
    def setUp(self):
        super().setUp()
        self.contract = ContractFactory()
        self.contract.partner_id.block_contract_creation_in_OC = False
        self.expected_email = "expected@email.com"
        self.expected_iban = "ES00 0000 0000 0000 0000"
        self.contract.email_ids = [PartnerFactory(self.expected_email)]
        self.contract.invoice_partner_id.mobile = False
        self.opencell_configuration = OpenCellConfigurationFactory()

    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_strategies.Customer",  # noqa
        spec=["get"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.Access",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.AccessFromContract",  # noqa
        return_value=Mock(spec=["to_dict"]),
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.Subscription",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.SubscriptionFromContract",  # noqa
        return_value=Mock(spec=["to_dict"]),
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.CRMAccountHierarchy",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.CRMAccountHierarchyFromContract",  # noqa
        return_value=Mock(spec=["to_dict", "code"]),
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.Customer",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.CustomerFromPartner",  # noqa
        return_value=Mock(spec=["to_dict"]),
    )
    def test_create_from_customer_to_subscription_hierarchy_in_opencell(
        self,
        MockCustomerFromPartner,
        MockCustomer,
        MockCRMAccountHierarchyFromContract,
        MockCRMAccountHierarchy,
        MockSubscriptionFromContract,
        MockSubscription,
        MockAccessFromContract,
        MockAccess,
        MockCustomerInStrategies,
    ):
        MockCustomerFromPartner.return_value.to_dict.return_value = {
            "example_data": 123
        }
        MockCRMAccountHierarchyFromContract.return_value.to_dict.return_value = {
            "example_data": 123
        }
        MockSubscriptionFromContract.return_value.to_dict.return_value = {
            "example_data": 123
        }
        MockAccessFromContract.return_value.to_dict.return_value = {"example_data": 123}
        MockCustomerInStrategies.get.side_effect = PyOpenCellAPIException(
            verb=ANY, url=ANY, status=400, body=ANY
        )

        CRMAccountHierarchyFromContractCreateService(
            self.contract, self.opencell_configuration
        ).run()

        MockCustomerFromPartner.assert_called_with(
            self.contract.partner_id, self.opencell_configuration
        )
        MockCustomer.create.assert_called_with(
            **MockCustomerFromPartner.return_value.to_dict.return_value
        )
        MockCRMAccountHierarchyFromContract.assert_called_with(
            self.contract, str(self.contract.partner_id.id) + "_0"
        )
        MockCRMAccountHierarchy.create.assert_called_with(
            **MockCRMAccountHierarchyFromContract.return_value.to_dict.return_value
        )
        MockSubscriptionFromContract.assert_called_with(
            self.contract, str(self.contract.partner_id.id) + "_0"
        )
        MockSubscription.create.assert_called_with(
            **MockSubscriptionFromContract.return_value.to_dict.return_value
        )
        MockAccessFromContract.assert_called_with(self.contract)
        MockAccess.create.assert_called_with(
            **MockAccessFromContract.return_value.to_dict.return_value
        )

    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_strategies.Customer",  # noqa
        spec=["get"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.Access",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.AccessFromContract",  # noqa
        return_value=Mock(spec=["to_dict"]),
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.Subscription",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.SubscriptionFromContract",  # noqa
        return_value=Mock(spec=["to_dict"]),
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.CRMAccountHierarchy",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.CRMAccountHierarchyFromContract",  # noqa
        return_value=Mock(spec=["to_dict", "code"]),
    )
    def test_create_from_customer_account_to_subscription_hierarchy_in_opencell(
        self,
        MockCRMAccountHierarchyFromContract,
        MockCRMAccountHierarchy,
        MockSubscriptionFromContract,
        MockSubscription,
        MockAccessFromContract,
        MockAccess,
        MockCustomerInStrategies,
    ):
        MockCRMAccountHierarchyFromContract.return_value.to_dict.return_value = {
            "example_data": 123
        }
        MockSubscriptionFromContract.return_value.to_dict.return_value = {
            "example_data": 123
        }
        MockAccessFromContract.return_value.to_dict.return_value = {"example_data": 123}

        customer = OpenCellCustomerResource(
            code="{}_0".format(self.contract.partner_id.id),
            email=self.expected_email,
            iban=self.expected_iban,
        )
        MockCustomerInStrategies.get.return_value.customer = customer

        CRMAccountHierarchyFromContractCreateService(
            self.contract, self.opencell_configuration
        ).run()

        MockCRMAccountHierarchyFromContract.assert_called_with(
            self.contract, str(self.contract.partner_id.id) + "_0_1"
        )
        MockCRMAccountHierarchy.create.assert_called_with(
            **MockCRMAccountHierarchyFromContract.return_value.to_dict.return_value
        )
        MockSubscriptionFromContract.assert_called_with(
            self.contract, str(self.contract.partner_id.id) + "_0_1"
        )
        MockSubscription.create.assert_called_with(
            **MockSubscriptionFromContract.return_value.to_dict.return_value
        )
        MockAccessFromContract.assert_called_with(self.contract)
        MockAccess.create.assert_called_with(
            **MockAccessFromContract.return_value.to_dict.return_value
        )

    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_strategies.Customer",  # noqa
        spec=["get"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.Access",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.AccessFromContract",  # noqa
        return_value=Mock(spec=["to_dict"]),
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.Subscription",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.SubscriptionFromContract",  # noqa
        return_value=Mock(spec=["to_dict"]),
    )
    def test_create_subscription_in_opencell(
        self,
        MockSubscriptionFromContract,
        MockSubscription,
        MockAccessFromContract,
        MockAccess,
        MockCustomerInStrategies,
    ):
        MockSubscriptionFromContract.return_value.to_dict.return_value = {
            "example_data": 123
        }
        MockAccessFromContract.return_value.to_dict.return_value = {"example_data": 123}
        self.contract.mandate_id.partner_bank_id.sanitized_acc_number = (
            self.expected_iban
        )
        expected_customer_code = "{}_0".format(self.contract.partner_id.id)
        customer = OpenCellCustomerResource(
            code=expected_customer_code,
            email=self.expected_email,
            iban=self.expected_iban,
        )
        MockCustomerInStrategies.get.return_value.customer = customer

        CRMAccountHierarchyFromContractCreateService(
            self.contract, self.opencell_configuration
        ).run()

        MockSubscriptionFromContract.assert_called_with(
            self.contract, expected_customer_code
        )
        MockSubscription.create.assert_called_with(
            **MockSubscriptionFromContract.return_value.to_dict.return_value
        )
        MockAccessFromContract.assert_called_with(self.contract)
        MockAccess.create.assert_called_with(
            **MockAccessFromContract.return_value.to_dict.return_value
        )
        MockAccess.create.assert_called_with(
            **MockAccessFromContract.return_value.to_dict.return_value
        )

    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_strategies.Customer",  # noqa
        spec=["get"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.Access",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.AccessFromContract",  # noqa
        return_value=Mock(spec=["to_dict"]),
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.Subscription",  # noqa
        spec=["create"],
    )
    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_service.SubscriptionFromContract",  # noqa
        return_value=Mock(spec=["to_dict"]),
    )
    def test_create_subscription_in_opencell_with_one_shots(
        self,
        MockSubscriptionFromContract,
        MockSubscription,
        MockAccessFromContract,
        MockAccess,
        MockCustomerInStrategies,
    ):
        MockSubscriptionFromContract.return_value.to_dict.return_value = {
            "example_data": 123
        }
        MockAccessFromContract.return_value.to_dict.return_value = {"example_data": 123}

        self.contract.mandate_id.partner_bank_id.sanitized_acc_number = (
            self.expected_iban
        )
        expected_customer_code = "{}_0".format(self.contract.partner_id.id)
        customer = OpenCellCustomerResource(
            code=expected_customer_code,
            email=self.expected_email,
            iban=self.expected_iban,
        )
        MockCustomerInStrategies.get.return_value.customer = customer

        CRMAccountHierarchyFromContractCreateService(
            self.contract, self.opencell_configuration
        ).run()

        MockSubscriptionFromContract.assert_called_with(
            self.contract, expected_customer_code
        )
        MockSubscription.create.assert_called_with(
            **MockSubscriptionFromContract.return_value.to_dict.return_value
        )
        MockAccessFromContract.assert_called_with(self.contract)
        MockAccess.create.assert_called_with(
            **MockAccessFromContract.return_value.to_dict.return_value
        )
        MockAccess.create.assert_called_with(
            **MockAccessFromContract.return_value.to_dict.return_value
        )

    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_strategies.Customer",  # noqa
        spec=["get"],
    )
    def test_create_subscription_fallback(
        self,
        MockCustomerInStrategies,
    ):
        expected_customer_code = "{}_0".format(self.contract.partner_id.id)
        customer = OpenCellCustomerResource(
            code=expected_customer_code, customerAccounts={"customerAccount": None}
        )
        MockCustomerInStrategies.get.return_value.customer = customer
        account_hierarchy_service = CRMAccountHierarchyFromContractCreateService(
            self.contract, self.opencell_configuration
        )
        self.assertRaises(
            PyOpenCellException,
            account_hierarchy_service.run,
        )

    @patch(
        "odoo.addons.opencell_somconnexio.opencell_services.crm_account_hierarchy_create_strategies.Customer",  # noqa
        spec=["get"],
    )
    def test_create_subscription_fallback_OC_creation_blocked(
        self,
        MockCustomerInStrategies,
    ):
        self.contract.partner_id.block_contract_creation_in_OC = True
        customer = OpenCellCustomerResource(
            code="{}_0".format(self.contract.partner_id.id),
            email=self.expected_email,
            iban=self.expected_iban,
        )
        MockCustomerInStrategies.get.return_value.customer = customer
        account_hierarchy_service = CRMAccountHierarchyFromContractCreateService(
            self.contract, self.opencell_configuration
        )
        self.assertRaises(
            PyOpenCellException,
            account_hierarchy_service.run,
        )
