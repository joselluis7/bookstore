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