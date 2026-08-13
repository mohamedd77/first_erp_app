import frappe
from frappe.model.document import Document

class DeliveryFeedback(Document):
	def validate(self):
		if int(self.rating) <= 2 and not self.note:
			frappe.throw("لازم تكتب ملاحظة توضح سبب التقييم المنخفض")