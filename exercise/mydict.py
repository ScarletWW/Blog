class Dict(dict):

    """
    需要进行单元测试的模块

    """
    def __init__(self, **kw):
        super().__init__(**kw) # 注意super是

    def __getattr__(self, key):
        try:
            return self[key]
        except:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
            