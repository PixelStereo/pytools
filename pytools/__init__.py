try:
    basestring  # attempt to evaluate basestring
    def is_string(test):
    	print('python 2')
    	return isinstance(test, basestring)
except NameError:
    def is_string(test):
    	print('python 3')
    	return isinstance(test, str)
