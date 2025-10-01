import logging

from odoo import _
from pyopencell.resources.customer import Customer
from pyopencell.exceptions import PyOpenCellAPIException, PyOpenCellHTTPException

logger = logging.getLogger(__name__)


class CRMAccountHierarchyCreateStrategies:
    def __init__(self, contract, force=False):
        self.contract = contract
        self.force = force
        try:
            self.customer = Customer.get(self.contract.partner_id.ref).customer
        except (PyOpenCellAPIException, PyOpenCellHTTPException):
            self.customer = None

    def strategies(self):
        if not self._customer_exists():
            return "customer_hierarchy", {
                "crm_account_hierarchy_code": self._customer_account_code
            }
        if self._customer_contracts_creation_blocked() and not self.force:
            error_msg = _(
                "Partner with code {} does not allow automatic subscription creation"
            ).format(  # noqa
                self.customer.code
            )
            return "fallback", {"message": error_msg}

        if self._number_customer_accounts() == 0:
            error_msg = _(
                "Customer with code {} found with no customer accounts associated"
            ).format(  # noqa
                self.customer.code
            )
            return "fallback", {"message": error_msg}

        for customer_account in self._customer_accounts:
            if self._same_email(customer_account) and self._same_iban(customer_account):
                return "subscription", {
                    "crm_account_hierarchy_code": customer_account["code"]
                }

        return "customer_account_hierarchy", {
            "crm_account_hierarchy_code": self._customer_account_code
        }

    @property
    def _customer_accounts(self):
        return self.customer.customerAccounts["customerAccount"] or []

    @property
    def _customer_account_code(self):
        if not self.customer:
            return "{}_0".format(self.contract.partner_id.ref)

        customer_accounts_count = len(self.customer.customerAccounts["customerAccount"])
        return "{}_{}".format(self.customer.code, customer_accounts_count)

    def _customer_exists(self):
        return bool(self.customer)

    def _customer_contracts_creation_blocked(self):
        return self.contract.partner_id.block_contract_creation_in_OC

    def _number_customer_accounts(self):
        return len(self._customer_accounts)

    def _same_email(self, customer_account):
        customer_account_email = customer_account["contactInformation"]["email"]
        return customer_account_email == self.contract.email_ids[0].email

    def _same_iban(self, customer_account):
        customer_iban = customer_account["methodOfPayment"][0]["bankCoordinates"][
            "iban"
        ].upper()
        contract_iban = self.contract.mandate_id.partner_bank_id.sanitized_acc_number
        return customer_iban == contract_iban
