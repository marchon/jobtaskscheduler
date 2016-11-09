# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from . import __version__ as app_version

app_name = "jobtaskscheduler"
app_title = "Job Task Scheduler"
app_publisher = "Codrotech Inc."
app_description = "A scheduler for job tasks"
app_icon = "octicon octicon-checklist"
app_color = "orange"
app_email = "billing@codrotech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jobtaskscheduler/css/jobtaskscheduler.css"
# app_include_js = "/assets/jobtaskscheduler/js/jobtaskscheduler.js"

# include js, css files in header of web template
# web_include_css = "/assets/jobtaskscheduler/css/jobtaskscheduler.css"
# web_include_js = "/assets/jobtaskscheduler/js/jobtaskscheduler.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "jobtaskscheduler.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "jobtaskscheduler.install.before_install"
# after_install = "jobtaskscheduler.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jobtaskscheduler.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"jobtaskscheduler.tasks.all"
# 	],
# 	"daily": [
# 		"jobtaskscheduler.tasks.daily"
# 	],
# 	"hourly": [
# 		"jobtaskscheduler.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jobtaskscheduler.tasks.weekly"
# 	]
# 	"monthly": [
# 		"jobtaskscheduler.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "jobtaskscheduler.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "jobtaskscheduler.event.get_events"
# }
