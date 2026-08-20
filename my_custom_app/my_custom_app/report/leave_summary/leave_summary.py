import frappe

def execute(filters=None):
	columns = [
		{"label": "Employee", "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 200},
		{"label": "Total Approved Days", "fieldname": "total_days", "fieldtype": "Int", "width": 150}
	]

	data = frappe.db.sql("""
		SELECT employee, SUM(total_days) as total_days
		FROM `tabLeave Request`
		WHERE status = 'Approved'
		GROUP BY employee
	""", as_dict=True)

	return columns, data