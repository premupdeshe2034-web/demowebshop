import configparser

import os


def get_demo_webshop(group, keys):
    config = configparser.ConfigParser()

    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "demo_configuration", "config.ini")

    print("CONFIG PATH:", file_path)

    read_files = config.read(file_path)
    print("READ FILE RESULT:", read_files)
    print("FILE EXISTS:", os.path.exists(file_path))
    print("SECTIONS:", config.sections())

    if group not in config:
        raise Exception(f"Section '{group}' not found in config file")

    return config.get(group, keys)


# test call (OUTSIDE function)
print(get_demo_webshop("demo_webshop", "url"))