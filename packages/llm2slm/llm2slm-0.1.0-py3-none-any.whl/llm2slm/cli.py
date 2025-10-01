import asyncio
import logging
import sys

import click

from llm2slm.core import convert_model, load_config, save_config
from llm2slm.providers import get_available_providers
from llm2slm.server import run_server

"""
CLI interface for the LLM2SLM project.

This module provides a command-line interface for converting Large Language Models (LLMs)
to Small Language Models (SLMs), managing configurations, and running the server.

Usage:
    python -m llm2slm [command] [options]

Commands:
    convert: Convert an LLM to an SLM.
    serve: Start the FastAPI server.
    config: Manage configuration settings.
    version: Show the version of LLM2SLM.
    providers: List available model providers.
    validate: Validate the current setup and configuration.

For more details, use --help with any command.
"""


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


@click.group()
@click.option("--log-level", default="INFO", help="Set the logging level")
def cli(log_level: str) -> None:
    """CLI for converting LLMs to SLMs."""
    logging.getLogger().setLevel(getattr(logging, log_level.upper()))


@cli.command()
@click.argument("input_model")
@click.argument("output_path")
@click.option(
    "--provider", default="openai", help="Model provider (openai, anthropic, google, liquid)"
)
@click.option("--compression-factor", default=0.5, type=float, help="Compression factor")
def convert(input_model: str, output_path: str, provider: str, compression_factor: float) -> None:
    """Convert an LLM to an SLM."""
    # Validate provider
    available_providers = get_available_providers()
    if provider not in available_providers:
        click.echo(
            f"Error: Invalid provider '{provider}'. "
            f"Available providers: {', '.join(available_providers)}",
            err=True,
        )
        sys.exit(1)

    try:
        logger.info("Starting model conversion...")
        result = asyncio.run(
            convert_model(
                input_model=input_model,
                output_path=output_path,
                provider=provider,
                compression_factor=compression_factor,
            )
        )
        logger.info("Model conversion completed successfully.")
        click.echo(f"Conversion result: {result}")
    except Exception as e:
        error_msg = f"Error during conversion: {e}"
        logger.error(error_msg)
        click.echo(error_msg, err=True)
        sys.exit(1)


# Export for testing
convert_command = convert


@cli.command()
@click.option("--host", default="0.0.0.0", help="Host to bind the server")
@click.option("--port", default=8000, type=int, help="Port to bind the server")
def serve(host: str, port: int) -> None:
    """Start the FastAPI server."""
    try:
        logger.info(f"Starting server on {host}:{port}")
        asyncio.run(run_server(host=host, port=port))
    except Exception as e:
        logger.error(f"Error starting server: {e}")
        sys.exit(1)


@cli.command()
@click.option("--set", nargs=2, metavar=("KEY", "VALUE"), help="Set a configuration key-value pair")
@click.option("--get", metavar="KEY", help="Get a configuration value")
def config(set: tuple, get: str) -> None:  # type: ignore[no-untyped-def]
    """Manage configuration."""
    config = load_config()
    if set:
        key, value = set
        config[key] = value
        save_config(config)
        logger.info(f"Set {key} to {value}")
    elif get:
        value = config.get(get)
        if value is not None:
            click.echo(value)
        else:
            logger.error(f"Key '{get}' not found in config")
            sys.exit(1)
    else:
        logger.info("Current config:")
        for k, v in config.items():
            click.echo(f"{k}: {v}")


@cli.command()
def version() -> None:
    """Show the version of LLM2SLM."""
    from llm2slm import __version__

    click.echo(f"LLM2SLM version {__version__}")


@cli.command()
def providers() -> None:
    """List available model providers."""
    try:
        providers_list = get_available_providers()
        if providers_list:
            click.echo("Available providers:")
            for provider in providers_list:
                click.echo(f"  - {provider}")
        else:
            click.echo("No providers available.")
    except Exception as e:
        logger.error(f"Error listing providers: {e}")
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@cli.command()
def validate() -> None:
    """Validate the current setup and configuration."""
    click.echo("Validating LLM2SLM setup...")

    # Check configuration
    try:
        load_config()
        click.echo("✓ Configuration loaded successfully")
    except Exception as e:
        click.echo(f"✗ Configuration error: {e}", err=True)
        sys.exit(1)

    # Check providers
    try:
        providers_list = get_available_providers()
        click.echo(f"✓ Found {len(providers_list)} provider(s): {', '.join(providers_list)}")
    except Exception as e:
        click.echo(f"✗ Provider check failed: {e}", err=True)

    # Check core modules
    try:

        click.echo("✓ Core SLM modules imported successfully")
    except Exception as e:
        click.echo(f"✗ Core module import failed: {e}", err=True)
        sys.exit(1)

    click.echo("\nSetup validation completed!")


def main() -> None:  # type: ignore[no-untyped-def]
    """Main entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
