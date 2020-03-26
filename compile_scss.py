import os
import sass

file_list = os.listdir('.')

all_scss = ''

for file in file_list:
    if file[-5::] == '.scss':
        with open(file, 'r') as scss:
            all_scss += '\n'
            for line in scss.readlines():
                all_scss += line

all_scss = sass.compile(string=all_scss, output_style='compressed')

with open('main.css', 'w') as css:
    css.write(all_scss)