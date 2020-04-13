import sass   # SCSS => CSS compiler
import click  # For turning functions into terminal commands

from src.utilities import *      # extra functions for gathering SCSS and processing CSS
from src.observe_files import *  # Watchdog observer and associated functions
from src.config import *         # R.E.P.L for setting option values and generating JSON config file

@click.option('--root', default='./', 
                help='Path to root project directory. Default is ./')
@click.option('--scss_dir', default='./scss', type= click.Path(dir_okay=True, resolve_path=True),
                help='Path the directory containing SCSS files and subfolders with SCSS files Default is ./scss')
@click.option('--css_dir', default='./css', 
                help='Path to directory to receive CSS output file. Default is ./css')
@click.option('--css_filename', default='index.css', 
                help='Name of CSS output file. Default is index.css')
@click.option('--output_style', default='expanded', 
                help='Format of generated CSS. Options: expanded, nested, compact, compressed')
@click.option('--config', is_flag=True,
                help='Check current configuration or set new values for compile_scss_config.json file.')
@click.command()
@click.pass_context
def compile_scss(ctx, root, scss_dir, css_dir, css_filename, output_style, config):
    '''
    Main command in Compile SCSS package.

    Run: 'compile_scss --help' to view all usage options.
    '''

    print(f"{click.get_current_context() = }")

    # Create dictionary of default option values
    defaults = {
        'root'        : format_directory_name(root),
        'scss_dir'    : format_directory_name(scss_dir),
        'css_dir'     : format_directory_name(css_dir),
        'css_filename': css_filename,
        'output_style': output_style,
    }

    # check for config file in root directory and 
    # override defaults to config dict if found,
    # otherwise, options = {}
    config = read_config_file(root)

    # if no config was found, set defaults dict to default options
    if config == {}:
        options = set_config_file(config)
    else:
        click.echo(f"\n*** Config file loaded: *** \n{path.join(path.abspath(root), 'compile_scss_config.json')}\n")
        
    # if the --config flag is True, pass the default options
    # to set_config_file to edit or create the config file
    if config:
        options = set_config_file(defaults)

    print(f"{options = }")
    scss_dir = options['scss_dir']

    file_tree = get_include_paths(scss_dir)
    raw_scss = get_raw_scss(file_tree, scss_dir)
    if raw_scss != '':
        write_css(raw_scss, options)
    else:
        message = f"No SCSS found in SCSS directory: {scss_dir}"
        set_config_file(options, message)
