def _restrictive_update(old_dict, new_dict):
    '''Update a dictionary, but throw an error if trying to add new keys'''

    new_keys = set(new_dict) - set(old_dict)
    if new_keys:
        err = 'Got unexpected keyword arguments: {}.'
        raise AttributeError( err.format(list(new_keys)) )
    else:
        old_dict.update(new_dict)

def defaultkwargs(f):
    def wrapper(self, *args, **kwargs):
        new_kwargs = dict(self._defaults)
        _restrictive_update(new_kwargs, kwargs)
        return f(self, *args, **new_kwargs)

    return wrapper
    

class A(object):
    """Example object that gets wrapped"""
    _defaults = {
        'name':'Allan',
        'city':'Berlin',
        'dob':'01/01/01'
        }

    @defaultkwargs
    def __init__(self, *args, **kwargs):
    ''' Since this is wrapped with @defaultkwargs, all keys in _defaults
        will exist in kwargs
    '''
        self.name = kwargs['name']
        self.city = kwargs['city']
        self.dob = kwargs['dob']

if __name__ == '__main__':
    a = A(name='Charles', city='Paris')
    b = A()
    print( '{} - {} - {}'.format(a.name, a.city, a.dob))
    print( '{} - {} - {}'.format(b.name, b.city, b.dob))
