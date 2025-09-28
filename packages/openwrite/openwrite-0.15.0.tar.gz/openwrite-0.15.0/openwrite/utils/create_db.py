from .db import init_engine
from .models import User, Blog, Post, View, Settings, Home, Like, Settings, Page, Tag, PostTag
from .migrations import run_migrations, ensure_database_compatibility
from openwrite.db.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import StaticPool
import os
import json
import logging

logger = logging.getLogger(__name__)

def init_db(dbtype, dbpath):
    """
    Initialize database with proper migrations.
    This function now uses the migration system for better schema management.
    """
    engine = init_engine(dbtype, dbpath)
    
    # Ensure database compatibility
    ensure_database_compatibility(engine)
    
    # Run migrations to ensure all tables, columns, and indexes exist
    run_migrations(engine)
    
    logger.info("Database initialization completed.")
    
