from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.assignment_tag
def get_top_parent_page(page):
	"""Get the parent page at the top of a hierarchy. For user
	with a Django CMS 'page'"""

	while page.parent is not None:
		page = page.parent

	return page

@register.filter
def highlight(text, word):
	return mark_safe(text.replace(word, '<span class="highlight">%s</span>' % word))