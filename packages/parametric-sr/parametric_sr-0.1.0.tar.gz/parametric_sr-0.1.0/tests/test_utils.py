from psr import get_operations, get_variables, get_delayed_constants, get_constants

# create functions units for use
Add, Sub = get_operations(names=["add", "sub"])
Mul = get_operations(names="mul")
X1, X2 = get_variables(indices=2)
C1 = get_delayed_constants(prefixes="C")
One = get_constants(values=1)
