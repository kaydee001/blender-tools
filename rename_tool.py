def add_prefix(objects, prefix):
    renamed_objects = []
    for obj in objects:
        new_name = prefix + obj.name
        obj.name = new_name

        renamed_objects.append(obj)


def add_suffix(objects, suffix):
    renamed_objects = []
    for obj in objects:
        new_name = obj.name + suffix
        obj.name = new_name

        renamed_objects.append(obj)

    return renamed_objects


def rename_obj(objects, prefix="", suffix=""):
    # if obj.name.startswith(prefix):
    #     pass
    # if obj.name.endswith(suffix):
    #     pass
    for obj in objects:
        new_prefix = "" if obj.name.startswith(prefix) else prefix
        new_suffix = "" if obj.name.endswith(suffix) else suffix

        new_name = new_prefix + obj.name + new_suffix
        obj.name = new_name
