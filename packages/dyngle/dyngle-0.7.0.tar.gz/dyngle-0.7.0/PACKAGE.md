# Dyngle

Use cases

- A task runner 
- A lightweight workflow engine
- A replacement for Make in Python projects
- A replacement for short functions in RC files
- Freedom from quirky Bash syntax

Technical foundations

- Configuration, task definition, and flow control in YAML
- Operations as system commands using a familiar shell-like syntax
- Expressions and logic in pure Python

## Quick installation (MacOS)

```bash
brew install python@3.11
python3.11 -m pip install pipx
pipx install dyngle
```

## Getting started

Create a file `.dyngle.yml`:

```yaml
dyngle:
  operations:
    hello:
      - echo "Hello world"
```

Run an operation:

```bash
dyngle run hello
```

## Configuration

Dyngle reads configuration from YAML files. You can specify the config file location using:

- `--config` command line option
- `DYNGLE_CONFIG` environment variable  
- `.dyngle.yml` in current directory
- `~/.dyngle.yml` in home directory

## Operations

Operations are defined under `dyngle:` in the configuration. In its simplest form, an Operation takes the form of a YAML array defining the steps, as a system command with space-separated arguments. In that sense, a Dyngle operation looks something akin to a "PHONY" Make target, a short Bash script, or a CI/CD job. As a serious example, consider the `init` operation from the Dyngle configuration delivered with the project's source code.

```yaml
dyngle:
  operations:
    init:
      - rm -rf .venv
      - python3.11 -m venv .venv
      - .venv/bin/pip install --upgrade pip poetry
```

The elements of the YAML array _look_ like lines of Bash, but Dyngle replaces the shell with YAML-based flow control and Python-based expressions (described below). So shell-specific operators such as `|`, `>`, and `$VARIABLES` won't work.

## Data and Templates

Dyngle maintains a block of Data throughout an operation, which is a set of named values (Python `dict`, YAML "mapping"). The values are usually strings but can also be other data types that are valid in both YAML and Python.

The `dyngle run` command feeds the contents of stdin to the Operation as Data, by converting a YAML mapping to named Python values. The values may be substituted into commands or arguments in Steps using double-curly-bracket syntax (`{{` and `}}`) similar to Jinja2.

For example, consider the following configuration:

``` yaml
dyngle:
  operations:
    hello:
      - echo "Hello {{name}}!"
```

Cram some YAML into stdin to try it in your shell:

```bash
echo "name: Francis" | dyngle run hello
```

The output will say:

```text
Hello Francis!
```

## Expressions

Operations may contain Expressions, written in Python, that can be referenced in operation steps using the same syntax as for Data. In the case of a naming conflict, an Expression takes precedence over Data with the same name. Expressions can reference names in the Data directly.

Expressions may be defined in either of two ways in the configuration:

1. Global Expressions, under the `dyngle:` mapping, using the `expressions:` key.
2. Local Expressions, within a single Operation, in which case the Steps of the operation require a `steps:` key.

Here's an example of a global Expression

```yaml
dyngle:
  expressions:
    count: len(name)    
  operations:
    say-hello:
      - echo "Hello {{name}}! Your name has {{count}} characters."
```

For completeness, consider the following example using a local Expression for the same purpose.

```yaml
dyngle:
  operations:
    say-hello:
      expressions:
        count: len(name)
      steps:
        - echo "Hello {{name}}! Your name has {{count}} characters."
```

Expressions can use a controlled subset of the Python standard library, including:

- Built-in data types such as `str()`
- Essential built-in functions such as `len()`
- The core modules from the `datetime` package (but some methods such as `strftime()` will fail)
- A specialized function called `formatted()` to perform string formatting operations on a `datetime` object
- A restricted version of `Path()` that only operates within the current working directory
- Various other useful utilities, mostly read-only, such as the `math` module
- A special function called `resolve` which resolves data expressions using the same logic as in templates
- An array `args` containing arguments passed to the `dyngle run` command after the Operation name

**NOTE** Some capabilities of the Expression namespace might be limited in the future. The goal is support purely read-only operations within Expressions.

Expressions behave like functions that take no arguments, using the Data as a namespace. So Expressions reference Data directly as local names in Python.

YAML keys can contain hyphens, which are fully supported in Dyngle. To reference a hyphenated key in an Expression, choose:

- Reference the name using underscores instead of hyphens (they are automatically replaced), OR
- Use the built-in special-purpose `resolve()` function (which can also be used to reference other expressions)



```yaml
dyngle:
  expressions:
    say-hello: >-
        'Hello ' + full_name + '!'
```

... or using the `resolve()` function, which also allows expressions to essentially call other expressions, using the same underlying data set.

```yaml
dyngle:
  expressions:
    hello: >-
        'Hello ' + resolve('formal-name') + '!'
    formal-name: >-
        'Ms. ' + full_name
```

Note it's also _possible_ to call other expressions by name as functions, if they only return hard-coded values (i.e. constants).

```yaml
dyngle:
  expressions:
    author-name: Francis Potter
    author-hello: >-
        'Hello ' + author_name()
``` 

Here are some slightly more sophisticated exercises using Expression reference syntax:

```yaml
dyngle:
  operations:
    reference-hyphenated-data-key:
      expressions:
        spaced-name: "' '.join([x for x in first_name])"
        count-name: len(resolve('first-name'))
        x-name: "'X' * int(resolve('count-name'))"
      steps:
        - echo "Your name is {{first-name}} with {{count-name}} characters, but I will call you '{{spaced-name}}' or maybe '{{x-name}}'"
    reference-expression-using-function-syntax:
      expressions:
        name: "'George'"
        works: "name()"
        double: "name * 2"
        fails: double()
      steps:
        - echo "It works to call you {{works}}"
        # - echo "I have trouble calling you {{fails}}"
```

Finally, here's an example using args:

```yaml
dyngle:
  operations:
    name-from-arg:
      expressions:
        name: "args[0]"
      steps:
        - echo "Hello {{name}}"
```

## Data assignment operator

The Steps parser supports one special operator which assigns the output (stdout) of its command to a Data field for use in subsequent steps.

The operator is `=>` and must go after the command and its arguments. Follow the operator with the name of the Data key to assign.

Example:

```yaml
dyngle:
  operations:
    today:
      expressions:
        just-the-date: resolve('full-date')[0:10]
      steps:
        - date => full-date
        - echo "Today is {{just-the-date}}"
```

(Note Dyngle does provide Python date operations in the Expression namespace, which might provide a better way to perform the same operation as this example, but it suffices to demonstrate assignment)

## Lifecycle

The lifecycle of an operation is:

1. Load Data if it exists from YAML on stdin (if no tty)
2. Find the named Operation in the configuration
2. Perform template rendering on the first Step, using Data and Expressions
3. Execute the Step in a subprocess
4. Continue with the next Step

Note that operations in the config are _not_ full shell lines. They are passed directly to the system.

## Imports

Configuration files can import other configuration files, by providing an entry `imports:` with an array of filepaths. The most obvious example is a Dyngle config in a local directory which imports the user-level configuration.

```yaml
dyngle:
  imports:
    - ~/.dyngle.yml
  expressions:
  operations:
```

In the event of item name conflicts, expressions and operations are loaded from imports in the order specified, so imports lower in the array will override those higher up. The expressions and operations defined in the main file override the imports. Imports are not recursive.

## Security

Commands are executed using Python's `subprocess.run()` with arguments split in a shell-like fashion. The shell is not used, which reduces the likelihood of shell injection attacks. However, note that Dyngle is not robust to malicious configuration. Use with caution.

