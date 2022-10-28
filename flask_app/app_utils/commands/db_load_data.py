"""
Update database with custom loads.
Currently supports 'csv' only.
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
"""

import click

from flask import Blueprint
from sqlalchemy import create_engine
from pandas import read_csv

from flask_app.app_utils.app_config import config_interface

cli_db_import_bp = Blueprint('import_db', __name__, cli_group='import')
cli_db_import_bp.cli.short_help = 'Import specified.'


@cli_db_import_bp.cli.command('csv')
@click.argument('csv_path')
@click.argument('db_table')
def load_data(csv_path: str, db_table: str):
    """
    Unpack csv and load data into
    specified db table in 'append' mode.

    :param csv_path: full path to file including .extension.
    :param db_table: name of the db table
    :return: None
    """

    # import csv
    try:
        df = read_csv(csv_path)
        print('CSV imported successfully...')

    except Exception as e:
        print(f"Error! Can't import file:\n{e.args}\n{e._message}")

    # convert column titles to lowercase for appropriate feature recognition
    df.columns = df.columns.str.lower()

    # set up db manipulation engine
    db_engine_url = config_interface.SQLALCHEMY_DB_ENGINE_URL
    db_engine = create_engine(db_engine_url)

    # load data into db
    try:
        df.to_sql(db_table, db_engine, if_exists='append', index=False)
        print('Data loaded into db successfully...')

    except Exception as e:
        print(f"Couldn't update database:\n{e._message}\n{e.args}")

    finally:
        db_engine.dispose()

