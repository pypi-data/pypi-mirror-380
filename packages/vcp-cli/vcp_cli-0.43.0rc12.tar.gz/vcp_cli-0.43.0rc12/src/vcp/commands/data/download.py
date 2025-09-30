from urllib.parse import urlparse

import click
from rich.console import Console

from vcp.commands.data.search import search_command
from vcp.datasets.api import DatasetSizeModel, LocationModel, get_dataset_api
from vcp.datasets.download import S3Credentials, download_locations
from vcp.utils.size import (
    calculate_total_dataset_size,
    format_size_bytes,
    get_file_count_from_dataset,
)
from vcp.utils.token import TokenManager

console = Console()

TOKEN_MANAGER = TokenManager()

EPILOG = f"""
{click.style("Examples:", fg="cyan", bold=True)} \n
- Download a {click.style("SINGLE", bold=True)} dataset by its exact ID\n
\t {click.style("vcp data download $DATASET_ID", fg="green")} \n
- Download {click.style("MULTIPLE", bold=True)} datasets matching a search term\n
\t {click.style("vcp data download --term $TERM", fg="green")} \n
\t ... equivalent to {click.style("vcp data search $TERM --download", fg="green")} \n
"""


def has_s3_locations(locations):
    """Check if any location contains S3 URLs."""
    for loc in locations:
        if isinstance(loc, LocationModel):
            if loc.scheme == "s3":
                return True
        elif isinstance(loc, DatasetSizeModel):
            if urlparse(loc.url).scheme == "s3":
                return True
        else:
            # Handle string URLs
            if urlparse(str(loc)).scheme == "s3":
                return True
    return False


@click.command("download", epilog=EPILOG)
@click.argument("dataset_id", nargs=-1)
@click.option(
    "--term", "-t", default=None, help="query term to download multiple datasets"
)
@click.option(
    "-o",
    "--outdir",
    type=click.Path(file_okay=False, dir_okay=True, writable=True, path_type=str),
    default=".",
    help="Directory to write the files.",
)
@click.option(
    "--exact",
    "-e",
    default=False,
    help="Use exact match when passing --term",
    is_flag=True,
)
@click.pass_context
def download_command(ctx, dataset_id: str, term: str, outdir: str, exact: bool):
    """
    Download a specific dataset by id. If you do not know the id, first use the search command to find the id.
    """
    # TODO: this should be able to download multiple datasets
    if term is not None:
        ctx.invoke(search_command, term=term, download=True, exact=exact)

    # session management
    tokens = TOKEN_MANAGER.load_tokens()
    if tokens is None:
        console.print("[red]Tokens not present: Login required[/red]")
        return None

    # call data api
    try:
        data = get_dataset_api(tokens.id_token, dataset_id, download=True)

        if getattr(data, "credentials", None) is None and has_s3_locations(
            data.locations
        ):
            console.print(
                f"[red]Error: Failed to get S3 credentials to download dataset {dataset_id}[/red]"
            )
            return None
        else:
            # Calculate and display size information
            total_size = calculate_total_dataset_size(data)
            file_count = get_file_count_from_dataset(data)

            if total_size > 0:
                size_display = format_size_bytes(total_size)
                if file_count > 0:
                    console.print(
                        f"Total download size: {size_display} ({file_count} files)"
                    )
                else:
                    console.print(f"Total download size: {size_display}")
            else:
                if file_count > 0:
                    console.print(
                        f"Dataset contains {file_count} files (size information not available)"
                    )
                else:
                    console.print("Download size information not available")

            # Ask for confirmation
            if not click.confirm("Continue with download?", default=True):
                console.print("Download cancelled.")
                return None

            # Only create S3Credentials if they exist, otherwise pass None
            credentials = (
                S3Credentials(**data.credentials) if data.credentials else None
            )
            download_locations(data.locations, credentials, outdir)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise e
        return None


@click.command("credentials")
@click.argument("dataset_id")
def generate_credentials_command(dataset_id: str):
    """
    Get the credentials for a specific dataset by id. If you do not know the id, first use the search command to find the id.
    """
    # TODO: this should be able to download multiple datasets

    # session management
    tokens = TOKEN_MANAGER.load_tokens()
    if tokens is None:
        console.print("[red]Tokens not present: Login required[/red]")
        return None

    # call data api
    try:
        data = get_dataset_api(tokens.id_token, dataset_id, download=True)

        if getattr(data, "error", None) or getattr(data, "credentials", None) is None:
            console.print(f"[red]Error: {data['error']}[/red]")
            return None
        else:
            credentials = S3Credentials(**data.credentials)
            print(credentials.model_dump())
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        return None
