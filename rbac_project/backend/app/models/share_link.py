from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class ShareLink(Base):
    __tablename__ = "share_links"
    
    id = Column(Integer, primary_key=True)
    token = Column(String, unique=True, index=True)
    resource_id = Column(Integer, ForeignKey("resources.id"))
    expires_at = Column(DateTime)
    permission = Column(String)  # 'view' or 'edit'
    created_by = Column(Integer, ForeignKey("users.id"))