import frappe

def create_naming_rules():
    # في v15 الاسم الصحيح للـ Doctype هو "Document Naming Rule"
    doctype_name = "Document Naming Rule"
    
    # التأكد أولاً من وجود الـ Doctype في النظام
    if not frappe.db.exists("DocType", doctype_name):
        print(f"⚠️ {doctype_name} is not installed on this site.")
        return

    rules = [
        {
            "label": "WIP Items Rule",
            "prefix": "WIP-",
            "conditions": [
                {"field": "is_stock_item", "condition": "=", "value": "1"},
                {"field": "is_purchase_item", "condition": "=", "value": "0"},
                {"field": "is_fixed_asset", "condition": "=", "value": "0"}
            ]
        },
        {
            "label": "Final Products Rule",
            "prefix": "FINAL-",
            "conditions": [
                {"field": "is_stock_item", "condition": "=", "value": "0"},
                {"field": "is_sales_item", "condition": "=", "value": "1"},
                {"field": "is_fixed_asset", "condition": "=", "value": "0"}
            ]
        },
        {
            "label": "Fixed Assets Rule",
            "prefix": "AST-",
            "conditions": [
                {"field": "is_fixed_asset", "condition": "=", "value": "1"}
            ]
        },
        {
            "label": "SKU Items Rule",
            "prefix": "SKU-",
            "conditions": [
                {"field": "is_stock_item", "condition": "=", "value": "1"},
                {"field": "is_purchase_item", "condition": "=", "value": "1"},
                {"field": "is_fixed_asset", "condition": "=", "value": "0"}
            ]
        }
    ]

    for r in rules:
        if not frappe.db.exists(doctype_name, r["label"]):
            doc = frappe.get_doc({
                "doctype": doctype_name,
                "document_type": "Item",
                "name": r["label"],
                "prefix": r["prefix"],
                "length": 4,
                "priority": 1
            })
            
            for c in r["conditions"]:
                doc.append("conditions", c)
            
            doc.insert(ignore_permissions=True)
            print(f"✅ Created: {r['label']}")

    frappe.db.commit()