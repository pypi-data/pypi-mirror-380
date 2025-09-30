# Copyright 2023 Camptocamp SA
# @author Simone Orsi <simahawk@gmail.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import logging

from odoo import _, api, exceptions, fields, models

_logger = logging.getLogger(__name__)


class EDIStateConsumerMixin(models.AbstractModel):
    """Provide specific EDI states for related records."""

    _name = "edi.state.consumer.mixin"
    _description = __doc__

    edi_state_id = fields.Many2one(
        string="EDI state",
        comodel_name="edi.state",
        ondelete="restrict",
        copy=False,
    )
    edi_state_workflow_id = fields.Many2one(related="edi_state_id.workflow_id")

    def _edi_set_state(self, state):
        self.sudo().write({"edi_state_id": state.id})

    def edi_find_state(self, code=None, default=False):
        assert code or default
        return self.origin_exchange_type_id.get_state_for_model(
            self._name, code=code, default=default
        )

    def edi_is_valid_state(self, state=None, exc_type=None):
        state = state or self.edi_state_id
        if not state:
            return True
        if exc_type is None and "origin_exchange_type_id" in self._fields:
            exc_type = self.origin_exchange_type_id
        if not exc_type:
            _logger.warning("No exchange type given for %s#%s", self._name, self.id)
            return True
        return (
            state.workflow_id.is_valid_for_model(self._name)
            and state.id in exc_type.state_workflow_ids.state_ids.ids
        )

    @api.constrains("edi_state_id")
    def _check_edi_state_id(self):
        for rec in self:
            if not rec.edi_is_valid_state():
                raise exceptions.UserError(
                    _("State %(name)s [%(code)s] not allowed")
                    % dict(name=rec.edi_state_id.name, code=rec.edi_state_id.code)
                )
