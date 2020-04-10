import sass   # SCSS => CSS compiler
import click  # For turning functions into terminal commands

from src.utilities import *  # extra functions for gathering SCSS and processing CSS
from src.observe_files import *  # Watchdog observer and associated functions

@click.option('--root', default='./', 
                help='Path to directory containing SCSS files and subfolders with SCSS files. Default is ./')
@click.option('--css_dir', default='./', 
                help='Path to directory to receive CSS output file. Default is ./')
@click.option('--css_filename', default='index.css', 
                help='Name of CSS output file. Default is index.css')
@click.option('--output_style', default='expanded', 
                help='Format of generated CSS. Options: expanded, nested, compact, compressed')
@click.option('--config / --no-config', default=False, help='Check current configuration or set new values for compile_scss_config.json file.')
@click.command()
def compile_scss(root, css_dir, css_filename, output_style, config):

    # if the config flag is True, set config, 
    # otherwise try to read a config file from root directory
    if config:
        options = set_config()
    else:
        options = read_config(root)

    print(f"{options=}")
    # if no config file is found in root directory,
    # set config, otherwise, override default values
    # with values from config file.
    if options != None:
        root = options['root']
        css_dir = options['css_dir']
        css_filename = options['css_filename']
        output_style = options['output_style']
    else:
        options = set_config({})

    root = format_directory_name(root)
    css_dir  = format_directory_name(css_dir)

    if valid_path(root):
        file_tree = get_include_paths(root)

        if dir_contains_extension(root, '.scss'):
            raw_scss = get_raw_scss(file_tree)

        compiled_css = sass.compile(
            string=raw_scss, 
            output_style=f"{output_style}"
        )

        write_css(compiled_css, css_dir, css_filename)

def set_config(options=None):
    if options == None:
        click.echo("NO CONFIG FILE FOUND")
    else:
        click.echo(f"current config: {options}")
