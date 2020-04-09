import sass
import click
from . import tools

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
    options = tools.read_config(root)
    print(options)
    if options != {}:
        # root = getcwd()
        css_dir = options['css_dir']
        css_filename = options['css_filename']
        output_style = options['output_style']

    print(f"{root=}, {css_dir=}, {css_filename=}, {output_style=}")

    root = tools.format_directory_name(root)
    css_dir  = tools.format_directory_name(css_dir)

    if tools.valid_path(root):
        file_tree_paths = tools.get_include_paths(root)

        if tools.dir_contains_extension(root, '.scss'):
            file_list = tools.listdir(root)
            
            raw_scss = tools.get_raw_scss(file_tree_paths)

        compiled_css = sass.compile(
            string=raw_scss, 
            output_style=f"{output_style}"
        )

        tools.write_css(compiled_css, css_dir, css_filename)

