from rich.console import Console
from rich.logging import RichHandler
from random import randrange, seed
import logging
from novara.config import config

# -----------------------------------------------------------------

logging.basicConfig(
    level=config.logging_level if config.is_initialized else 'NOTSET',
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger("rich")
console = Console()

# -----------------------------------------------------------------


def print(*args, **kwargs):
    console.print(*args, **kwargs)


# -----------------------------------------------------------------


def color_value(value: str):
    seed(value.lower())
    r, g, b = [str(hex(randrange(25, 255))[2:]) for _ in range(3)]
    value_colored = f"[bold #{r}{g}{b}]{value}[/]"

    return value_colored