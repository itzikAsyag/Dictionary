import ClientClass
_RaiseKeyError = object() # singleton for no-default behavior
_AddOp =  "add"
_DelOp = "del"

class LowerDict(dict):  # dicts take a mapping or iterable as their optional first argument
    def __init__(self, client):
        if isinstance(client , ClientClass.Client_Class):
            self._client = client
            super(LowerDict, self).__init__(self)
        else:
            print("Error , Dictionary init dosent got ClientClass variable")
            return None
    def __getitem__(self, k):
        return super(LowerDict, self).__getitem__(k)
    def __setitem__(self, k, v):
        self._client.SendUpdate(_AddOp, k, v)
        return super(LowerDict, self).__setitem__(k, v)
    def __delitem__(self, k):
        self._client.SendUpdate( _DelOp, k)
        return super(LowerDict, self).__delitem__(k)
    def get(self, k, default=None):
        return super(LowerDict, self).get(k, default)
    def setdefault(self, k, default=None):
        return super(LowerDict, self).setdefault(k, default)
    def pop(self, k, v=_RaiseKeyError):
        if v is _RaiseKeyError:
            return super(LowerDict, self).pop(k)
        return super(LowerDict, self).pop(k, v)
    def update(self, mapping=(), **kwargs):
        super(LowerDict, self).update(self)
    def __contains__(self, k):
        return super(LowerDict, self).__contains__(k)
# lol