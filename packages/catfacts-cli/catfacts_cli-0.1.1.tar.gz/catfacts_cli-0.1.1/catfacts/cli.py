import requests
import sys
import argparse
from rich.console import Console
from catfacts import __version__

console = Console()

API_URL = "https://catfact.ninja/fact"


def get_cat_fact():
    """Fetch and print a single cat fact."""
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        fact = response.json()
        console.print(f"🐱 [bold cyan]Cat Fact:[/bold cyan] {fact['fact']}")
    except requests.RequestException as e:
        console.print(f"[bold red]❌ Error:[/bold red] Could not fetch cat fact. ({e})")


def main():
    parser = argparse.ArgumentParser(
        prog="catfacts",
        description="🐱 A simple CLI tool to get random cat facts."
    )
    parser.add_argument(
        "--count", "-c",
        type=int,
        default=1,
        help="Number of cat facts to fetch"
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version and exit"
    )

    args = parser.parse_args()

    # Show version
    if args.version:
        console.print(f"🐾 catfacts-cli version [bold green]{__version__}[/bold green]")
        sys.exit(0)

    # Fetch facts
    for _ in range(args.count):
        get_cat_fact()


if __name__ == "__main__":
    main()
