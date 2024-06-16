import cli
import typer

app = typer.Typer()

app.command()(cli.configure)
app.command()(cli.test)
app.command()(cli.query)
app.command()(cli.show_table)
app.command()(cli.show_tree)

if __name__ == "__main__":
    app()