"""
🎼 ABCWeaver CLI Interface

Click-based command line interface for all abcweaver operations.
"""

import click
from rich.console import Console
from rich.panel import Panel
from . import __version__

console = Console()

@click.group()
@click.version_option(version=__version__, prog_name="abcweaver")
def abcweaver():
    """🎼 ABCWeaver - ABC ↔ MusicXML Transformation Engine
    
    Bidirectional transformation between ABC notation and MusicXML format
    with Redis stream processing capabilities.
    
    Part of the G.Music Assembly ecosystem.
    """
    console.print(Panel.fit("🎼 [bold blue]ABCWeaver[/bold blue] - Musical Transformation Engine", style="blue"))

@abcweaver.command()
@click.argument('abc_string')
@click.option('--output', '-o', required=True, help='Output MusicXML file path')
@click.option('--title', default='Untitled', help='Score title')
@click.option('--composer', default='ABCWeaver', help='Composer name')
def create(abc_string, output, title, composer):
    """Create new MusicXML from ABC notation"""
    console.print(f"[green]Creating MusicXML:[/green] {output}")
    console.print(f"[yellow]ABC:[/yellow] {abc_string}")

    try:
        from .core.converter import Converter

        # Initialize converter
        converter = Converter()

        # Create MusicXML from ABC string
        with console.status(f"[bold green]Creating MusicXML score..."):
            converter.create_musicxml_from_abc(abc_string, output, title, composer)

        # Show success message
        import os
        if os.path.exists(output):
            file_size = os.path.getsize(output)
            console.print(f"[green]✅ MusicXML created![/green] {output} ({file_size:,} bytes)")
            console.print(f"[dim]Title:[/dim] {title}")
            console.print(f"[dim]Composer:[/dim] {composer}")
        else:
            console.print(f"[red]❌ Creation failed - output file not created[/red]")

    except Exception as e:
        console.print(f"[red]Creation failed:[/red] {e}")

@abcweaver.command()
@click.argument('musicxml_file')
@click.argument('abc_string')
@click.option('--part-name', default='New Part', help='Name of the new part')
@click.option('--instrument', default='Piano', help='Instrument name')
@click.option('--clef-sign', default='G', help='Clef sign (G, F, C)')
@click.option('--clef-line', default='2', help='Clef line number')
def insert(musicxml_file, abc_string, part_name, instrument, clef_sign, clef_line):
    """Insert ABC chunk into existing MusicXML"""
    console.print(f"[green]Inserting into:[/green] {musicxml_file}")
    console.print(f"[yellow]ABC:[/yellow] {abc_string}")
    console.print(f"[blue]Part:[/blue] {part_name} ({instrument})")

    try:
        from .core.converter import Converter
        import os

        # Check if input file exists
        if not os.path.exists(musicxml_file):
            console.print(f"[red]❌ MusicXML file not found:[/red] {musicxml_file}")
            return

        # Initialize converter
        converter = Converter()

        # Insert ABC into MusicXML
        with console.status(f"[bold green]Inserting ABC into MusicXML part..."):
            new_part_id = converter.insert_abc_into_musicxml(
                musicxml_file, abc_string, part_name, instrument, clef_sign, clef_line
            )

        # Show success message
        if new_part_id:
            console.print(f"[green]✅ ABC inserted![/green] Created new part: {new_part_id}")
            console.print(f"[dim]Part name:[/dim] {part_name}")
            console.print(f"[dim]Instrument:[/dim] {instrument}")
            console.print(f"[dim]Clef:[/dim] {clef_sign}/{clef_line}")

            # Show file size info
            if os.path.exists(musicxml_file):
                file_size = os.path.getsize(musicxml_file)
                console.print(f"[dim]Updated file size:[/dim] {file_size:,} bytes")
        else:
            console.print(f"[red]❌ Insertion failed - no part ID returned[/red]")

    except Exception as e:
        console.print(f"[red]Insertion failed:[/red] {e}")

@abcweaver.command()
@click.argument('musicxml_file')
@click.option('--part', '-p', help='Part ID to extract (e.g., P1)')
@click.option('--output', '-o', required=True, help='Output ABC file path')
@click.option('--measures', help='Measure range (e.g., 1-8)')
def extract(musicxml_file, part, output, measures):
    """Extract ABC from MusicXML part"""
    console.print(f"[green]Extracting from:[/green] {musicxml_file}")
    console.print(f"[blue]Part:[/blue] {part or 'All parts'}")
    console.print(f"[yellow]Output:[/yellow] {output}")

    try:
        from .core.converter import Converter
        import os

        # Check if input file exists
        if not os.path.exists(musicxml_file):
            console.print(f"[red]❌ MusicXML file not found:[/red] {musicxml_file}")
            return

        # Initialize converter
        converter = Converter()

        # Extract ABC from MusicXML
        with console.status(f"[bold green]Extracting ABC from MusicXML..."):
            abc_content = converter.extract_abc_from_musicxml(musicxml_file, part, measures)

        # Write ABC content to output file
        with open(output, 'w', encoding='utf-8') as f:
            f.write(abc_content)

        # Show success message
        if os.path.exists(output):
            file_size = os.path.getsize(output)
            console.print(f"[green]✅ ABC extracted![/green] Created {output} ({file_size:,} bytes)")

            # Show a preview of the extracted ABC
            lines = abc_content.split('\n')
            if len(lines) > 3:
                console.print(f"[dim]Preview:[/dim]")
                for line in lines[:3]:
                    if line.strip():
                        console.print(f"  {line}")
                if len(lines) > 3:
                    console.print(f"  ... ({len(lines) - 3} more lines)")
        else:
            console.print(f"[red]❌ Extraction failed - output file not created[/red]")

    except Exception as e:
        console.print(f"[red]Extraction failed:[/red] {e}")

@abcweaver.command()
@click.argument('input_file')
@click.option('--output', '-o', required=True, help='Output file path')
@click.option('--format', 'output_format', type=click.Choice(['abc', 'musicxml']), required=True, help='Output format')
@click.option('--part', help='Specific part to convert (for MusicXML → ABC)')
def convert(input_file, output, output_format, part):
    """Convert between ABC and MusicXML formats"""
    console.print(f"[green]Converting:[/green] {input_file} → {output}")
    console.print(f"[blue]Format:[/blue] {output_format}")

    try:
        from .core.converter import Converter
        from .utils.helpers import detect_file_format

        # Initialize converter
        converter = Converter()

        # Auto-detect input format
        try:
            input_format = detect_file_format(input_file)
            console.print(f"[dim]Detected input format:[/dim] {input_format}")
        except Exception as e:
            console.print(f"[red]Error detecting file format:[/red] {e}")
            return

        # Validate conversion direction
        if input_format == output_format:
            console.print(f"[yellow]Warning:[/yellow] Input and output formats are the same ({input_format})")

        # Perform conversion
        with console.status(f"[bold green]Converting {input_format} to {output_format}..."):
            converter.convert_file(input_file, output, input_format, output_format, part)

        # Show success message
        import os
        if os.path.exists(output):
            file_size = os.path.getsize(output)
            console.print(f"[green]✅ Conversion complete![/green] Created {output} ({file_size:,} bytes)")
        else:
            console.print(f"[red]❌ Conversion failed - output file not created[/red]")

    except ImportError as e:
        console.print(f"[red]Import error:[/red] {e}")
    except Exception as e:
        console.print(f"[red]Conversion failed:[/red] {e}")

@abcweaver.command()
@click.argument('file_path')
@click.option('--format', 'file_format', type=click.Choice(['abc', 'musicxml']), help='File format (auto-detect if not specified)')
@click.option('--repair', is_flag=True, help='Attempt to repair issues')
def validate(file_path, file_format, repair):
    """Validate ABC or MusicXML syntax"""
    console.print(f"[green]Validating:[/green] {file_path}")
    console.print(f"[blue]Format:[/blue] {file_format or 'auto-detect'}")

    try:
        from .core.abc_parser import ABCParser
        from .core.validator import Validator
        from .utils.helpers import detect_file_format
        import os

        # Check if file exists
        if not os.path.exists(file_path):
            console.print(f"[red]❌ File not found:[/red] {file_path}")
            return

        # Auto-detect format if not specified
        if not file_format:
            try:
                file_format = detect_file_format(file_path)
                console.print(f"[dim]Detected format:[/dim] {file_format}")
            except Exception as e:
                console.print(f"[red]Error detecting format:[/red] {e}")
                return

        # Initialize appropriate validator
        validator = Validator()

        with console.status(f"[bold green]Validating {file_format} file..."):
            # Validate based on format
            if file_format == 'abc':
                result = validator.validate_abc_file(file_path)
            elif file_format == 'musicxml':
                result = validator.validate_musicxml_file(file_path)
            else:
                console.print(f"[red]❌ Unsupported format:[/red] {file_format}")
                return

        # Display results
        if result.is_valid:
            console.print(f"[green]✅ Validation passed![/green] File is valid {file_format}")
        else:
            console.print(f"[red]❌ Validation failed![/red] Found {len(result.errors)} error(s)")
            for i, error in enumerate(result.errors, 1):
                console.print(f"  [red]{i}.[/red] {error}")

        # Show warnings if any
        if hasattr(result, 'warnings') and result.warnings:
            console.print(f"[yellow]⚠️  {len(result.warnings)} warning(s):[/yellow]")
            for i, warning in enumerate(result.warnings, 1):
                console.print(f"  [yellow]{i}.[/yellow] {warning}")

        # Handle repair option
        if repair and not result.is_valid and file_format == 'abc':
            console.print(f"[blue]🔧 Repair suggestions:[/blue]")
            parser = ABCParser()
            suggestions = parser.suggest_corrections(open(file_path).read())
            for i, suggestion in enumerate(suggestions, 1):
                console.print(f"  [blue]{i}.[/blue] {suggestion}")

    except Exception as e:
        console.print(f"[red]Validation failed:[/red] {e}")

# Stream commands group
@abcweaver.group()
def stream():
    """Redis stream operations via nyro package"""
    pass

@stream.command('send')
@click.argument('abc_string')
@click.option('--stream-name', default='abcweaver_abc', help='Redis stream name')
@click.option('--metadata', help='Additional metadata (JSON format)')
def stream_send(abc_string, stream_name, metadata):
    """Send ABC chunk to Redis stream"""
    console.print(f"[green]Sending to stream:[/green] {stream_name}")
    console.print(f"[yellow]ABC:[/yellow] {abc_string}")
    # TODO: Implement stream send functionality
    console.print("[red]Not implemented yet[/red]")

@stream.command('consume')
@click.option('--stream-name', default='abcweaver_abc', help='Redis stream name')
@click.option('--target', help='Target MusicXML file for processed ABC')
@click.option('--count', default=1, help='Number of messages to consume')
def stream_consume(stream_name, target, count):
    """Consume ABC chunks from Redis stream"""
    console.print(f"[green]Consuming from stream:[/green] {stream_name}")
    console.print(f"[blue]Target:[/blue] {target or 'stdout'}")
    # TODO: Implement stream consume functionality
    console.print("[red]Not implemented yet[/red]")

if __name__ == "__main__":
    abcweaver()