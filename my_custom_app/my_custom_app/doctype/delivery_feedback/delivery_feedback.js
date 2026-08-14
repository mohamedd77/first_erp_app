frappe.ui.form.on("Delivery Feedback", {
	rating: function(frm) {
		if (frm.doc.rating == "1" || frm.doc.rating == "2") {
			frm.set_df_property("note", "reqd", 1);
		} else {
			frm.set_df_property("note", "reqd", 0);
		}
		frm.refresh_field("note");
	},

	refresh: function(frm) {
		if (!frm.doc.reviewed && !frm.is_new()) {
			frm.add_custom_button("Mark as Reviewed", function() {
				frm.call("mark_as_reviewed").then(() => {
					frm.reload_doc();
				});
			});
		}
	}
});