
import numpy as np, collections

@profile
def allocate():
    # 1
    dict_list = [{'x': 1.0 * i, 'y': 2.5 * i} for i in range(100000)]
    
    # 2
    class xy_class(object):
        def __init__(self, x, y):
            self.x, self.y = x, y

    class_list = [xy_class(1.0 * i, 2.5 * i) for i in range(100000)]
    
    # 3
    class xy_slots(object):
        __slots__ = ['x', 'y']

        def __init__(self, x, y):
            self.x, self.y = x, y
        
    slots_list = [xy_slots(1.0 * i, 2.5 * i) for i in range(100000)]
    
    # 4
    xy_namedtuple = collections.namedtuple('xy', ['x', 'y'])
    namedtuple_list = [xy_namedtuple(1.0 * i, 2.5 * i) for i in range(100000)]
    
    # 5
    tuple_list = [(1.0 * i, 2.5 * i) for i in range(100000)]
    
    # 6
    list_list = [[1.0 * i, 2.5 * i] for i in range(100000)]
    
    # 7
    record_np = np.fromiter(((1.0 * i, 2.5 * i) for i in range(100000)),
                       dtype = [('x', 'd'), ('y', 'd')])
    
allocate()
