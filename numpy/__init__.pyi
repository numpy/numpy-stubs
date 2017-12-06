# very simple, just enough to start running tests

class ndarray: pass

class dtype: pass

def array(
    object: object,
    dtype: dtype = ...,
    copy: bool = ...,
    subok: bool = ...,
    ndmin: int = ...) -> ndarray: ...
