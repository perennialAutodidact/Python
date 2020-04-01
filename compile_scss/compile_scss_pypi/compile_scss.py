import sass
import click
from sys import exc_info
from os import path, listdir



def valid_path(filepath):
    '''
    If given file path exists, return True, 
        otherwise raise BadParameter error
    '''
    if(path.exists(filepath)):
        return True
    else:
        raise click.BadParameter(f"The directory {filepath} does not exist.")

def dir_contains_extension(dir, ext):
    '''
    Searches specified directory for a particular file extension
    If at least one file in the directory contains the given extension, return True,
        otherwise, raise BadParamter error
    '''
    if valid_path(dir):
        file_list = listdir(dir)

    if [True for filename in file_list if '.scss' in filename] != []:
        return True
    else:
        raise click.BadParameter(f"The path: '{dir}' does not contain any files with the {ext} extension.")

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
    if valid_path(scss_dir):
        if dir_contains_extension(scss_dir, '.scss'):
            file_list = listdir(scss_dir)
            print(file_list)
       

