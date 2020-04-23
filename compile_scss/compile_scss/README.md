# Compile SCSS

## v0.9.1

A CLI utility for compiling multiple SCSS files into a single CSS file to avoid linking a million CSS files within a project. Compile SCSS utilizes Click to construct its CLI interface.

## Installation

This doesn't work yet, but will soon:

`pip install compile_scss`

---

## Usage

Run `compile_scss`

If `compile_scss` is run without any options or flags, *Compile SCSS* will look in the project's root directory for a file named `compile_scss_config.json`, which stores a JSON object with user's predefined configuration values.

If a configuration file is found *Compile SCSS* will run using the configuration found in the JSON file. If no configuration file is found, a Read, Evaluate, Print, Loop (R.E.P.L.) will be triggered and the user will have the option to set new configuration values with a series of prompts.

---

## Options

`--root <PROJECT_ROOT_DIRECTORY>`

>The `--root` option allows the user to specify their project's root directory. *Compile SCSS* will search that directory for the `compile_scss_config.json` file. >
>
>The default path to the root directory is `./`, which translates to whichever directory from which `compile_scss` is called.

---

`--set-config`

> If the `--set-config` flag is present, the configuration R.E.P.L. will be triggered by default.
>
>If a configuration file was found, the user will have the option to either create a new configuration file or continue with the values found in the configuration file.
>
>If no configuration file was found, the user will have the option to create a new configuration file.

---

`--watch`

> If the `--watch` flag is present, *Compile SCSS* will observe the SCSS directory specified in the configuration file for any changes and update the CSS file accordingly.

---

## Configuration

By default, *Compile SCSS* will look in the project's root directory for a file named `compile_scss_config.json`. The file must be present and contain a valid configuration object in order for *Compile SCSS* to run.

The configuration file must contain five keys and corresponding values:

* **root** - The project's root directory. The default value for this is `./`

* **scss_dir** - The top-level SCSS directory for the project. This directory can contain subdirectories and as many SCSS files as needed. The `scss_dir` path must lead to a directory containing at least one SCSS file in order to be a valid SCSS path.

* **css_dir** - The CSS directory containing the main CSS file. This is where *Compile SCSS* will generate its CSS output file.

* **css_filename** - The desired name of the target CSS file.
    >The filename must not contain special characters other than non-leading/trailing hyphens or underscores. The file extension must be lowercase, but the filename can contain capital letters.
    >
    >See the examples below for valid and invalid filenames.

* **output_style** - Libsass' `sass.compile()` allows CSS output to be compiled in one of four styles:
  * compact

  * compressed

  * expanded

  * nested

### Valid and invalid CSS filenames

#### *Valid*

```python
index.css      # recommended format

iNdEx.css      # capital letters okay
i-n-d-e-x.css  # hyphens okay
home_page.css  # underscores okay
m4in.css       # numbers okay
```

#### *Invalid*

```python
-index-.css  # no leading or trailing hyphens
m@!n.css     # no special characters
index.CSS    # file extension must be lowercase
_index_.css  # no leading or trailing underscores
ind ex.css   # no spaces
```

### Example configuration file

```json
{
    "root": ".",
    "scss_dir": "./static/scss",
    "css_dir": "./static/css",
    "css_filename": "index.css",
    "output_style": "expanded"
}
```

---

*Compile SCSS* is still in development. It has been tested successfully but not extensively with:

* Variables
* @import statements
* Functions (basic)
* Mixins (basic)
