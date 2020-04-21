import click
from src.utilities import valid_path, format_directory_name, valid_filename, valid_output_style, config_is_valid
import re
import json

def display_config(config):
    '''
    Display the current contents of the configuration file.
    '''
    click.echo("\nYour current configuration:")

    click.echo(f"{'-' * 30}")
    for key in config.keys():
        click.echo(f"    - {key}: {config[key]}")
    
    return

def display_message(message, divider, width, no_top = False):
    '''
    Display a formatted message to the user.
    '''
    if no_top == False:
        click.echo(f"\n{divider * width}")

    click.echo(f"{message}".center(width, ' '))
    click.echo(f"{divider * width}")

def write_config(config):
    '''
    Convert the config dictionary into JSON, then write the JSON object to compile_scss_config.json
    
    If the file does not exist, it will be created. 
    
    If the file exists it's contents are erased before the new contents are written.
    '''
    new_file_path = config['root'] + 'compile_scss_config.json'

    
    # open the target config file, otherwise create it
    with open(new_file_path, 'a+') as config_file:
        # remove all contents
        config_file.truncate(0)

        # write new contents
        contents = json.dumps(config, indent=4, separators=(',', ': '))
        config_file.write(contents)
    return


def prompt_for_values(config):
    '''
    REPL that prompts user for a value for each option,
    if they choose to override the default config.
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
        },
    }

    while True:
        for key in config.keys():
            prompt_message = prompts[key]['msg']

            while key != 'config_file':
                user_entry = click.prompt(f"\nPlease enter {prompt_message}")
                
                # if prompt is for a directory path, 
                # check that the directory exists
                if 'directory' in prompt_message:
                    if not valid_path(user_entry):
                        error = f'Your entry: {user_entry} is not a valid directory.'
                        display_message(error, divider='* ', width=len(error) // 2 + 1)
                        # invalid_entry(user_entry, 'directory')
                        continue
                    else:
                        config[key] = format_directory_name(user_entry)
                        break  # break SCSS/CSS directory loops

                # receive user value for CSS file name
                # and ensure its validity.
                elif 'file name' in prompt_message:
                    if not valid_filename(user_entry, 'css'):
                        click.echo(
                            f"\nThe file name cannot contain special characters other than non-leading/trailing hyphens/underscores. The file extension must be lowercase."
                        )
                        continue
                    else:
                        config[key] = user_entry
                        break  # break file name loop

                # if the prompt has additional options,
                # ensure that input is on of them
                elif 'options' in prompts[key].keys():
                    if user_entry not in prompts[key]['options']:
                        message = f"You must choose one of these: {', '.join(OUTPUT_STYLES)}"
                        display_message(message, divider='* ', width = len(message) // 2 + 1)
                        continue
                    else:
                        config[key] = user_entry
                        break  # break output_style config loop
                else:
                    break  # break while loop for current key
        
        return config

def set_config_file(config, config_file = ''):
    '''
    Read, Evaluate, Print, Loop allowing the user to set 
    new option values and generating a JSON config file or 
    to return the default values set within compile_scss
    '''

    #  choose menu options base on existence of config_file
    menu_with_config = {
        '1': 'Create or edit configuration file',
        '2': 'Use current configuration',
        '3': 'Exit',
    }

    menu_no_config = {
        '1': 'Create configuration file',
        '2': 'Exit',
    }

    splash_msg = "Configuration!"
    display_message(splash_msg, divider='-', width = 40)

    menu_options = menu_no_config if config_file == '' else menu_with_config 

    if config != {}:
        display_config(config)


    while True:
        click.echo("\nPlease choose from the following config:\n")
    
        #  display each menu option with it's message
        for number in menu_options.keys():
            click.echo(f"{number}. {menu_options[number]}")

        choice = click.prompt("\nEnter the number of your selection")
        if choice not in menu_options.keys():
            message = f"Your entry '{choice}' is not a valid selection"
            display_message(message, divider='* ', width=len(message)//2 + 1)
            continue
        elif choice == "1":
            #  ask user for a value for each config option
            config = prompt_for_values(config)
            
            break
        elif choice == "2":

            # if no config file, exit with option 2
            if config_file == '':
                click.echo("\nGoodbye!\n")
                exit()
            break
        elif choice == "3":
            click.echo("\nGoodbye!\n")
            exit()

    print(f"after set_config: {config = }")
    return config
