import sass   # SCSS => CSS compiler
import click  # For turning functions into terminal commands

from src.utilities import *      # extra functions for gathering SCSS and processing CSS
from src.observe_files import *  # Watchdog observer and associated functions
from src.config import *         # R.E.P.L for setting option values and generating JSON config file

@click.option('--root', default='./', 
                help='Path to root project directory. Default is ./')
@click.option('--set-config', is_flag=True,
                help='Check current configuration or set new values for compile_scss_config.json file.')
@click.command()
def compile_scss(root, set_config): #(root, scss_dir, css_dir, css_filename, output_style, config):
    '''
    Main command in Compile SCSS package.

    Run: 'compile_scss --help' to view all usage options.
    '''
    
    # if set_config:
    #     config = set_config_file({})

    # check for config file in root directory and 
    # override defaults to options dict if found,
    # otherwise, options = {}
    config = read_config_file(root)
    config_file_path = path.join(format_directory_name(root), 'compile_scss_config.json')

    print(f"{config = }")
    splash_msg = "Compile SCSS"
    display_message(splash_msg, divider='-', width = 40)
    
    # if no config was found, set defaults dict to default options
    if config == {}:
        # if the --set_config flag is True, pass the default config
        # to set_config_file to edit or create a new config file
        if set_config:
            config = set_config_file(config)
        else:
            error_quit(f"\nNavigate to your project's root directory and check for a configuration file named 'compile_scss_config.json'")
    
    elif config != {}:
        if set_config:
            config = set_config_file(config)
        if not config_is_valid(config):
            error_quit("\nPlease check the configuration file in your project's root directory.")


        config_file = path.join(config['root'], 'compile_scss_config.json')
        click.echo(f"\nConfig file successfully loaded:\n{config_file}")


    
    # if not valid_path(scss_dir):
    #     message = f"*** Invalid SCSS folder ***\n{scss_dir}"
    #     set_config_file(options, config_file = path.join(root, 'compile_scss_config.json'), message = message)
    
    # file_tree = get_include_paths(scss_dir)
    # raw_scss = get_raw_scss(file_tree, scss_dir)
    
    # if raw_scss != '':
    #     write_css(raw_scss, options)
    # elif raw_scss == '':
    #     message = f"*** No SCSS found in SCSS directory: {scss_dir}"
    #     set_config_file(options, config_file = path.join(root, 'compile_scss_config.json'), message=message)


