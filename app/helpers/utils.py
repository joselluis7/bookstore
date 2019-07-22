#-*-encoding:utf-8-*-
import locale

def list_string(l):
	s = ""
	item = 0
	if len(l) > 1:

		for item in range(len(l) - 1):
			s = s + l[item] + ", "
		s = s + l[item + 1]
	else:
		s = l.pop()
	return s

def currency_format(value):
	locale.setlocale(locale.LC_ALL,'')
	return locale.currency(value, grouping=True, symbol=None)

def output_format(price,class_type,isbn,title,authors):
		price = currency_format(price)
		authors = list_string(authors)
		return "€ {0} [{1}] {2}: {3} - {4} ".format(price,class_type,isbn,title,authors)

