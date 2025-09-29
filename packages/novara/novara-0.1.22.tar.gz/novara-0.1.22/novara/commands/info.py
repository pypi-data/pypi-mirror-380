import rich_click as click
from novara.constants import __version__
from novara.utils import logger
from novara.config import config
from novara.request import request
import requests
import time


from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

def get_latest_version():
    url = f"https://pypi.org/pypi/novara/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        latest_version = data['info']['version']
        return latest_version
    else:
        raise Exception(f"Failed to fetch package information: {response.status_code}")

@click.command()
def info():
    logger.debug('fetching version of the cli from pypi...')
    latest_version = get_latest_version()

    logger.debug("check connectivity to the backend...")
    try:
        r = request.get("api/up")
        is_up = r.status_code == 200
    except Exception:
        is_up = False

    if is_up:
        logger.debug("time response of the backend...")
        start_time = time.time()
        r = request.get("api/up")
        time_elapsed = time.time() - start_time
    else:
        time_elapsed = None

    console = Console()

    # Header
    console.rule("[bold cyan]Novara CLI Info[/bold cyan]", style="cyan")

    # Version Info
    version_table = Table(show_header=False, box=None)
    version_table.add_row("Novara CLI Version:", f"[green]{__version__}[/green]")
    version_table.add_row("Latest Available:", f"[green]{latest_version}[/green]")
    console.print(version_table)

    if __version__ != latest_version:
        console.print(
            Panel.fit(
                Text(
                    "You are using an older version of the CLI.\n"
                    "Consider upgrading:\n"
                    "    pip install --upgrade novara",
                    style="yellow bold"
                ),
                border_style="yellow"
            )
        )

    # Backend Info
    backend_table = Table(show_header=False, box=None)
    backend_table.add_row("Backend Server:", f"[blue]{config.server_url}[/blue]")
    backend_table.add_row("Author:", f"{config.author}")
    if is_up and time_elapsed is not None:
        backend_table.add_row("Backend Status:", f"[green]Reachable ({time_elapsed:.2f}s response)[/green]")
    else:
        backend_table.add_row("Backend Status:", "[red]Unreachable[/red]")
    console.print(backend_table)

    console.rule(style="cyan")
