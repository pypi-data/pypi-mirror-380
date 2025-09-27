import click
import uvicorn


@click.command()
@click.option("--host", default="127.0.0.1", help="Bind to IP address")
@click.option("--port", default=8080, help="Bind to port")
@click.option("--workers", default=1, help="Number of worker processes")
def main(host, port, workers):
    """Starts the pp.server using uvicorn."""
    uvicorn.run(
        "pp.server.server:app",
        host=host,
        port=port,
        workers=workers,
        reload=True,
    )


if __name__ == "__main__":
    main()
