def import_string_file(language):
    strings_path = f"lib.strings.strings_{language}"
    return __import__(strings_path, fromlist=[''])


def reload_string_file(context):
    context.strings = import_string_file(context.language)
