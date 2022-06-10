# Под капотом функции copy, deepcopy делают не более, чем вызывают методы __copy__, __deepcopy__.

from collections import UserList
from copy import copy, deepcopy
