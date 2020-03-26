import os
import sys
import sass

sys_args = sys.argv[1::]
args = {
    'dir'        : './',
    'ext'        : '.scss',
    'output_dir' : './',
    'output_name': 'main.css',
    'format'     : 'expanded',
}

for item in sys_args:
    item = item.split('=')
    if item[0] in args.keys():
        args[item[0]] = item[1]

file_list = os.listdir(args['dir'])

compiled_sass = ''

for file in file_list:
    if args['ext'] in file:
        file_path = f"./{args['dir']}/{file}"
        with open(file_path, 'r') as sass_file:
            compiled_sass += '\n'
            for line in sass_file.readlines():
                compiled_sass += line

compiled_sass = sass.compile(string=compiled_sass, output_style=f"{args['format']}")

with open(args['output_name'], 'a+') as css_file:
    css_file.truncate(0)
    css_file.write(compiled_sass)

os.rename(f"{args['dir']}{args['output_name']}", f"{args['output_dir']}{args['output_name']}")
