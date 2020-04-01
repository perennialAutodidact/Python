import sass
import click
from os import path, listdir, remove
from shutil import copyfile

def format_directory_name(directory):
    if directory[-1] != '/':
            directory += '/'

    return directory

def valid_path(file_path):
    '''
    If given file path exists, return True, 
        otherwise raise BadParameter error
    '''
    if(path.exists(file_path)):
        return file_path
    else:
        raise click.BadParameter(f"The directory {file_path} does not exist.")

def dir_contains_extension(dir, ext):
    '''
    Searches specified directory for a particular file extension
    If at least one file in the directory contains the given extension, return True,
        otherwise, raise BadParamter error
    '''
    if valid_path(dir):
        file_list = listdir(dir)

    if [True for file_name in file_list if '.scss' in file_name] != []:
        return True
    else:
        raise click.BadParameter(f"The path: '{dir}' does not contain any files with the {ext} extension.")

def get_extension(file_name):
    '''
    Returns a string containing the file extension of a given file
    '''
    return file_name.split('.')[-1]

def get_raw_scss(directory, scss_files):
    '''
    Iterates over a list of files. If the file's extension is .scss,
        open it, read its contents and add them to a string of raw SCSS.
        Returns raw SCSS data
    '''

    raw_scss = ''
    scss_vars = ''
    for file_name in scss_files:
        if get_extension(file_name) == 'scss':
            file_path = directory + file_name
            with open(file_path, 'r') as scss_file:
                raw_scss += '\n'

                for line in scss_file.readlines():
                    if '@import' in line:
                        continue
                    elif line[0] == '$':
                        scss_vars += line
                        continue
                    else:
                        raw_scss += line


    raw_scss = scss_vars + raw_scss
    return raw_scss

def write_css(compiled_css, css_dir, css_name):
    new_file_path = css_dir + css_name

    with open(new_file_path, 'a+') as css_file:
        css_file.truncate(0)
        css_file.write(compiled_css)

    return

# @click.option('--config', default=None, 
#                 help='Optional path to config.txt file containing predefined set of options')
@click.option('--scss_dir', default='./', 
                help='Path to directory containing SCSS files. Default is ./')
@click.option('--css_dir', default='./', 
                help='Path to directory to receive CSS output file. Default is ./')
@click.option('--css_name', default='index.css', 
                help='Name of CSS output file. Default is index.css')
@click.option('--output_style', default='expanded', 
                help='Format of generated CSS. Options: expanded, nested, compact, compressed')
@click.command()
def compile_scss(scss_dir,css_dir,css_name,output_style):

    scss_dir = format_directory_name(scss_dir)
    css_dir  = format_directory_name(css_dir)

    if valid_path(scss_dir):
        if dir_contains_extension(scss_dir, '.scss'):
            file_list = listdir(scss_dir)
            
            raw_scss = get_raw_scss(scss_dir, file_list)

            compiled_css = sass.compile(string=raw_scss, output_style=f"{output_style}")

            write_css(compiled_css, css_dir, css_name)