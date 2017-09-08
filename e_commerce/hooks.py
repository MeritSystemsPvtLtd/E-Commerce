# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "e_commerce"
app_title = "E-Commerce"
app_publisher = "Frappé"
app_description = "E-Commerce For Shopping Cart"
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = "mani@meritsystems.com"
app_license = "GNU General Public License"
fixtures = ["Custom Field"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/e_commerce/css/e_commerce.css"
# app_include_js = "/assets/e_commerce/js/e_commerce.js"

# include js, css files in header of web template
# web_include_css = "/assets/e_commerce/css/e_commerce.css"
# web_include_js = "/assets/e_commerce/js/e_commerce.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "e_commerce.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "e_commerce.install.before_install"
# after_install = "e_commerce.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "e_commerce.notifications.get_notification_config"

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
# 		"e_commerce.tasks.all"
# 	],
# 	"daily": [
# 		"e_commerce.tasks.daily"
# 	],
# 	"hourly": [
# 		"e_commerce.tasks.hourly"
# 	],
# 	"weekly": [
# 		"e_commerce.tasks.weekly"
# 	]
# 	"monthly": [
# 		"e_commerce.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "e_commerce.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "e_commerce.event.get_events"
# }

