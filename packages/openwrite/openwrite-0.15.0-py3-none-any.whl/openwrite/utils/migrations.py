from sqlalchemy import inspect, text, Column, Integer, String, Date, Text, DateTime, Index
from sqlalchemy.exc import OperationalError, ProgrammingError
import logging
from .models import Settings, Home, User, Blog, Post, View, Like, Page, Tag, PostTag
from openwrite.db.base import Base

logger = logging.getLogger(__name__)

def run_migrations(engine):
    logger.info("Starting database migrations...")
    
    try:
        inspector = inspect(engine)
        
        models = [Settings, Home, User, Blog, Post, View, Like, Page, Tag, PostTag]
        
        for model in models:
            table_name = model.__tablename__
            
            if not inspector.has_table(table_name):
                logger.info(f"Creating table: {table_name}")
                model.__table__.create(engine)
                continue
            
            existing_columns = {col['name'] for col in inspector.get_columns(table_name)}
            model_columns = {col.name for col in model.__table__.columns}
            
            missing_columns = model_columns - existing_columns
            
            for column_name in missing_columns:
                column = model.__table__.columns[column_name]
                add_column_to_table(engine, table_name, column)
            
            create_missing_indexes(engine, inspector, model, table_name)
        
        logger.info("Database migrations completed successfully.")
        
    except Exception as e:
        logger.error(f"Error during database migrations: {e}")
        raise


def add_column_to_table(engine, table_name, column):
    try:
        column_type = column.type.compile(engine.dialect)
        nullable = "NULL" if column.nullable else "NOT NULL"
        
        default_clause = ""
        if column.default is not None:
            if hasattr(column.default, 'arg'):
                if callable(column.default.arg):
                    default_clause = f" DEFAULT {column.default.arg.__name__}()"
                else:
                    default_clause = f" DEFAULT '{column.default.arg}'"
        
        alter_statement = f"ALTER TABLE {table_name} ADD COLUMN {column.name} {column_type} {nullable}{default_clause}"
        
        logger.info(f"Adding column {column.name} to table {table_name}")
        
        with engine.connect() as conn:
            conn.execute(text(alter_statement))
            conn.commit()
            
    except (OperationalError, ProgrammingError) as e:
        logger.error(f"Error adding column {column.name} to table {table_name}: {e}")
        pass


def create_missing_indexes(engine, inspector, model, table_name):
    try:
        existing_indexes = {idx['name'] for idx in inspector.get_indexes(table_name)}
        
        if hasattr(model, '__table_args__') and model.__table_args__:
            for arg in model.__table_args__:
                if isinstance(arg, Index):
                    index_name = arg.name
                    if index_name not in existing_indexes:
                        logger.info(f"Creating index {index_name} on table {table_name}")
                        try:
                            arg.create(engine)
                        except (OperationalError, ProgrammingError) as e:
                            logger.warning(f"Could not create index {index_name}: {e}")
                            pass
                            
    except Exception as e:
        logger.error(f"Error checking indexes for table {table_name}: {e}")
        pass


def ensure_database_compatibility(engine):
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            
        logger.info("Database connectivity verified.")
        
    except Exception as e:
        logger.error(f"Database compatibility check failed: {e}")
        raise


def get_migration_status(engine):
    try:
        inspector = inspect(engine)
        status = {
            'tables': {},
            'missing_tables': [],
            'missing_columns': {}
        }
        
        models = [Settings, Home, User, Blog, Post, View, Like, Page, Tag, PostTag]
        
        for model in models:
            table_name = model.__tablename__
            
            if not inspector.has_table(table_name):
                status['missing_tables'].append(table_name)
            else:
                existing_columns = {col['name'] for col in inspector.get_columns(table_name)}
                model_columns = {col.name for col in model.__table__.columns}
                missing_columns = model_columns - existing_columns
                
                status['tables'][table_name] = {
                    'exists': True,
                    'columns': len(existing_columns),
                    'missing_columns': list(missing_columns)
                }
                
                if missing_columns:
                    status['missing_columns'][table_name] = list(missing_columns)
        
        return status
        
    except Exception as e:
        logger.error(f"Error getting migration status: {e}")
        return {'error': str(e)}