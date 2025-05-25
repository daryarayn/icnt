from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import DatabaseConnectionPool

db, _ = DatabaseConnectionPool.get_connection()

class Teacher(db.Model):
	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column(nullable=False)
	description_teacher: Mapped[str] = mapped_column(Text, nullable=True)
	img: Mapped[str] = mapped_column(String(20), nullable=True)


class News(db.Model):
	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column(nullable=False)
	description_new: Mapped[str] = mapped_column(Text, nullable=True)
	img: Mapped[str] = mapped_column(String(20), nullable=True)