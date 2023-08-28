#!/usr/bin/pythoni3

def safe_print_division(a, b):
    result = None

    try:
        div = a / b
    except Exception:
        pass
    finally:
        if result is None:
            print("{}".format("Inside result: None"))
        else:
            print("{} {:.1f}".format("Inside result:", div))
    return (div)
