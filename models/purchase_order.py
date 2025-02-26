from odoo import models, fields, api, exceptions


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection(selection_add=[('to_approve', 'Waiting for MD Approval')], tracking=True)
    md_id = fields.Many2one('res.users', string="Approved by MD", tracking=True)

    @api.model
    def create(self, vals):
        """Override create method to notify vendor upon PO creation"""
        order = super(PurchaseOrder, self).create(vals)

        # Ensure the PO has a vendor before sending an email
        if order.partner_id and order.partner_id.email:
            order.send_vendor_email_notification()

        return order

    def send_vendor_email_notification(self):
        """Send an email notification to the vendor when a PO is created"""
        template = self.env.ref('purchase.email_template_edi_purchase', raise_if_not_found=False)
        if template and self.partner_id.email:
            template.send_mail(self.id, force_send=True)

    def button_confirm(self):
        """ Override default confirm method to include COO logic """
        for order in self:
            if not self.env.user.has_group('odoo_it_procurement.group_coo'):
                raise exceptions.UserError("Only the COO can confirm this order.")

            if order.amount_total > 50000:
                # COO confirms, but approval is required from MD
                order.write({'state': 'to_approve'})
            else:
                # COO confirms and approves directly
                super(PurchaseOrder, order).button_confirm()
                order.write({'state': 'purchase'})

    def action_md_approve(self):
        """ MD approves orders above 50,000 """
        for order in self:
            if order.state != 'to_approve':
                raise exceptions.UserError("MD can only approve orders that are pending approval.")
            if not self.env.user.has_group('odoo_it_procurement.group_md'):
                raise exceptions.UserError("Only the MD can approve this order.")

            order.write({
                'state': 'purchase',
                'md_id': self.env.user.id
            })
