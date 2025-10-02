from odoo.addons.component.core import Component
from datetime import datetime

# 5 mins in seconds to delay the jobs
ETA = 300


class ContractLineListener(Component):
    _inherit = "contract.line.listener"

    def on_record_create(self, record, fields=None):
        super().on_record_create(record, fields=fields)

        categ_id = record.product_id.categ_id.id

        if self._is_oneshot_product(categ_id):
            self._schedule_oneshot_addition(record)
        elif self._is_service_product(categ_id):
            self._schedule_service_addition(record)

    def on_record_write(self, record, fields=None):
        super().on_record_write(record, fields=fields)
        if record.date_end:
            eta = 0
            if record.date_end > datetime.today().date():
                end_datetime = datetime.combine(record.date_end, datetime.min.time())
                eta = end_datetime - datetime.today()
            self.env["contract.contract"].with_delay(eta=eta).terminate_service(
                record.contract_id.id, record
            )

    def _is_oneshot_product(self, categ_id):
        """Check if product belongs to one-shot categories"""
        return categ_id in self._get_oneshot_categ_ids()

    def _is_service_product(self, categ_id):
        """Check if product belongs to service categories"""
        service_categs = (
            self._get_service_categ_ids()
            + self._get_additional_service_categ_ids()
            + self._get_multimedia_service_categ_id_list()
            + self._get_sb_additional_service_categ_id_list()
        )
        return categ_id in service_categs

    def _get_oneshot_categ_ids(self):
        """Get IDs for one-shot service categories"""
        return [
            self.env.ref("somconnexio.mobile_oneshot_service").id,
            self.env.ref("somconnexio.broadband_oneshot_service").id,
            self.env.ref("somconnexio.broadband_oneshot_adsl_service").id,
        ]

    def _get_service_categ_ids(self):
        """Get IDs for service technology categories"""
        return (
            self.env["service.technology"]
            .search([])
            .mapped("service_product_category_id")
            .ids
        )

    def _get_additional_service_categ_ids(self):
        """Get IDs for additional service categories"""
        return [
            self.env.ref("somconnexio.broadband_additional_service").id,
            self.env.ref("somconnexio.mobile_additional_service").id,
        ]

    def _get_multimedia_service_categ_id_list(self):
        """Get IDs for multimedia service categories and their children"""
        multimedia_service = self.env.ref("multimedia_somconnexio.multimedia_service")
        multimedia_service_childs = self.env["product.category"].search(
            [("parent_id", "=", multimedia_service.id)]
        )
        return multimedia_service_childs.ids

    def _get_sb_additional_service_categ_id_list(self):
        """Get IDs for switchboard additional service categories and their children"""
        sb_additional_service = self.env.ref(
            "switchboard_somconnexio.switchboard_additional_service"
        )
        sb_additional_service_childs = self.env["product.category"].search(
            [("parent_id", "=", sb_additional_service.id)]
        )
        return sb_additional_service_childs.ids

    def _schedule_oneshot_addition(self, record):
        """Schedule one-shot service addition job"""
        self.env["contract.contract"].with_delay(eta=ETA).add_one_shot(
            record.contract_id.id, record.product_id.default_code
        )

    def _schedule_service_addition(self, record):
        """Schedule service addition job"""
        self.env["contract.contract"].with_delay(eta=ETA).add_service(
            record.contract_id.id, record
        )
