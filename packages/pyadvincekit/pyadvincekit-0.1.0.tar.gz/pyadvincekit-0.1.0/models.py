#!/usr/bin/env python3
"""
Generated ORM models for Generated Database
Generated at: 2025-09-29T17:31:48.919705
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, Float, JSON, Date, Time, Numeric, BigInteger, SmallInteger, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped
from pyadvincekit.models.base import BaseModel
from datetime import datetime, date, time
from typing import Optional

Base = declarative_base()
