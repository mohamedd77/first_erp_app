import frappe
from frappe.model.document import Document

class DeliveryFeedback(Document):
	def validate(self):
		if int(self.rating) <= 2 and not self.note:
			frappe.throw("لازم تكتب ملاحظة توضح سبب التقييم المنخفض")



	@frappe.whitelist()
	def mark_as_reviewed(self):
		self.reviewed = 1
		self.save()
		frappe.msgprint("تم تسجيل المراجعة بنجاح")