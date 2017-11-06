class dict_observer(dict):
    """
    Send all changes to an observer.
    """

    def __init__(self, value, observer):
        dict.__init__(self, value)
        self.set_observer(observer)

    def set_observer(self, observer):
        """
        All changes  to this dictionary will trigger calls to observer methods
        """
        self.observer = observer

    def __setitem__(self, key, value):
        """
        Intercept the l[key]=value operations.
        Also covers slice assignment.
        """
        try:
            oldvalue = self.__getitem__(key)
        except KeyError:
            dict.__setitem__(self, key, value)
            self.observer.dict_create(self, key)
        else:
            dict.__setitem__(self, key, value)
            self.observer.dict_set(self, key, oldvalue)

    def __delitem__(self, key):
        oldvalue = dict.__getitem__(self, key)
        dict.__delitem__(self, key)
        self.observer.dict_del(self, key, oldvalue)

    def clear(self):
        oldvalue = self.copy()
        dict.clear(self)
        self.observer.dict_clear(self, oldvalue)

    def update(self, update_dict):
        replaced_key_values = []
        new_keys = []
        for key, item in update_dict.items():
            if key in self:
                replaced_key_values.append((key, item))
            else:
                new_keys.append(key)
        dict.update(self, update_dict)
        self.observer.dict_update(self, new_keys, replaced_key_values)

    def setdefault(self, key, value=None):
        if key not in self:
            dict.setdefault(self, key, value)
            self.observer.dict_setdefault(self, key, value)
            return value
        else:
            return self[key]

    def pop(self, k, x=None):
        if k in self:
            value = self[k]
            dict.pop(self, k, x)
            self.observer.dict_pop(self, k, value)
            return value
        else:
            return x

    def popitem(self):
        key, value = dict.popitem(self)
        self.observer.dict_popitem(self, key, value)
        return key, value
