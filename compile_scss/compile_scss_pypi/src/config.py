import click
from src.utilities import valid_path

def set_config(options):
    '''
    Read, Evaluate, Print, Loop allowing the user to set 
    new option values and generating a JSON config file
    '''
    menu_options = {
        '1': 'Setup configuration file',
        '2': 'Use default option values',
        '3': 'Exit',
    }

    click.echo("-"*23)
    click.echo("Configure Compile SCSS")
    click.echo("-"*23+"\n")

    while True:
        click.echo("Please choose from the following options: \n")
    
        for number in menu_options.keys():
            click.echo(f"{number}. {menu_options[number]}")

        choice = click.prompt("\nEnter the number of your selection")
        if choice not in menu_options.keys():
            click.echo('\n' + '!'*35)
            click.echo("  Please enter a valid selection")
            click.echo('!'*35)
            continue
        elif choice == "1":
            options = prompt_for_options(options)
            break
        elif choice == "2":
            break
        elif choice == "3":
            click.echo("Goodbye!")
            exit()
        else:
            continue
    return options


def prompt_for_options(options):
    prompts = {
        'root': {
            'msg': "the path to your SCSS directory"
        },
        'css_dir': {
            'msg': "the path to your target CSS directory"
        },
        'css_filename': {
            'msg': "the name you'd like for your CSS file"
        },
        'output_style': {
            'msg': "the output style of your CSS",
            'options': ['compact', 'compressed', 'expanded', 'nested']
        }
    }
    while True:
        click.echo("")
        for key in options.keys():
            while True:
                options[key] = click.prompt(f"Please enter {prompts[key]['msg']}")
                if 'options' in prompts[key].keys():
                    if options[key] not in prompts[key]['options']:

                        click.echo('\n' + '!'*25)
                        click.echo("That's not a valid option.")
                        click.echo('!'*25)

                        click.echo(f"Enter one of these: {', '.join(prompts[key]['options'])}\n")
                    else:
                        break  # break output_style options
                else:
                    break  # break while loop for current key
        return options