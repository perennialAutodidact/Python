import sass
import click
from os import path, listdir, remove, walk
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
        otherwise raise BadParameter error
    '''
    if(path.exists(file_path)):
        return file_path
    else:
        raise click.BadParameter(f"The directory {file_path} does not exist.")

def dir_contains_extension(directory, extension):
    '''
    Searches specified directory for a particular file extension
    If at least one file in the directory contains the given extension, return True,
        otherwise, raise BadParamter error
    '''
    if valid_path(directory):
        file_list = listdir(directory)

    if [True for file_name in file_list if '.scss' in file_name] != []:
        return True
    else:
        raise click.BadParameter(f"The path: '{directory}' does not contain any files with the {extension} extension.")

def get_extension(file_name):
    '''
    Returns a string containing the file extension of a given file
    '''
    return file_name.split('.')[-1]


def get_include_paths(root):
    file_tree_paths = {
        'root'        : root,
        'subdirs'     : {
            # name : path
        },
        'files'       : [],
    }

    for dir_path, subdir_names, file_names in walk(root):

        for subdir_name in subdir_names:
            subdir_name = format_directory_name(subdir_name)
            
            if subdir_name not in file_tree_paths.keys():
                file_tree_paths['subdirs'][subdir_name] = []

            
            subdir_path = path.join(dir_path, subdir_name)
            file_tree_paths['subdirs'][subdir_name].append(subdir_path)

            files = file_tree_paths['files']

            for file_name in file_names:
                file_path = path.join(subdir_path, file_name)
                file_path = format_directory_name(file_path)

                if file_name not in files:
                    files.append(file_path)

        for f in file_tree_paths['files']:
            print(f)

    print(file_tree_paths)
    # return 
def get_raw_scss(directory, dir_files):
    '''
    Iterates over a list of files. If the file's extension is .scss,
        open it, read its contents and add them to a string of raw SCSS.
        Returns raw SCSS data
    '''

    raw_scss = ''
    for file_name in dir_files:

        if get_extension(file_name) == 'scss':
            file_path = directory + file_name
            with open(file_path, 'r') as scss_file:
                raw_scss += '\n'

                for line in scss_file.readlines():
                    raw_scss += line + '\n'

    return raw_scss

def write_css(compiled_css, css_dir, css_filename):
    '''
        Creates a new css file in the target CSS directory if it doesn't exist,
            then overwrites all contents with the compiled CSS.
    '''
    new_file_path = css_dir + css_filename

    with open(new_file_path, 'a+') as css_file:
        css_file.truncate(0)
        css_file.write(compiled_css)

    return

def read_config():
    '''
        Open config.txt and create a dictionary of new option values to override defaults.
    '''
    pass

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
    # options = read_config()
    
    # if options != {}:
    #     pass
    #     # Get new option values from config.txt
    # else:
        root = format_directory_name(root)
        css_dir  = format_directory_name(css_dir)

        if valid_path(root):
            include_paths = get_include_paths(root)

            if dir_contains_extension(root, '.scss'):
                file_list = listdir(root)
                
                raw_scss = get_raw_scss(root, file_list)

                # include_paths=[root, f'{root}pages/']
                # print(file_list)
                # print(include_paths)
                compiled_css = sass.compile(string=raw_scss, 
                                            output_style=f"{output_style}", 
                                            include_paths=[root, f"{root}pages"]
                )

                write_css(compiled_css, css_dir, css_filename)

