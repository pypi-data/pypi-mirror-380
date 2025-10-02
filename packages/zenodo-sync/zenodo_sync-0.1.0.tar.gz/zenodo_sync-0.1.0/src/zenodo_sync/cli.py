"""Command-line interface for zenodo-sync."""

import click
from pathlib import Path
from typing import Optional

from .core import ZenodoSync
from .exceptions import ZenodoSyncError


@click.group()
@click.version_option()
@click.option(
    "--token",
    envvar="ZENODO_TOKEN",
    help="Zenodo API token (or set ZENODO_TOKEN environment variable)",
)
@click.option(
    "--sandbox/--production",
    default=True,
    help="Use Zenodo sandbox (default) or production",
)
@click.pass_context
def cli(ctx: click.Context, token: Optional[str], sandbox: bool) -> None:
    """zenodo-sync: Synchronize research data with Zenodo."""
    ctx.ensure_object(dict)
    ctx.obj["token"] = token
    ctx.obj["sandbox"] = sandbox


@cli.command()
@click.argument("file_path", type=click.Path(exists=True, path_type=Path))
@click.option("--deposition-id", help="Existing Zenodo deposition ID")
@click.pass_context
def upload(
    ctx: click.Context, file_path: Path, deposition_id: Optional[str]
) -> None:
    """Upload a file to Zenodo."""
    try:
        sync = ZenodoSync(
            token=ctx.obj["token"], 
            sandbox=ctx.obj["sandbox"]
        )
        result = sync.upload_file(file_path, deposition_id)
        click.echo(f"Upload successful: {result}")
    except ZenodoSyncError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


@cli.command()
@click.argument("record_id")
@click.argument("output_dir", type=click.Path(path_type=Path))
@click.pass_context
def download(ctx: click.Context, record_id: str, output_dir: Path) -> None:
    """Download files from a Zenodo record."""
    try:
        sync = ZenodoSync(
            token=ctx.obj["token"], 
            sandbox=ctx.obj["sandbox"]
        )
        files = sync.download_file(record_id, output_dir)
        click.echo(f"Downloaded {len(files)} files to {output_dir}")
    except ZenodoSyncError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


@cli.command()
@click.argument("local_dir", type=click.Path(exists=True, path_type=Path))
@click.option("--record-id", help="Existing Zenodo record ID")
@click.option(
    "--exclude",
    multiple=True,
    help="Glob patterns for files to exclude (can be used multiple times)",
)
@click.pass_context
def sync(
    ctx: click.Context,
    local_dir: Path,
    record_id: Optional[str],
    exclude: tuple,
) -> None:
    """Synchronize a local directory with Zenodo."""
    try:
        sync_obj = ZenodoSync(
            token=ctx.obj["token"], 
            sandbox=ctx.obj["sandbox"]
        )
        result = sync_obj.sync_directory(
            local_dir, record_id, list(exclude) if exclude else None
        )
        click.echo(f"Sync completed: {result}")
    except ZenodoSyncError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()


def main() -> None:
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()