import typer

from esgvoc.cli.clean import app as clean_app
from esgvoc.cli.config import app as config_app
from esgvoc.cli.drs import app as drs_app
from esgvoc.cli.find import app as find_app
from esgvoc.cli.get import app as get_app
from esgvoc.cli.install import app as install_app
from esgvoc.cli.offline import app as offline_app
from esgvoc.cli.status import app as status_app
from esgvoc.cli.test_cv import app as test_cv_app
from esgvoc.cli.valid import app as valid_app

app = typer.Typer()

# Register the subcommands
app.add_typer(get_app)
app.add_typer(status_app)
app.add_typer(valid_app)
app.add_typer(install_app)
app.add_typer(drs_app)
app.add_typer(config_app, name="config")
app.add_typer(offline_app, name="offline")
app.add_typer(clean_app, name="clean")
app.add_typer(test_cv_app, name="test")
app.add_typer(find_app)


def main():
    app()


if __name__ == "__main__":
    main()
