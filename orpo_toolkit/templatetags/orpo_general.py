from django import template

register = template.Library()

@register.filter
def getrange(start, end):
	try:
		start = int(start)
		end = start + int(end) + 1
	except ValueError:
		return range(0, 4)

	return range(start, end)

@register.filter
def subtract(value, arg):
    return value - arg