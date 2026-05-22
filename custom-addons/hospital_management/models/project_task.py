from odoo import api, models
from odoo.osv import expression


class ProjectTask(models.Model):
    _inherit = "project.task"

    def _hospital_assignee_only(self):
        user = self.env.user
        return user.has_group(
            "hospital_management.group_hospital_project_assignee"
        ) and not user.has_group("project.group_project_manager")

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, **kwargs):
        if self._hospital_assignee_only():
            domain = expression.AND(
                [domain, [("user_ids", "in", self.env.user.id)]]
            )
        return super()._search(
            domain, offset=offset, limit=limit, order=order, **kwargs
        )
