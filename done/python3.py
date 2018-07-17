def just_print(n):
	print(n)

foo_code = foo.__code__
code = type(foo_code)
function = type(foo)

res = []
for thing in foo_code.co_consts:
	if type(thing) is code and thing.co_name == "magic":
		res.append(just_print.__code__)
	else:
		res.append(thing)

new_consts = tuple(res)

new_foo = function(
		code(foo_code.co_argcount, foo_code.co_nlocals, foo_code.co_stacksize, foo_code.co_flags, foo_code.co_code, 
			new_consts, foo_code.co_names, foo_code.co_varnames, foo_code.co_filename, "foo", foo_code.co_firstlineno, foo_code.co_lnotab,
			foo_code.co_freevars, foo_code.co_cellvars),
		foo.__globals__, "foo", foo.__defaults__, foo.__closure__)
new_foo()