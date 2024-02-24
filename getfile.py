def get_files(full_path='', list_top_dir=False, list_all_files=False):
    index_f=[]

    for root, directories, files in os.walk(full_path, topdown=False):
        if list_top_dir:
            if ce_path(root) == ce_path(full_path):
                index_f = directories
        # print('A', root)
        # print('B', directories)
        # print('C', files)
        else:
            if list_all_files:
                for f in files:
                    if os.path.isfile(ce_path(root) + f):
                        index_f.append(ce_path(root) + f)
            else:
                index_f = files
    return index_f
