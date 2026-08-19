import frappe

@frappe.whitelist()
def get_approved_leaves(employee=None):
	filters = {"status": "Approved"}
	if employee:
		filters["employee"] = employee

	leaves = frappe.get_all(
		"Leave Request",
		filters=filters,
		fields=["name", "employee", "leave_type", "from_date", "to_date", "total_days"]
	)

	return leaves