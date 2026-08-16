frappe.ui.form.on("Leave Request", {
	from_date: function(frm) {
		calculate_days(frm);
	},
	to_date: function(frm) {
		calculate_days(frm);
	},
	refresh: function(frm) {
		if (frm.doc.status === "Draft") {
			frm.add_custom_button("Submit for Approval", function() {
				frm.set_value("status", "Pending Approval");
				frm.save();
			});
		}

		if (frm.doc.status === "Pending Approval") {
			frm.add_custom_button("Approve", function() {
				frm.call("approve_leave").then(() => {
					frm.reload_doc();
				});
			});

			frm.add_custom_button("Reject", function() {
				frm.call("reject_leave").then(() => {
					frm.reload_doc();
				});
			});
		}
	}
});

function calculate_days(frm) {
	if (frm.doc.from_date && frm.doc.to_date) {
		let diff = frappe.datetime.get_day_diff(frm.doc.to_date, frm.doc.from_date);
		if (diff >= 0) {
			frm.set_value("total_days", diff + 1);
		}
	}
}