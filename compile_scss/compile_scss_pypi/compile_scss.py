import sass
import click

@click.option('--scss_dir', default='./', 
                help='Path to directory containing SCSS files')
@click.option('--css_dir', default='./', 
                help='Path to directory to receive CSS output file')
@click.option('--css_name', default='index.css', 
                help='Name of CSS output file')
@click.option('--output_style', default='expanded', 
                help='Format of generated CSS. Options: expanded, nested, compact, compressed')
@click.command()
def compile_scss(scss_dir,css_dir,css_name,output_style):
    click.echo(f"{scss_dir=}, {css_dir=}, {css_name=}, {output_style=}")
    
