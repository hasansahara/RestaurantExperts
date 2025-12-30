frappe.ready(() => {

    // الحصول على قائمة Help
    const help_menu = frappe.ui.toolbar.get_menu("Help");

    if (!help_menu) return;

    // إضافة فاصل (اختياري)
    frappe.ui.toolbar.add_menu_divider("Help");

    // إضافة عنصر الدعم الفني
    help_menu.push({
        label: __("الدعم الفني"),
        action: () => {
            show_support_dialog();
        }
    });

});

// نافذة الدعم
function show_support_dialog() {
    frappe.msgprint({
        title: __("الدعم الفني"),
        message: `
            <div style="line-height: 2">
                📞 <strong>الهاتف:</strong><br>
                <a href="tel:+966531002543">+966 53 100 2543</a><br><br>

                💬 <strong>واتساب:</strong><br>
                <a href="https://wa.me/966531002543" target="_blank">
                    اضغط للتواصل عبر واتساب
                </a>
            </div>
        `,
        indicator: "green"
    });

