a  = dict()


a.__getattribute__ = lambda self, name: self[name]


a['a'] = 111








