# Every model represents a table in our DB
from .database import Base
from sqlalchemy.orm import Relationship
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, ForeignKey


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    # reference table name not class name
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    # User class - sqlalchemy will automatically figure out what we want somehow.
    # ok the somehow is as follows: sqlalchemy fetches the user based of the owner_id and fetches it for us.
    owner = Relationship("User")
    phone_number = Column(String, nullable=True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    # SQLAlchemy can not add new columns on the fly - gotta restart the table
    # Or use Alembic - Data migration Tool
    # phone_number = Column(String)


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)


class Follow(Base):
    __tablename__ = "follows"
    follower_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    followed_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
