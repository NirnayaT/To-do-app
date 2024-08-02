from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    UniqueConstraint,
    ForeignKey,
    Text,
    Enum,
    Date,
)
from datetime import datetime
from sqlalchemy.orm import sessionmaker, relationship

from Database.enumeration import TaskStatus


# Establish a connection to the PostgreSQL database
engine = create_engine(
    "postgresql://postgres:admin123@localhost:5432/ProjectManagementApp"
)

connection = engine.connect()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    __table_args__ = (UniqueConstraint("email", name="unique_user_constraint"),)
    projects = relationship("Project", back_populates="owner")


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow)
    owner_id = Column(Integer(), ForeignKey("users.id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    owner = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project")


class Task(Base):  # main class table
    __tablename__ = "tasks"  # table name
    id = Column(Integer(), primary_key=True)
    task = Column(String(100), nullable=False)
    is_complete = Column(
        Enum(TaskStatus), nullable=False, default=TaskStatus.INCOMPLETE
    )
    created_on = Column(DateTime(), default=datetime.now)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    project = relationship("Project", back_populates="tasks")
    comments = relationship("Comment", back_populates="task")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    task = relationship("Task", back_populates="comments")
    user = relationship("User")


Base.metadata.create_all(engine)  # create engine

Session = sessionmaker(bind=engine)
session = Session()  # session starts
