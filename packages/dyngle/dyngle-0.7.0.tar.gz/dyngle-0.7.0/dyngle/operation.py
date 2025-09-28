from dataclasses import dataclass
from functools import cached_property
import re
import shlex
import subprocess

from dyngle.error import DyngleError
from dyngle.template import Template


@dataclass
class Operation:

    local_expressions: dict

    steps: list

    def run(self, data: dict, global_expressions: dict):
        # The data dict is mutable
        steps = self.steps
        expressions = global_expressions | self.local_expressions
        for markup in steps:
            step = Step(markup)
            step.run(data, expressions)


STEP_PATTERN = re.compile(
    r'^\s*(?:([\w.-]+)\s+->\s+)?(.+?)(?:\s+=>\s+([\w.-]+))?\s*$')


def parse_step(markup):
    if match := STEP_PATTERN.match(markup):
        input, command_text, output = match.groups()
        command_template = shlex.split(command_text.strip())
        return input, command_template, output
    else:
        raise DyngleError(f"Invalid step markup {{markup}}")


@dataclass
class Step:

    markup: str

    def __post_init__(self):
        self.input, self.command_template, self.output = \
            parse_step(self.markup)

    def run(self, data, expressions):
        command = [Template(word).render(data, expressions)
                   for word in self.command_template]
        pipes = {}
        if self.output:
            pipes['stdout'] = subprocess.PIPE
        result = subprocess.run(command, text=True, **pipes)
        if result.returncode != 0:
            raise DyngleError(
                f'Step failed with code {result.returncode}: {self.markup}')
        if self.output:
            data[self.output] = result.stdout
