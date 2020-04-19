import json
import sass
import click
import re
from os import path, listdir, remove, walk, getcwd, access, R_OK
from shutil import copyfile

VALID_OUTPUT_STYLES = [
    'compact', 
    'compressed',
    'expanded',
    'nested',
]

def format_directory_name(directory):
    '''
    Expands directory paths with ./, ../, or ~/ and 
    adds a '/' to the end them if it isn't included by the 
    user to prevent file opening/creation errors.
    '''

    directory = path.abspath(path.expanduser(directory))

    if directory[-1] != '/':
            directory += '/'

    return directory

def valid_path(file_path, file_label=''):
    '''
    If given file path can be read from, return True, 
        otherwise, raise an error and return False
    '''
    try:
        file_path = format_directory_name(file_path)

        if access(file_path, R_OK) == False:
            raise FileNotFoundError(f"\nInvalid path. {file_path} does not exist")

    except FileNotFoundError as error:
        click.echo(error)
        if file_label:
            click.echo(f"Please enter a valid {file_label} path in your 'compile_scss_config.json' file and try again.")
            pass
        return False

    return True


def dir_contains_extension(directory, extension):
    '''
    Searches specified directory for a particular file extension
    If at least one file in the directory contains the given extension, return True,
        otherwise, return False
    '''
    if valid_path(directory):
        file_list = listdir(directory)

    # if at least one filename in the directory ends in .scss, return True
    if [True for filename in file_list if '.scss' in filename] != []:
        return True
    else:
        return False

def get_extension(filename):
    '''
    Returns a string containing the file extension of a given file
    '''
    return filename.split('.')[-1].replace('/','')


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
    for dir_path, subdir_names, filenames in walk(root):

        # createa list of all the subdirectories of root
        file_tree['directories'].append(dir_path)

        # create a list of all the files within root
        # and all its subdirectories
        for filename in filenames:
            file_path = path.join(dir_path, filename)
            file_tree['files'].append(file_path)
   
    return file_tree


def get_raw_scss(file_tree, scss_dir):
    '''
    Iterates over a list of files. If the file's extension is .scss,
        open it, read its contents and add them to a string of raw SCSS.
        Returns raw SCSS data
    '''
    root = format_directory_name(scss_dir)

    raw_scss = ''
    if valid_path(scss_dir):
        file_tree = get_include_paths(scss_dir)

        if dir_contains_extension(scss_dir, '.scss'):
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


def write_css(raw_scss, options):
    '''
        Creates a new css file in the target CSS directory if it doesn't exist,
            then overwrites all contents with the compiled CSS.
    '''

    if raw_scss != '':
        compiled_css = sass.compile(
            string=raw_scss, 
            output_style=f"{options['output_style']}"
        )

        new_file_path = options['css_dir'] + options['css_filename']

        # open the target css file, otherwise create it
        with open(new_file_path, 'a+') as css_file:
            # remove all contents
            css_file.truncate(0)

            # write new contents
            css_file.write(compiled_css)
    else:
        return "NO SCSS FOUND"
    return 


def read_config_file(root):
    '''
        Open compile_scss_config.json and create a dictionary
        of new option values to override defaults.
        returns a blank dictionary if no config file exists.
    '''
    file_list = listdir(root)

    config_file = 'compile_scss_config.json'

    # if config_file is in the list of files
    if config_file in file_list:

        full_path = path.join(root, config_file)

            # open the file, read the contents and parse
            # json object into a dictionary
        try:    
            with open(full_path, 'r') as config:
                options = json.load(config)

                if isinstance(options, dict):
                    return options 
                else:
                    raise TypeError("\nYour configuration file does not contain a valid JSON object.")

        # If errors are raised, return an empty dictionary
        except json.JSONDecodeError as error:
            click.echo(error)
            click.echo("\nThere was a problem loading the JSON in your configuration file.\nCheck the JSON syntax and try again, or just run compile_scss\nwith the '--config' flag to generate a new configuration file.")
            return {}

        except TypeError as error:
            click.echo(error)
            return {}

        except PermissionError:
            click.echo("\nYou don't have permission to access the given root directory or configuration file.")
            return {}

    # if no configuration file is found, return an empty dictionary
    return {}


def valid_filename(filename, extension):
    '''
    Return True if a filename and extension match a valid pattern,
    otherwise, raise an error and return False
    
    The file name cannot contain special characters other than non-leading/trailing
    hyphens/underscores. The file extension must be lowercase.

    This is mainly for checking the format of the CSS file generated by Compile SCSS.

    Examples:
    Valid : index.css, i-n-d-e-x.css, main.css, home_page.css, iNdEx.css, page1.css
    Invalid: -index-.css, index.CSS, _index.css, 
    '''
    filename_regex = r'[^\W\_][-\w]*[^\W\_]\.' + extension
    regex_match = re.match(filename_regex, filename)

    try:
        if regex_match == None:
            raise ValueError (f'Invalid CSS filename: {filename}')
    
    except ValueError as error:
        click.echo(error)
        return False
    
    return True

def has_required_keys(options, required_keys):
    '''
    Return True if options dict contains all the keys
    in the keys list. If any keys are missing, 
    raise a KeyError and return False.
    '''
    try:
        missing_keys = []
        for key in required_keys:
            if key not in options.keys():
                missing_keys.append(key)
        if len(missing_keys) > 0:
            missing_keys = '\n'.join(missing_keys)
            raise KeyError

    except KeyError:
        click.echo(f"\nThe following keys are missing from your configuration file:\n\n{missing_keys}\n\nPlease change your configuration file to include those keys or run Compile SCSS with the '--config' flag to create a new configuration file.")
        return False
    
    return True

def config_is_valid(options):
    '''
    Validate each option in the configuration file for Compile SCSS. 
    Raises errors if directory paths do not exist, CSS filename is not valid,
    or the output style is not one of the available options.
    '''
    required_keys  = ['root', 'scss_dir', 'css_dir', 'css_filename', 'output_style']
    output_style = options['output_style']
    
    validations = {
        'config_keys' : has_required_keys(options, required_keys),
        'root_dir'    : valid_path(options['root'], 'project root'),
        'scss_dir'    : valid_path(options['scss_dir'], 'SCSS'),
        'css_dir'     : valid_path(options['css_dir'], 'CSS'),
        'css_filename': valid_filename(options['css_filename'], 'css'),
        'output_style': True if output_style in VALID_OUTPUT_STYLES else False,
    }
    
    try:
        if not all(validations.values()):
            raise ValueError(f'Invalid configuration.')
    except ValueError as error:
        click.echo(error)
        return False
    
    return options