import frappe

def execute():
    frappe.db.sql("""
        UPDATE `tabWorkspace`
        SET is_hidden = 0
        WHERE module = 'Restaurant Expert'
    """)
