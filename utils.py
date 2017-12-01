def import_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip()
