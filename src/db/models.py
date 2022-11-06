from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.types import JSON
from src.db.database import Base


# Project Table
class Project(Base):
    __tablename__ = "projects"

    project_id = Column(
        String(255),
        primary_key=True,
        comment="primary key",
    )
    project_name = Column(
        String(255),
        nullable=False,
        unique=True,
        comment="Project Name",
    )
    description = Column(
        Text,
        nullable=True,
        comment="Explanation of Project",
    )
    create_datetime = Column(
        DateTime(timezone=True),
        server_default=current_timestamp(),
        nullable=False,
    )


class Model(Base):
    __tablename__ = "models"

    model_id = Column(
        String(255),
        primary_key=True,
        comment="primary key",
    )
    project_id = Column(
        String(255),
        ForeignKey("projects.project_id"),
        nullable=False,
        comment="foreign key",
    )
    model_name = Column(
        String(255),
        nullable=False,
        comment="model name",
    )
    description = Column(
        Text,
        nullable=True,
        comment="description",
    )
    created_datetime = Column(
        DateTime(timezone=True),
        server_default=current_timestamp(),
        nullable=False,
    )


class Experiment(Base):
    __tablename__ = "experiments"

    experiment_id = Column(
        String(255),
        primary_key=True,
        comment="primary key",
    )
    model_id = Column(
        String(255),
        ForeignKey("models.model_id"),
        nullable=False,
        comment="foreign key",
    )
    model_version_id = Column(
        String(255),
        nullable=False,
        comment="Version id of experiments",
    )
    parameters = Column(
        JSON,
        nullable=True,
        comment="learning parameters",
    )
    training_dataset = Column(
        Text,
        nullable=True,
        comment="training data",
    )
    validation_dataset = Column(
        Text,
        nullable=True,
        comment="validation data",
    )
    test_dataset = Column(
        Text,
        nullable=True,
        comment="test data",
    )
    evaluations = Column(
        JSON,
        nullable=True,
        comment="evaludation results",
    )
    artifact_file_paths = Column(
        JSON,
        nullable=True,
        comment="model's file path",
    )
    created_datetime = Column(
        DateTime(timezone=True),
        server_default=current_timestamp(),
        nullable=False,
    )
