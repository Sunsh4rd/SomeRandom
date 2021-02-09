alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,!?:;()'

def unique_sym_count(string):
	return len(set(string.lower()))

def gen_matrix(key):
	n = unique_sym_count(key)
	return [[0]] * n