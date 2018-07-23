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
    
    # Get the list of structure fields
    def fields(self):
        return list(self.keys())

    # Deletes a field from structure
    def remove_field(self, field):
        if field in self.keys():
            del self[field]
    
    # Adds a new field to the structure
    def add_field(self, field, value = None):
        if field not in self.keys():
            self[field] = value

    # Creates a shallow copy of the structure
    def copy(self):
        import copy as cp
        self_copy = structure()
        for field in self.keys():
            if isinstance(self[field], structure):
                self_copy[field] = self[field].copy()
            else:
                self_copy[field] = cp.copy(self[field])
        
        return self_copy

    # Creates a deep copy of the strucre
    def deepcopy(self):
        import copy as cp
        self_copy = structure()
        for field in self.keys():
            if isinstance(self[field], structure):
                self_copy[field] = self[field].deepcopy()
            else:
                self_copy[field] = cp.deepcopy(self[field])
        
        return self_copy

    # Repeats (replicates) the structure to create an stratucre array (eg. for initialization)
    def repeat(self, n):
        return [self.deepcopy() for i in range(n)]
