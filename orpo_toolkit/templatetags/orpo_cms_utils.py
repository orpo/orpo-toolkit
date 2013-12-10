from django import template

register = template.Library()

@register.assignment_tag
def get_top_parent_page(page):
	"""Get the parent page at the top of a hierarchy. For user
	with a Django CMS 'page'"""

	while page.parent is not None:
		page = page.parent

	return page