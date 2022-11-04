def log_exception(exception, fn, **kwargs):
    values = ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
    with open("log.txt", "a") as log_file:
        log_file.write(f"Exception: {exception}, Function: {fn}, Values: {values}\n")


def itemgetter(collection, identifier):
    try:
        return collection[identifier]
    except (IndexError, KeyError, TypeError) as ex:
        log_exception(ex, "itemgetter", collection=collection, identifier=identifier)
        raise


a = [1, 2, 4, 5]
itemgetter(a, 9)
