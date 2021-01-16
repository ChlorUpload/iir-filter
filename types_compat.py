import sys

if sys.version_info[0] < 3:
    raise Exception
elif sys.version_info[1] <= 8:
    from typing import List, Tuple
else:
    List = list
    Tuple = tuple