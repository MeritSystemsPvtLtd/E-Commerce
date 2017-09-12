# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, _
import frappe.defaults
from frappe.utils import cint, flt, get_fullname, cstr
from frappe.contacts.doctype.address.address import get_address_display
from erpnext.shopping_cart.doctype.shopping_cart_settings.shopping_cart_settings import get_shopping_cart_settings
from frappe.utils.nestedset import get_root_of
from erpnext.accounts.utils import get_account_name
from erpnext.shopping_cart.cart import _get_cart_quotation, apply_cart_settings, set_cart_count, get_cart_quotation, get_shopping_cart_menu

class WebsitePriceListMissingError(frappe.ValidationError): pass

@frappe.whitelist()
def change_in_shipping(shipp):
	with_items=True
	quotation = _get_cart_quotation()
	if shipp == '0':
		quotation.shipping_rule = None
	else:
		quotation.shipping_rule = shipp
	empty_card = False
	"""qty = flt(qty)
	if qty == 0:
		quotation_items = quotation.get("items", {"item_code": ["!=", item_code]})
		if quotation_items:
			quotation.set("items", quotation_items)
		else:
			empty_card = True

	else:
		quotation_items = quotation.get("items", {"item_code": item_code})
		if not quotation_items:
			quotation.append("items", {
				"doctype": "Quotation Item",
				"item_code": item_code,
				"qty": qty
			})
		else:
			quotation_items[0].qty = qty"""

	apply_cart_settings(quotation=quotation)

	quotation.flags.ignore_permissions = True
	if not empty_card:
		quotation.save()
	else:
		quotation.delete()
		quotation = None

	set_cart_count(quotation)

	context = get_cart_quotation(quotation)

	if cint(with_items):
		return {
			"items": frappe.render_template("templates/includes/cart/cart_items.html",
				context),
			"taxes": frappe.render_template("templates/includes/order/order_taxes.html",
				context),
		}
	else:
		return {
			'name': quotation.name,
			'shopping_cart_menu': get_shopping_cart_menu(context)
		}


@frappe.whitelist()
def get_payment_mode(context=None):
	print "In get_payment_mode"
	doc = frappe.get_all("Mode of Payment", fields=["mode_of_payment"], filters=
		{"enable_for_cart_page": 1})
	contextMOP = {"mop":doc}
	return {
		"payment_mode": frappe.render_template("templates/includes/cart/cart_payment_modes.html",
			contextMOP)
		}

@frappe.whitelist()
def cart_shipping_rule(context=None):
	doc = frappe.get_all("Shipping Rule", fields=["label"], filters=
		{"enable_for_cart_page": 1})
	contextSOP = {"sop":doc}
	return {
		"cart_shipping_rule": frappe.render_template("templates/includes/cart/cart_shipping_rule.html",
			contextSOP)
		}

