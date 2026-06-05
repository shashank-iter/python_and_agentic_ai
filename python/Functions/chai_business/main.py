# import recipies.flavor

# print(recipies.flavor.ginger_chai())
from recipies.flavor import elaichi_chai, ginger_chai

print(ginger_chai(), elaichi_chai())

# relative imports
# from .recipies.flavor import elaichi_chai
#
# avoid  from masala_chai import *
# __init__.py turns folder into python package
# after python 3.3 doesn't needed.
