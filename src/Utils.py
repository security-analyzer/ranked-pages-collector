def save_array_as_file(file_name, array):
    with open(file_name, "w") as txt_file:
        for line in array:
            try:
                if line:
                    txt_file.write(line + "\n")
            except:
                continue