def scale(name):
    def getter(instance):
        return instance.__dict__[name]

    def setter(instance, value):
        if value < 0:
            raise ValueError('value must be > 0')
        instance.__dict__[name] = value

    return property(getter, setter)

class Size:

    width = scale('width')
    height = scale('height')


s = Size()
s.width = 300
s.height = 400
print(s.width, s.height)