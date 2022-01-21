# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
import json

def generate_diff(path_file1, path_file2):
    file1 = json.load(open(path_file1))
    file2 = json.load(open(path_file2))
    keys_union = list(set(file1.keys()) | set(file2.keys()))
    keys_union.sort()
    result = '{\n'
    for i in keys_union:
        if (i in file1) and (i in file2):
            if file1[i] != file2[i]:
                result = result + '  - {0}: {1}\n'.format(i,file1[i])
                result = result + '  + {0}: {1}\n'.format(i,file2[i])
            else:
                result = result + '    {0}: {1}\n'.format(i,file1[i])
        if (i in file1) and (i not in file2):
            result = result + '  - {0}: {1}\n'.format(i,file1[i])
        if (i not in file1) and (i in file2):
            result = result + '  + {0}: {1}\n'.format(i,file2[i])
    result = result + '}'
    result = result.replace('False', 'false')
    result = result.replace('True', 'true')
    return result
