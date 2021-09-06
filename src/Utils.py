import yaml

def save_array_as_file(file_name, array):
    with open(file_name, "w") as txt_file:
        for line in array:
            try:
                if line:
                    txt_file.write(line + "\n")
            except:
                continue

def config(key):
    try:
        with open("config.yaml", "r") as config_file:
            config = yaml.safe_load(config_file)
            return config[key]
    except:
        return ''