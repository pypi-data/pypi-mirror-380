import typer

app = typer.Typer(help="Mi app de ejemplo con Typer")

@app.command()
def saludar(nombre: str):
    """
    Saluda a alguien por su nombre.
    """
    typer.echo(f"¡Hola, {nombre}!")

@app.command()
def saludar_rep(nombre: str, repetir: int = 1):
    """
    Saluda varias veces a alguien.
    """
    for i in range(repetir):
        typer.echo(f"¡Hola ({i+1}) {nombre}!")

if __name__ == "__main__":
    app()
