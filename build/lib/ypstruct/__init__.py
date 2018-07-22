class structure (dict):

    def __repr__(self):
        return 'structure({})'.format(super().__repr__())

    def __getattr__(self, field):
        if field not in dir(self):
            if field in self.keys():
                return self[field]
            else:
                return None
        else:
            return None

    def __setattr__(self, field, value):
        if field not in dir(self):
            self[field] = value
        else:
            return super().__setattr__(field, value)
    
    def fields(self):
        return list(self.keys())

    def remove_field(self, field):
        if field in self.keys():
            del self[field]
    
    def add_field(self, field, value = None):
        if field not in self.keys():
            self[field] = value

    def copy(self):
        import copy as cp
        self_copy = structure()
        for field in self.keys():
            if isinstance(self[field], structure):
                self_copy[field] = self[field].copy()
            else:
                self_copy[field] = cp.copy(self[field])
        
        return self_copy

    def deepcopy(self):
        import copy as cp
        self_copy = structure()
        for field in self.keys():
            if isinstance(self[field], structure):
                self_copy[field] = self[field].deepcopy()
            else:
                self_copy[field] = cp.deepcopy(self[field])
        
        return self_copy

    def repeat(self, n):
        return [self.deepcopy() for i in range(n)]
