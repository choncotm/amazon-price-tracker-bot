from datetime import datetime

from sqlalchemy import BigInteger, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    chat_id = Column(BigInteger, nullable=False)
    language = Column(String(8), nullable=False, default="fr")
    created_at = Column(DateTime, default=datetime.utcnow)

    tracks = relationship("Track", back_populates="user", cascade="all, delete-orphan")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    url = Column(Text, nullable=False)
    title = Column(Text)
    image_url = Column(Text)
    last_price = Column(Float)
    currency = Column(String(8), default="EUR")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="tracks")
    history = relationship("PriceHistory", back_populates="track", cascade="all, delete-orphan")


class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True)
    track_id = Column(Integer, ForeignKey("tracks.id"), nullable=False)
    old_price = Column(Float, nullable=False)
    new_price = Column(Float, nullable=False)
    checked_at = Column(DateTime, default=datetime.utcnow)

    track = relationship("Track", back_populates="history")


class FeatureUsage(Base):
    __tablename__ = "feature_usage"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    feature = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
