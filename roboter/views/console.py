import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../package/package_termcolor'))
import termcolor

def get_template(template_file_path, color=None):
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir_path = os.path.join(base_dir, 'templates')

    template = os.path.join(template_dir_path, template_file_path)

    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter="=" * 60, sep=os.linesep)
        contents = termcolor.colored(contents, color)
        return contents

def volumeInfoKeyCheck(data, key):
    if key in data['volumeInfo'].keys():
        return data['volumeInfo'][key]
    else:
        return 'NoneData'

def resultReturn(data):
    data_box = []
    for data in data['items']:
        data_obj = {}
        data_obj['ID'] = data['id']
        data_obj['ETAG'] = data['etag']
        data_obj['SELFLINK'] = data['selfLink']
        data_obj['TITLE'] = volumeInfoKeyCheck(data, 'title')
        data_obj['AUTHORS'] = volumeInfoKeyCheck(data, 'authors')
        data_obj['DESCRIPTION'] = volumeInfoKeyCheck(data, 'description')
        data_obj['PUBLISHDATE'] = volumeInfoKeyCheck(data, 'publishedDate')
        data_box.append(data_obj)
    return data_box