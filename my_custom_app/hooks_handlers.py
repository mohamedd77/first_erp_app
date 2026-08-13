import frappe

def on_sales_invoice_save(doc, method):
	frappe.msgprint(f"مرحباً! الفاتورة دي للعميل: {doc.customer}")