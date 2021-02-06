import pyqrcode
import typer

app = typer.Typer(add_completion=False)

OUTPUT_OPTIONS = typer.Option("qr-code.svg", "-o", "--output", help="path to output")


@app.command(help="Generate a QR code that points to a URL.")
def generate_qr(url: str, output: str = OUTPUT_OPTIONS):
    img = pyqrcode.create(url)
    img.svg(output, scale=8)
