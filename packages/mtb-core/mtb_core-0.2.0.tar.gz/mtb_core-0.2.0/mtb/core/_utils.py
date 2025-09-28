def print_dir(obj, *, use_dict=False):
    """Return the values of the given object's __dict__ attribute."""
    if use_dict:
        for key, value in obj.__dict__.items():
            print(f"{key}: {value}")
    else:
        for key in dir(obj):
            print(f"{key}: {getattr(obj, key)}")
