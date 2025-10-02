import logging
from odoo import _

from pyopencell.resources.customer import Customer
from pyopencell.resources.subscription_list import SubscriptionList
from pyopencell.exceptions import PyOpenCellAPIException, PyOpenCellHTTPException
from .subscription_service import SubscriptionService

logger = logging.getLogger(__name__)


class CRMAccountHierarchyUpdateStrategies:
    def __init__(
        self,
        contracts,
        updated_field,
        partner=None,
        customer_account_code=None,
        force=False,
    ):
        self.contracts = contracts
        self.updated_field = updated_field
        self.force_contract = force
        if partner:
            self.customer_code = partner.ref
        else:
            self.customer_code = self.contracts[0].partner_id.ref
        if customer_account_code:
            self.customer_account_code = customer_account_code
        else:
            self.customer_account_code = None
        try:
            self.customer = Customer.get(self.customer_code).customer
        except (PyOpenCellAPIException, PyOpenCellHTTPException):
            self.customer = None

    def strategies(self):
        if not self._customer_exists():
            strategy, kwargs = self._fallback_not_found()

        elif len(self._customer_accounts) == 0:
            strategy, kwargs = self._fallback_customer_without_accounts()

        elif self.updated_field == "address":
            strategy, kwargs = self._change_address()

        elif self.updated_field == "iban" and self.force_contract:
            if len(self.contracts) == 1:
                strategy, kwargs = self._change_iban_force()
            else:
                strategy, kwargs = self._fallback_many_contracts_force()

        elif len(self._customer_accounts) > 1:
            strategy, kwargs = self._fallback_customer_different_accounts()

        elif not self._all_contracts_to_change_in_customer_subscription_list():
            strategy, kwargs = self._fallback_customer_not_whole_account_hierarchy()

        elif self.updated_field == "email":
            strategy, kwargs = self._change_email()

        elif self.updated_field == "iban":
            strategy, kwargs = self._change_iban()

        else:
            strategy, kwargs = self._fallback_unknown()

        return strategy, kwargs

    @property
    def _customer_account_code(self):
        if self.customer_account_code:
            return self.customer_account_code
        return "{}_0".format(self.customer_code)

    @property
    def _customer_account_code_force(self):
        return SubscriptionService(self.contracts[0]).subscription.userAccount

    @property
    def _customer_accounts(self):
        customer_accounts = self.customer.customerAccounts["customerAccount"]
        return [ca.get("code") for ca in customer_accounts]

    def _customer_exists(self):
        return bool(self.customer)

    def _fallback_unknown(self):
        msg = _("Something went wrong, unable to choose a strategy").format(
            self.customer_code
        )
        return "fallback", {"fallback_message": msg}

    def _fallback_not_found(self):
        msg = _("Customer with code {} not found in OC").format(self.customer_code)
        return "fallback", {"fallback_message": msg}

    def _fallback_customer_without_accounts(self):
        msg = _(
            "Customer with code {} does not have any customer account hierachy."
        ).format(self.customer_code)
        return "fallback", {"fallback_message": msg}

    def _fallback_customer_different_accounts(self):
        msg = _(
            "Customer with code {} has more than one customer account hierachy. "
        ).format(self.customer_code) + _("Please update OC manually.")
        return "fallback", {"fallback_message": msg}

    def _fallback_customer_not_whole_account_hierarchy(self):
        msg = _(
            "Trying to add changes that would need to divide the customer account hierarchy from customer with code {} . "  # noqa
        ).format(self.customer_code) + _("Please update OC manually.")
        return "fallback", {"fallback_message": msg}

    def _fallback_many_contracts_force(self):
        msg = _("Many contracts used with Force Contract IBAN Strategy")
        return "fallback", {"fallback_message": msg}

    def _change_email(self):
        return "email", {"customer_account_code": self._customer_account_code}

    def _change_iban(self):
        return "iban", {"customer_account_code": self._customer_account_code}

    def _change_iban_force(self):
        return "iban", {"customer_account_code": self._customer_account_code_force}

    def _change_address(self):
        return "address", {"customer_account_code": self._customer_account_code}

    def _get_customer_subscription_list(self):
        user_account = SubscriptionService(self.contracts[0]).subscription.userAccount

        return SubscriptionList.get(
            query="userAccount.code:{}|status:ACTIVE".format(user_account)
        ).subscriptions

    def _all_contracts_to_change_in_customer_subscription_list(self):
        contract_codes = sorted([c.code for c in self.contracts])
        sub_codes = sorted([s.code for s in self._get_customer_subscription_list()])
        return sub_codes == contract_codes
