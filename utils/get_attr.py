import inspect

def get_init_attributes(cls):
    init_method = cls.__init__
    source = inspect.getsource(init_method)
    attributes = set()
    for line in source.split('\n'):
        if line.strip().startswith('self.'):
            parts = line.split('=')
            if len(parts) > 1:
                attribute = parts[0].strip().replace('self.', '')
                attributes.add(attribute)
    
    return attributes


# attributes = get_init_attributes(model)
# print(attributes)