from odoo import api, models
from odoo.osv import expression


class ProjectProject(models.Model):
    _inherit = "project.project"

    def _hospital_assignee_only(self):
        user = self.env.user
        return user.has_group(
            "hospital_management.group_hospital_project_assignee"
        ) and not user.has_group("project.group_project_manager")

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, **kwargs):
        if self._hospital_assignee_only():
            project_ids = (
                self.env["project.task"]
                .sudo()
                .search([("user_ids", "in", self.env.user.id)])
                .mapped("project_id")
                .ids
            )
            domain = expression.AND([domain, [("id", "in", project_ids)]])
        return super()._search(
            domain, offset=offset, limit=limit, order=order, **kwargs
        )
