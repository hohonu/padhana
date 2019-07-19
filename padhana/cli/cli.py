import os
import re

import click
import six
from PyInquirer import (Token, ValidationError, Validator, print_json, prompt,
                        style_from_dict)
from pyfiglet import figlet_format

try:
    import colorama
    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored

except ImportError:
    colored = None

style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})


@click.group()
def cli():
    pass


@click.command()
def run_file():
    click.echo('Initialized the database')

@click.command()
def web_ui():
    """
    Start Web UI
    """
    click.echo("Starting Web UI")


cli.add_command(web_ui)


@click.command()
def help():
    """
    CLI for working with Padhana
    """
    click.echo("Access to pipelines, stores and connectors")


if __name__ == '__main__':
    help()
