import click
from src.utilities import valid_path, format_directory_name
import re
import json

def set_config_file(options, config_file = '', message = ''):
    '''
    Read, Evaluate, Print, Loop allowing the user to set 
    new option values and generating a JSON config file or 
    to return the default values set within compile_scss
    '''

    menu_options = {
        '1': 'Change or create configuration file',
        '2': 'Use current configuration',
        '3': 'Exit',
    }

    splash_msg = " Configure Compile SCSS "
    display_message(splash_msg)

    if message != '':
        click.echo()

    if config_file == '':
        click.echo(f"No configuration file was found in the current root directory: {options['root']}\n")
    else:
        click.echo(f"Configuration file loaded: {config_file}")

    if options != {}:
        click.echo("Your current configuration:")
        for key in options.keys():
            click.echo(f"-{key}: {options[key]}")
        
    while True:
        click.echo("\nPlease choose from the following options: \n")
    
        #  display each menu option with it's message
        for number in menu_options.keys():
            click.echo(f"{number}. {menu_options[number]}")

        choice = click.prompt("\nEnter the number of your selection")
        if choice not in menu_options.keys():
            invalid_entry(choice, 'selection')
            continue
        elif choice == "1":
            #  ask user for a value for each config option
            options = prompt_for_options(options)
            break
        elif choice == "2":
            break
        elif choice == "3":
            click.echo("\nGoodbye!\n")
            exit()

    write_config(options)
    
    return options


def prompt_for_options(options):
    '''
    REPL that prompts user for a value for each option,
    if they choose to override the default options.
    '''
    OUTPUT_STYLES = ['compact', 'compressed', 'expanded', 'nested']
    prompts = {
        'root': {
            'msg': "the path to your project's root directory"
        },
        'scss_dir':{
            'msg': "the path to your main SCSS directory"
        },
        'css_dir': {
            'msg': "the path to your target CSS directory"
        },
        'css_filename': {
            'msg': "the file name you'd like for your CSS file"
        },
        'output_style': {
            'msg': f"the output style of your CSS ({', '.join(['compact', 'compressed', 'expanded', 'nested'])})",
            'options': OUTPUT_STYLES
        }
    }

    filename_regex = r'[^\WA-Z0-9\-_][a-z-]+'

    while True:
        for key in options.keys():
            while True:
                prompt_message = prompts[key]['msg']
                user_entry = click.prompt(f"Please enter {prompt_message}")
                
                # if prompt is for a directory path, 
                # check that the directory exists
                if 'directory' in prompt_message:
                    if not valid_path(user_entry):
                        invalid_entry(user_entry, 'directory')
                        continue
                    else:
                        options[key] = format_directory_name(user_entry)
                        break  # break SCSS/CSS directory loops

                # receive user value for CSS file name
                # and ensure its validity.
                elif 'file name' in prompt_message:
                    default_filename = 'index'
                    regex_match = re.match(filename_regex, user_entry)
                    if regex_match:
                        regex_match = regex_match.group()
                    else:
                        regex_match = ''

                    if not len(regex_match) == len(user_entry) or user_entry[-1] == '-':
                        invalid_entry(user_entry, 'file name')
                        click.echo(
                            f"For the sake of simplicity, please make your file name a single,\nlowercase word with no numbers or punctuation (except non-leading or non-trailing hyphens).\nThe default is '{default_filename}' and the file extension '.css' will be added automatically.\n"
                        )
                        continue
                    else:
                        options[key] = user_entry + '.css'
                        break  # break file name loop

                # if the prompt has additional options,
                # ensure that input is on of them
                elif 'options' in prompts[key].keys():
                    if user_entry not in prompts[key]['options']:
                        invalid_entry(user_entry, 'output style')

                        continue
                    else:
                        options[key] = user_entry
                        break  # break output_style options loop
                else:
                    break  # break while loop for current key
        
        return options

def write_config(options):

    print("WRITE CONFIG CALLED")

    new_file_path = options['root'] + 'compile_scss_config.json'

    # open the target config file, otherwise create it
    with open(new_file_path, 'a+') as config_file:
        # remove all contents
        config_file.truncate(0)

        # write new contents
        contents = json.dumps(options, indent=4, separators=(',', ': '))
        config_file.write(contents)

def invalid_entry(entry, option_type):
    '''
    Display an error message in the config REPL if an invalid entry is provided by ther user.
    "Your entry: '{entry:str}' is not a valid {option_type:str}."
    '''
    error_message = f"Your entry: '{entry}' is not a valid {option_type}."
    click.echo('\n' + '!'*(len(error_message) + 2))
    click.echo(f" {error_message} ")
    click.echo('!'*(len(error_message) + 2) + '\n')

def display_message(message):
    click.echo("-"*len(message))
    click.echo(message)
    click.echo("-"*len(message)+"\n")
