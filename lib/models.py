from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    wrestlers = relationship('Wrestler', back_populates='team')

class Wrestler(Base):
    __tablename__ = 'wrestlers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    weight_class = Column(String, nullable=False)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Team', back_populates='wrestlers')
