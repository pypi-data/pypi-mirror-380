#!/usr/bin/env python3
# ABOUTME: AI-powered code translator that converts code between languages with idiomatic optimizations
# ABOUTME: Uses Claude Sonnet 4.5's extended thinking to explain translation decisions

import typer
from typing import Optional
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.markdown import Markdown
from rich.columns import Columns
from rich.text import Text
import anthropic
import os
import sys

app = typer.Typer(help="🌍 Polyglot - AI Code Translator with Extended Thinking")
console = Console()

LANGUAGE_EXTENSIONS = {
    'python': 'py', 'rust': 'rs', 'go': 'go', 'typescript': 'ts',
    'javascript': 'js', 'java': 'java', 'cpp': 'cpp', 'c': 'c',
    'ruby': 'rb', 'php': 'php', 'swift': 'swift', 'kotlin': 'kt'
}

def get_anthropic_client():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[red]Error: ANTHROPIC_API_KEY environment variable not set[/red]")
        raise typer.Exit(1)
    return anthropic.Anthropic(api_key=api_key)

def translate_code(source_code: str, source_lang: str, target_lang: str, explain: bool = True):
    """Translate code using Claude Sonnet 4.5 with extended thinking"""
    client = get_anthropic_client()

    prompt = f"""Translate the following {source_lang} code to {target_lang}.

Requirements:
1. Preserve the original functionality and logic
2. Use idiomatic {target_lang} patterns and best practices
3. Optimize for {target_lang}'s strengths
4. Include brief comments explaining non-obvious translations
5. Return ONLY the translated code, no explanations outside the code

Source Code ({source_lang}):
```{source_lang}
{source_code}
```

Translated {target_lang} code:"""

    with console.status(f"[bold cyan]Translating from {source_lang} to {target_lang}...", spinner="dots"):
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            thinking={
                "type": "enabled",
                "budget_tokens": 2000
            } if explain else {
                "type": "disabled"
            },
            messages=[{"role": "user", "content": prompt}]
        )

    # Extract thinking and translated code
    thinking_text = ""
    translated_code = ""

    for block in response.content:
        if block.type == "thinking":
            thinking_text = block.thinking
        elif block.type == "text":
            translated_code = block.text

    # Clean up code blocks if present
    if "```" in translated_code:
        lines = translated_code.split("\n")
        code_lines = []
        in_code_block = False
        for line in lines:
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block or (not "```" in translated_code):
                code_lines.append(line)
        translated_code = "\n".join(code_lines).strip()

    return translated_code, thinking_text

@app.command()
def translate(
    source_lang: str = typer.Argument(..., help="Source language (e.g., python, rust, go)"),
    target_lang: str = typer.Argument(..., help="Target language (e.g., python, rust, go)"),
    file: Optional[Path] = typer.Option(None, "--file", "-f", help="File to translate"),
    show_thinking: bool = typer.Option(True, "--thinking/--no-thinking", help="Show AI reasoning"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output file")
):
    """Translate code between programming languages with AI-powered optimization"""

    # Read source code
    if file:
        if not file.exists():
            console.print(f"[red]Error: File {file} not found[/red]")
            raise typer.Exit(1)
        source_code = file.read_text()
    else:
        console.print("[cyan]Enter your code (press Ctrl+D when done):[/cyan]")
        source_code = sys.stdin.read()

    if not source_code.strip():
        console.print("[red]Error: No code provided[/red]")
        raise typer.Exit(1)

    # Normalize language names
    source_lang = source_lang.lower()
    target_lang = target_lang.lower()

    # Translate
    translated_code, thinking = translate_code(source_code, source_lang, target_lang, show_thinking)

    # Display results
    console.print("\n")
    console.print(Panel.fit(
        f"[bold cyan]{source_lang.title()}[/bold cyan] → [bold green]{target_lang.title()}[/bold green]",
        title="🌍 Polyglot Translation"
    ))

    if show_thinking and thinking:
        console.print("\n[bold yellow]🧠 AI Reasoning Process:[/bold yellow]")
        console.print(Panel(thinking, border_style="yellow", padding=(1, 2)))

    console.print("\n[bold green]✨ Translated Code:[/bold green]")
    syntax = Syntax(translated_code, target_lang, theme="monokai", line_numbers=True)
    console.print(Panel(syntax, border_style="green", padding=(1, 2)))

    # Save to file if requested
    if output:
        output.write_text(translated_code)
        console.print(f"\n[green]✅ Saved to {output}[/green]")

    # Show comparison
    console.print("\n[bold]📊 Side-by-side Comparison:[/bold]")
    source_syntax = Syntax(source_code, source_lang, theme="monokai", line_numbers=True)
    target_syntax = Syntax(translated_code, target_lang, theme="monokai", line_numbers=True)

    console.print(Columns([
        Panel(source_syntax, title=f"[cyan]{source_lang.title()}[/cyan]", border_style="cyan"),
        Panel(target_syntax, title=f"[green]{target_lang.title()}[/green]", border_style="green")
    ]))

@app.command()
def languages():
    """List supported programming languages"""
    console.print("\n[bold cyan]🌍 Supported Languages:[/bold cyan]\n")
    langs = list(LANGUAGE_EXTENSIONS.keys())
    for i in range(0, len(langs), 4):
        row = "  ".join(f"[green]• {lang:<12}[/green]" for lang in langs[i:i+4])
        console.print(row)
    console.print()

if __name__ == "__main__":
    app()
