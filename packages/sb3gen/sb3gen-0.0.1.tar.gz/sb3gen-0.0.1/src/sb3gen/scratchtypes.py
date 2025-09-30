from random import randrange

def uid(length: int = 20):
    """
    Generates a UID, see: https://github.com/scratchfoundation/scratch-vm/blob/develop/src/util/uid.js

    Directly translated from the original Javascript code
    """
    SOUP = "!#%()*+,-./:;=?@[]^_`{|}~ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    id = ""
    for i in range(length):
        id += SOUP[randrange(0, len(SOUP))]
    return id

class ScratchValue():
    def __init__(self, value: str | int | bool):
        self.val = value
    def __str__(self) -> str:
        return str(self.val)

# Base class which represents Scratch variables and lists
class _ScratchObject():
    def __init__(self, name: str, value: ScratchValue | list[ScratchValue] = ScratchValue(""), id: str | None = None):
        if id is None:
            self.uid: str = uid()
        else:
            self.uid: str = id
        self.val: ScratchValue | list[ScratchValue] = value
        self.name: str = name
    def __iter__(self):
        yield self.name
        yield self.val
    def target_def_form(self) -> tuple:
        return (self.uid, list(self))

class ScratchVariable(_ScratchObject):
    def __init__(self, name: str, value: ScratchValue = ScratchValue(""), is_cloud: bool = False, uid: str | None = None):
        super().__init__(name, value, uid)
        self.is_cloud: bool = is_cloud
    def __iter__(self):
        yield from super().__iter__()
        if self.is_cloud:
            yield True

class ScratchList(_ScratchObject):
    def __init__(self, name: str, value: list[ScratchValue] = [ScratchValue("")], id: str | None = None):
        super().__init__(name, value, id)
    def __getitem__(self, i: int):
        return self.val[i]

class Broadcast():
    def __init__(self, name: str, id: str | None = None):
        self.name: str = name
        if id is None:
            self.uid = uid()
        else:
            self.uid = id
    def target_def_form(self) -> tuple:
        return (self.uid, self.name)
