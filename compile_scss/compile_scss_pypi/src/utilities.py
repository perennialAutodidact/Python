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

def dir_contains_extension(directory, extension):
    '''
    Searches specified directory for a particular file extension
    If at least one file in the directory contains the given extension, return True,
        otherwise, return False
    '''
    if valid_path(directory):
        file_list = listdir(directory)

    # if at least one filename in the directory ends in .scss, return True
    if [True for file_name in file_list if '.scss' in file_name] != []:
        return True
    else:
        return False

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

    # dictionary of file tree info,
    # populated below
    file_tree = {
        'root'        : root,
        'directories' : [],
        'files'       : [],
    }

    # Iterate through the 3-tuple yielded by walk()
    for dir_path, subdir_names, file_names in walk(root):

        # createa list of all the subdirectories of root
        file_tree['directories'].append(dir_path)

        # create a list of all the files within root
        # and all its subdirectories
        for file_name in file_names:
            file_path = path.join(dir_path, file_name)
            file_tree['files'].append(file_path)
   
    return file_tree


def get_raw_scss(file_tree):
    '''
    Iterates over a list of files. If the file's extension is .scss,
        open it, read its contents and add them to a string of raw SCSS.
        Returns raw SCSS data
    '''
    raw_scss = ''
    scss_vars = ''

    # For each file in the file tree
    file_paths = file_tree['files']
    for file_path in file_paths:

        # if the file's extension is .scss
        if get_extension(file_path) == 'scss':

            # open the file and add its contents to raw_scss variable
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
    new_file_path = css_dir + css_filename

    # open the target css file, otherwise create it
    with open(new_file_path, 'a+') as css_file:
        # remove all contents
        css_file.truncate(0)

        # write new contents
        css_file.write(compiled_css)

    return


def read_config(root):
    '''
        Open compile_scss_config.json and create a dictionary
        of new option values to override defaults.
        returns a blank dictionary if no config file exists.
    '''
    file_list = listdir(root)
    config_file = 'compile_scss_config.json'

    options = None
    # if config_file is in the list of files
    if config_file in file_list:

        options = {}
        full_path = path.join(root, config_file)

        # open the file, read the contents and parse
        # json object into a dictionary
        with open(full_path, 'r') as config:
            options = json.load(config)
            print(type(options))
    return options

