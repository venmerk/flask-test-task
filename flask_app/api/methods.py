
from sqlalchemy import create_engine, update, insert
from flask_app.app_utils.app_config import config_interface


def update_or_create(model, id, json_args):
    """
    Update or create a record based on availability.
    :param model: sqla defined db model
    :param id: model item id (primary key)
    :param json_args: PUT json arguments
    """

    db_engine_url = config_interface.SQLALCHEMY_DB_ENGINE_URL
    db_engine = create_engine(db_engine_url)

    # get entity
    entity = model.query.filter_by(id=id).first()

    # update or create?
    if entity:
        upd = update(model)
        upd = upd.values(json_args)
        upd = upd.where(model.__table__.c.id == id)
    else:
        upd = insert(model)
        upd = upd.values(json_args)

    # process
    try:
        updated = db_engine.execute(upd)

    except Exception as e:
        print(f"Couldn't update database:\n{e._message}\n{e.args}")

    finally:
        db_engine.dispose()

    return model.query.filter_by(id=updated.inserted_primary_key[0]).first() or None
