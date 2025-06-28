from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Resource(Base):
    __tablename__ = "resources"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    file_path = Column(String)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    
    organization = relationship("Organization", back_populates="resources")  # Add this line