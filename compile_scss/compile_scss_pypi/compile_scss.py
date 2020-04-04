import sass
import click
import json
from os import path, listdir, remove, walk, getcwd
from shutil import copyfile

def format_directory_name(directory):
    '''
    This just adds a forward slash '/' to the end of a 
        directory if it isn't included by the user to
        prevent file opening/creation errors.
    '''

    if directory[-1] != '/':
            directory += '/'

    return directory

def valid_path(file_path):
    '''
    If given file path exists, return True, 
        otherwise return False
    '''
    if(path.exists(file_path)):
        return file_path
    else:
        return False
        # raise click.BadParameter(f"The directory {file_path} does not exist.")

def dir_contains_extension(directory, extension):
    '''
    Searches specified directory for a particular file extension
    If at least one file in the directory contains the given extension, return True,
        otherwise, return False
    '''
    if valid_path(directory):
        file_list = listdir(directory)

    if [True for file_name in file_list if '.scss' in file_name] != []:
        return True
    else:
        return False
        # raise click.BadParameter(f"The path: '{directory}' does not contain any files with the {extension} extension.")

def get_extension(file_name):
    '''
    Returns a string containing the file extension of a given file
    '''
    return file_name.split('.')[-1].replace('/','')


def get_include_paths(root):
    '''
        Walks through the file tree of the given root directory and returns
            a dictionary containing names and paths of all subdirectories and
            a list of all files within those directories
    '''
    file_tree_paths = {
        'root'        : root,
        'directories' : [],
        'files'       : [],
    }

    for dir_path, subdir_names, file_names in walk(root):
        file_tree_paths['directories'].append(dir_path)

        for file_name in file_names:
            file_path = path.join(dir_path, file_name)
            file_tree_paths['files'].append(file_path)
   
    return file_tree_paths


def get_raw_scss(file_tree_paths):
    '''
    Iterates over a list of files. If the file's extension is .scss,
        open it, read its contents and add them to a string of raw SCSS.
        Returns raw SCSS data
    '''
    raw_scss = ''
    scss_vars = ''

    file_paths = file_tree_paths['files']
    for file_path in file_paths:

        if get_extension(file_path) == 'scss':
            with open(file_path, 'r') as scss_file:
                raw_scss += '\n'

                # ignore @import lines, it's all getting smooshed together anyway
                # separate scss vars
                for line in scss_file.readlines():
                    if '@import' in line:
                        continue
                    elif line[0] == "$":
                        scss_vars += line
                    else:
                        raw_scss += line + '\n'

    # add scss vars at the very top of all scss
    # this is a workaround for lack of support for @import
    # in Libsass (or my own inability to figure it out)
    raw_scss = scss_vars + raw_scss

    return raw_scss

def write_css(compiled_css, css_dir, css_filename):
    '''
        Creates a new css file in the target CSS directory if it doesn't exist,
            then overwrites all contents with the compiled CSS.
    '''
    print(f'{css_dir=}')
    new_file_path = css_dir + css_filename

    with open(new_file_path, 'a+') as css_file:
        css_file.truncate(0)
        css_file.write(compiled_css)

    return

def read_config(root):
    '''
        Open config.json and create a dictionary of new option values to override defaults.
    '''
    file_list = listdir(root)

    print(file_list)
    if 'config.json' in file_list:
        print(path.join(path.abspath(root), 'config.json'))
        with open(path.join(root, 'config.json'), 'r') as config:
            options = json.load(config)
        return options

@click.option('--root', default='./', 
                help='Path to directory containing SCSS files and subfolders with SCSS files. Default is ./')
@click.option('--css_dir', default='./', 
                help='Path to directory to receive CSS output file. Default is ./')
@click.option('--css_filename', default='index.css', 
                help='Name of CSS output file. Default is index.css')
@click.option('--output_style', default='expanded', 
                help='Format of generated CSS. Options: expanded, nested, compact, compressed')
@click.command()
def compile_scss(root, css_dir, css_filename, output_style):
    options = read_config(root)
    print(getcwd())
    
    if options != {}:
        print(options)
        # Get new option values from config.txt
    else:
        root = format_directory_name(root)
        css_dir  = format_directory_name(css_dir)
 
        if valid_path(root):
            file_tree_paths = get_include_paths(root)

            if dir_contains_extension(root, '.scss'):
                file_list = listdir(root)
                
                raw_scss = get_raw_scss(file_tree_paths)

                compiled_css = sass.compile(
                    string=raw_scss, 
                    output_style=f"{output_style}"
                )

            write_css(compiled_css, css_dir, css_filename)

