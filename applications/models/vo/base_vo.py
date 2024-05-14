class BaseVo:
    def clear_none(self):
        for attr in dir(self):
            if not attr.startswith('_') and getattr(self, attr) is None:
                setattr(self, attr, '')
        return self
