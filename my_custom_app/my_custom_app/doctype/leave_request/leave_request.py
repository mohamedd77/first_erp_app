import frappe
from frappe.model.document import Document
from frappe.utils import date_diff, getdate

class LeaveRequest(Document):
	def validate(self):
		self.validate_dates()
		self.calculate_total_days()

	def validate_dates(self):
		if getdate(self.from_date) > getdate(self.to_date):
			frappe.throw("تاريخ البداية لازم يكون قبل تاريخ النهاية")

		if getdate(self.from_date) < getdate(frappe.utils.nowdate()):
			frappe.throw("مينفعش تطلب إجازة في تاريخ فات")

	def calculate_total_days(self):
		self.total_days = date_diff(self.to_date, self.from_date) + 1

	@frappe.whitelist()
	def approve_leave(self):
		self.status = "Approved"
		self.save()
		frappe.msgprint("تمت الموافقة على الإجازة")

	@frappe.whitelist()
	def reject_leave(self):
		self.status = "Rejected"
		self.save()
		frappe.msgprint("تم رفض الإجازة")