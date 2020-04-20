import click
from src.utilities import valid_path, format_directory_name
import re
import json

def display_config(config):
    click.echo("\tYour current configuration:")

    click.echo(f"\t{'-' * 30}")
    for key in config.keys():
        click.echo(f"\t- {key}: {config[key]}")
    
    return

def set_config_file(config, config_file_path = '', message = ''):
    '''
    Read, Evaluate, Print, Loop allowing the user to set 
    new option values and generating a JSON config file or 
    to return the default values set within compile_scss
    '''
    print(f"{config = }")

#     menu_config_with_config = {
#         '1': 'Create or edit configuration file',
#         '2': 'Use current configuration',
#         '3': 'Exit',
#     }

#     menu_config_no_config = {
#         '1': 'Create configuration file',
#         '2': 'Exit',
#     }

#     splash_msg = "Configure Compile SCSS"
#     display_message(splash_msg, divider='-', width = 40)

#     if message != '':
#         display_message(message, divider='', width = len(message) // 2, no_top = True)


#     if config_file == '':
#         click.echo(f"No configuration file was found in the current root directory:\n\n\t{config['root']}")
#         menu_config = menu_config_no_config
#     else:
#         click.echo(f"Configuration file loaded: {config_file}\n")
#         menu_config = menu_config_no_config

#         if config != {}:
#             click.echo("\tYour current configuration:")

#             click.echo(f"\t{'-' * 30}")
#             for key in config.keys():
#                 click.echo(f"\t- {key}: {config[key]}")

#     while True:
#         click.echo("\nPlease choose from the following config: \n")
    
#         #  display each menu option with it's message
#         for number in menu_config.keys():
#             click.echo(f"{number}. {menu_config[number]}")

#         choice = click.prompt("\nEnter the number of your selection")
#         if choice not in menu_config.keys():
#             message = f"Your entry '{choice}' is not a valid selection"
#             display_message(message, divider='* ', width=len(message)//2)
#             continue
#         elif choice == "1":
#             #  ask user for a value for each config option
#             config = prompt_for_config(config)
#             break
#         elif choice == "2":

#             # if no config file, exit with option 2
#             if config_file == '':
#                 click.echo("\nGoodbye!\n")
#                 exit()
#             break
#         elif choice == "3":
#             click.echo("\nGoodbye!\n")
#             exit()

#     return config



# def prompt_for_config(config):
#     '''
#     REPL that prompts user for a value for each option,
#     if they choose to override the default config.
#     '''
#     OUTPUT_STYLES = ['compact', 'compressed', 'expanded', 'nested']
#     prompts = {
#         'root': {
#             'msg': "the path to your project's root directory"
#         },
#         'scss_dir':{
#             'msg': "the path to your main SCSS directory"
#         },
#         'css_dir': {
#             'msg': "the path to your target CSS directory"
#         },
#         'css_filename': {
#             'msg': "the file name you'd like for your CSS file"
#         },
#         'output_style': {
#             'msg': f"the output style of your CSS ({', '.join(['compact', 'compressed', 'expanded', 'nested'])})",
#             'config': OUTPUT_STYLES
#         }
#     }

#     filename_regex = r'[^\WA-Z0-9\-_][a-z-]+'

#     while True:
#         for key in config.keys():
#             while True:
#                 prompt_message = prompts[key]['msg']
#                 user_entry = click.prompt(f"Please enter {prompt_message}")
                
#                 # if prompt is for a directory path, 
#                 # check that the directory exists
#                 if 'directory' in prompt_message:
#                     if not valid_path(user_entry):
#                         invalid_entry(user_entry, 'directory')
#                         continue
#                     else:
#                         config[key] = format_directory_name(user_entry)
#                         break  # break SCSS/CSS directory loops

#                 # receive user value for CSS file name
#                 # and ensure its validity.
#                 elif 'file name' in prompt_message:
#                     default_filename = 'index'
#                     regex_match = re.match(filename_regex, user_entry)
#                     if regex_match:
#                         regex_match = regex_match.group()
#                     else:
#                         regex_match = ''

#                     if not len(regex_match) == len(user_entry) or user_entry[-1] == '-':
#                         invalid_entry(user_entry, 'file name')
#                         click.echo(
#                             f"For the sake of simplicity, please make your file name a single,\nlowercase word with no numbers or punctuation (except non-leading or non-trailing hyphens).\nThe default is '{default_filename}' and the file extension '.css' will be added automatically.\n"
#                         )
#                         continue
#                     else:
#                         config[key] = user_entry + '.css'
#                         break  # break file name loop

#                 # if the prompt has additional config,
#                 # ensure that input is on of them
#                 elif 'config' in prompts[key].keys():
#                     if user_entry not in prompts[key]['config']:
#                         invalid_entry(user_entry, 'output style')

#                         continue
#                     else:
#                         config[key] = user_entry
#                         break  # break output_style config loop
#                 else:
#                     break  # break while loop for current key
        
#         return config

# def write_config(config):
#     new_file_path = config['root'] + 'compile_scss_config.json'

#     # open the target config file, otherwise create it
#     with open(new_file_path, 'a+') as config_file:
#         # remove all contents
#         config_file.truncate(0)

#         # write new contents
#         contents = json.dumps(config, indent=4, separators=(',', ': '))
#         config_file.write(contents)

# def invalid_entry(entry, option_type):
#     '''
#     Display an error message in the config REPL if an invalid entry is provided by ther user.
#     "Your entry: '{entry:str}' is not a valid {option_type:str}."
#     '''
#     error_message = f"\nYour entry: '{entry}' is not a valid {option_type}.\n"
#     divider_top = f"\n{'!'*(len(error_message) + 2)}"
#     divider_bottom = f"{'!'*(len(error_message) + 2)}\n"
    
#     click.echo(divider_top)
#     click.echo(f" {error_message} ")
#     if option_type == 'directory':
#         click.echo(f"Either the directory does not exist yet".center(len(divider_top)-1, ' '))
#         click.echo(f"or its path is not valid".center(len(divider_bottom)-1, ' '))
#     click.echo(divider_bottom)

# def display_message(message, divider, width, no_top = False):
#     if no_top == False:
#         click.echo(f"\n{divider * width}")

#     click.echo(f"{message}".center(width, ' '))
#     click.echo(f"{divider * width}\n")
