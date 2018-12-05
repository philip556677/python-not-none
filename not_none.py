def not_none(nullable_parameters=None):

    def the_actual_test(f, args, filter_array):
        has_none = False
        bad_parameters = []

        if type(filter_array) is str:

            filter_array = [filter_array]

        if not filter_array:

            if any(arg[1] is None for arg in args):
                raise ValueError('function {}: Parameters cannot be None. '.format(f.__name__))

        elif type(filter_array) is list:
            for a in args:
                for ff in filter_array:
                    if a[0] != ff:
                        if a[1] is None:
                            has_none = True
                            bad_parameters.append(a[0])
                            break

        if has_none:
            raise ValueError('function {}: Parameters {} cannot be None. '.format(f.__name__, bad_parameters))

    def real_decorator(f):


        v_names = f.__code__.co_varnames

        def wrapper(*args, **kwargs):
            n_args = []

            for a in range(0, len(args)):
                n_args.append((v_names[a], args[a]))

            the_actual_test(f, n_args, nullable_parameters)
            result = f(*args, **kwargs)

            return result
        return wrapper

    return real_decorator


# tests
@not_none()
def _test_no_filter(a, b):
    pass


@not_none(nullable_parameters=["a"])
def _test_yes_filter(a, b):
    pass


@not_none(nullable_parameters="a")
def _test_string_filter(a,b):
    pass


@not_none(nullable_parameters="a")
def _test_default_filter(a,b=1):
    pass


try:

    _test_no_filter(None,None)

except Exception as e:

    print(e)


try:

    _test_no_filter(None, 1)

except Exception as e:

    print(e)


try:

    _test_yes_filter(None, None)

except Exception as e:

    print(e)


try:

    _test_yes_filter(None, 2)
    print("Function Success")

except Exception as e:

    print(e)

try:

    _test_string_filter(None, 2)
    print("Function Success")

except Exception as e:

    print(e)

try:

    _test_string_filter(None, None)


except Exception as e:

    print(e)


try:

    _test_default_filter(None)


except Exception as e:

    print(e)

try:

    _test_default_filter(None,None)


except Exception as e:

    print(e)