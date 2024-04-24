from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for database models
Base = declarative_base()

class HighScore(Base):
    """Database model for high scores."""
    __tablename__ = 'high_scores'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    game = Column(String, nullable=False)
    score = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<HighScore(name='{self.name}', game='{self.game}', score={self.score})>"

# Database connection setup
DB_URL = 'sqlite:///highscore.db'
engine = create_engine(DB_URL)
Base.metadata.create_all(engine)  # Create the database tables

Session = sessionmaker(bind=engine)
session = Session()
