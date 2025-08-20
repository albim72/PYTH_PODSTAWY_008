import builtins
import types
orig_build_class = builtins.__build_class__

def boom_build_class(func, name, *args, **kwargs):
    cls = orig_build_class(func, name, *args, **kwargs)
    for attr, val in list(vars(cls).items()):
        if isinstance(val, (types.FunctionType, classmethod, staticmethod)):
            # Wyciągnij funkcję niezależnie od dekoratora
            f = val if isinstance(val, types.FunctionType) else val.__func__
            def make_boom(f):
                def wrapper(self, *a, **k):
                    # ZA PIERWSZYM RAZEM: wyczyść obiekt, by reszta programu wybuchła
                    if hasattr(self, "__dict__"):
                        self.__dict__.clear()
                    return f(self, *a, **k)
                return wrapper
            wrapped = make_boom(f)
            if isinstance(val, classmethod):
                wrapped = classmethod(wrapped)
            elif isinstance(val, staticmethod):
                wrapped = staticmethod(f)  # statycznych nie owijamy „self-destrukcją”
            setattr(cls, attr, wrapped)
    return cls

builtins.__build_class__ = boom_build_class  # <<— globalny hak

# Od tego miejsca każda nowa klasa jest „skażona”:
class Konto:
    def __init__(self):
        self.saldo = 100
    def przelew(self, kwota):
        self.saldo -= kwota

k = Konto()
k.przelew(10)     # po tym wywołaniu __dict__ znika
print(k.saldo)    # -> AttributeError: 'Konto' object has no attribute 'saldo'
