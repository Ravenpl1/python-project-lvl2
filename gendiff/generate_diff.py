# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
import json


def generate_diff(path_file1, path_file2):
    file1 = json.load(open(path_file1))
    file2 = json.load(open(path_file2))
    keys_union = list(set(file1.keys()) | set(file2.keys()))
    keys_union.sort()
    result = '{\n'
    for key in keys_union:
        if (key in file1) and (key in file2):
            if file1[key] != file2[key]:
                result = result + '  - {0}: {1}\n'.format(key, file1[key])
                result = result + '  + {0}: {1}\n'.format(key, file2[key])
            else:
                result = result + '    {0}: {1}\n'.format(key, file1[key])
        if (key in file1) and (key not in file2):
            result = result + '  - {0}: {1}\n'.format(key, file1[key])
        if (key not in file1) and (key in file2):
            result = result + '  + {0}: {1}\n'.format(key, file2[key])
    result = result + '}'
    result = result.replace('False', 'false')
    result = result.replace('True', 'true')
    return result
