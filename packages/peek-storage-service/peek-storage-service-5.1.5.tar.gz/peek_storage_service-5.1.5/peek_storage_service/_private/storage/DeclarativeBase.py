""" 
 * orm.Base.py
 *
 *  Copyright Synerty HQ Pty Ltd 2013
 *
 *  This software is proprietary, you are not free to copy
 *  or redistribute this code in any format.
 *
 *  All rights to this software are reserved by 
 *  Synerty HQ Pty Ltd
 *
"""

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.schema import MetaData

metadata = MetaData(schema="peek_storage_service")
DeclarativeBase = declarative_base(metadata=metadata)
