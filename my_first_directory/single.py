

def gan(my_class):
    results = {}

    def get_results(*args, **kwargs):
        if my_class not in results:
            results[my_class] = my_class(*args, **kwargs)
        return results[my_class]

    return get_results


@gan
class Learned(object):
    y = 10
    pass


x = Learned()
print(x.y)

z = Learned()
print(z.y)
