import frappe


def execute():
	frappe.db.sql("SELECT * FROM `tabDoesNotExist`")
