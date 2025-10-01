"""Shared Rich help formatter for dropfix CLI tools"""
import argparse
import re

from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


console = Console()


class RichHelpFormatter(argparse.RawDescriptionHelpFormatter):
    """Custom formatter that uses Rich for help output"""

    def __init__(self, *args, title="Help", **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title

    def format_help(self):
        help_text = super().format_help()
        lines = help_text.split('\n')

        # Extract usage and description
        usage_line = ""
        description = ""
        options = []

        in_options = False
        current_option = None

        for line in lines:
            if line.startswith('usage:'):
                usage_line = line
            elif line.strip() and not line.startswith(' ') and not line.startswith('-') and 'options:' not in line.lower():
                description = line
            elif 'options:' in line.lower():
                in_options = True
            elif in_options and line.strip().startswith('-'):
                # Parse option line
                match = re.match(r'(\s*-[^\s]+(?:\s+[^\s,]+)?(?:,\s+-[^\s]+)?)\s{2,}(.+)', line)
                if match:
                    flag = match.group(1).strip()
                    desc = match.group(2).strip()
                    current_option = [flag, desc]
                    options.append(current_option)
            elif in_options and line.strip() and current_option:
                # Continuation of previous description
                current_option[1] += " " + line.strip()

        # Parse usage line to bold "usage:" and dim the rest
        usage_match = re.match(r'(usage:)(.+)', usage_line)
        if usage_match:
            usage_text = Text()
            usage_text.append(usage_match.group(1), style="bold white")
            usage_text.append(usage_match.group(2), style="dim")
        else:
            usage_text = Text(usage_line, style="white")

        desc_text = Text(description, style="cyan")

        # Create table for options
        options_table = Table(show_header=False, box=None, padding=(0, 2), border_style=None)
        options_table.add_column("Flag", style="bright_green", no_wrap=True)
        options_table.add_column("Description", style="dim")

        for flag, desc in options:
            options_table.add_row(flag, desc)

        # Build layout
        help_group = Group(
            usage_text,
            Text(""),
            desc_text,
            Text(""),
            Text("options:", style="bold white"),
            options_table
        )

        console.print(Panel(help_group, title=f"[bold cyan]{self.title}[/bold cyan]", border_style="cyan"))
        return ""  # Return empty string since we've already printed