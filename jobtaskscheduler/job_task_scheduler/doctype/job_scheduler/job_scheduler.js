// Copyright (c) 2016, Codrotech Inc. and contributors
// For license information, please see license.txt
frappe.ui.form.on('Job Scheduler', {
	run: function (frm) {
		switch (frm.doc.run) {
			case "Hourly":
				frm.doc.hour = null;
				frm.doc.day_of_month = null;
				frm.doc.month = null;
				frm.doc.day_of_week = null;
				frm.doc.cron_style = null;
				break;

			case "Daily":
				frm.doc.day_of_month = null;
				frm.doc.month = null;
				frm.doc.day_of_week = null;
				frm.doc.cron_style = null;
				break;

			case "Weekly":
				frm.doc.day_of_month = null;
				frm.doc.month = null;
				frm.doc.cron_style = null;
				break;

			case "Monthly":
				frm.doc.month = null;
				frm.doc.day_of_week = null;
				frm.doc.cron_style = null;
				break;

			case "Yearly":
				frm.doc.day_of_week = null;
				frm.doc.cron_style = null;
				break;

			case "Cron Style":
				frm.doc.minute = null;
				frm.doc.hour = null;
				frm.doc.day_of_month = null;
				frm.doc.month = null;
				frm.doc.day_of_week = null;
				break;
		}
	},
});
