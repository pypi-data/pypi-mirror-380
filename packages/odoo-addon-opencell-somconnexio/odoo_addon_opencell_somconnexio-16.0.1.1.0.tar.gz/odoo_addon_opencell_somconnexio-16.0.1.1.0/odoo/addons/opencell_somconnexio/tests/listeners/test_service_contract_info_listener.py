from odoo.addons.component.tests.common import ComponentMixin
from odoo.tests.common import TransactionCase

from odoo.addons.somconnexio.tests.helper_service import (
    contract_mobile_create_data,
    contract_fiber_create_data,
)


class TestServiceContractInfoListener(TransactionCase, ComponentMixin):
    @classmethod
    def setUpClass(cls):
        super(TestServiceContractInfoListener, cls).setUpClass()
        cls.setUpComponent()

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        ComponentMixin.setUp(self)

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        ComponentMixin.setUp(self)

        self.partner = self.env.ref("somconnexio.res_partner_2_demo")
        self.contract_mobile_data = contract_mobile_create_data(self.env, self.partner)
        self.contract_vodafone_fiber_data = contract_fiber_create_data(
            self.env, self.partner
        )
        self.contract_masmovil_fiber_data = contract_fiber_create_data(
            self.env, self.partner, "masmovil"
        )
        self.contract_orange_fiber_data = contract_fiber_create_data(
            self.env, self.partner, "orange"
        )
        self.new_phone_number = "600111222"

    def test_update_phone_number_mobile(self):
        self._execute_and_assert(
            self.contract_mobile_data,
            "mobile.service.contract.info",
            "mobile_contract_service_info_id",
        )

    def test_update_phone_number_vodafone_fiber(self):
        self._execute_and_assert(
            self.contract_vodafone_fiber_data,
            "vodafone.fiber.service.contract.info",
            "vodafone_fiber_service_contract_info_id",
        )

    def test_update_phone_number_masmovil_fiber(self):
        self._execute_and_assert(
            self.contract_masmovil_fiber_data,
            "mm.fiber.service.contract.info",
            "mm_fiber_service_contract_info_id",
        )

    def test_update_phone_number_orange_fiber(self):
        self._execute_and_assert(
            self.contract_orange_fiber_data,
            "orange.fiber.service.contract.info",
            "orange_fiber_service_contract_info_id",
        )

    def _execute_and_assert(self, data, contract_info_ref, contract_info_id):
        contract = self.env["contract.contract"].create(data)
        service_contract_info = self.env[contract_info_ref].browse(
            data[contract_info_id]
        )
        service_contract_info.write({"phone_number": self.new_phone_number})
        jobs_domain = [
            ("method_name", "=", "update_phone_number"),
            ("model_name", "=", "contract.contract"),
        ]
        queued_jobs = self.env["queue.job"].search(jobs_domain)
        self.assertEqual(queued_jobs.args, [contract, self.new_phone_number])
