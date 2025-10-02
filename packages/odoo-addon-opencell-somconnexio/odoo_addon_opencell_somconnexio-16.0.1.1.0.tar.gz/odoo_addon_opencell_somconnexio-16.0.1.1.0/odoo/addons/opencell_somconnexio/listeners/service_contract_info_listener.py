from odoo.addons.component.core import Component


class ServiceContractInfo(Component):
    _name = "opencell.service.contract.info.listener"
    _inherit = "base.event.listener"
    _apply_on = [
        "mobile.service.contract.info",
        "vodafone.fiber.service.contract.info",
        "mm.fiber.service.contract.info",
        "orange.fiber.service.contract.info",
    ]

    def on_record_write(self, record, fields=None):
        if "phone_number" in fields:
            self.env["contract.contract"].with_delay().update_phone_number(
                record.contract_ids, record.phone_number
            )
