from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(120))
    eye_color: Mapped[str] = mapped_column()
    birth_year: Mapped[str] = mapped_column(String(10))
    character_favorites: Mapped["Favorites"] = relationship(back_populates = "favorites_characters")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
        }
    
class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(120))
    terrain: Mapped[str] = mapped_column()
    population: Mapped[str] = mapped_column()
    planet_favorites: Mapped["Favorites"] = relationship(back_populates = "favorites_planets")

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "terrain": self.terrain,
            "population": self.population, 
        }
    
class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_id: Mapped[int] = mapped_column(ForeignKey("characters.id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
    favorites_characters: Mapped[list["Characters"]] = relationship(back_populates = "character_favorites")
    favorites_planets: Mapped[list["Planets"]] = relationship(back_populates = "planet_favorites")

    def serialize(self):
        return {
            "character_id": self.character_id,
            "planet_id": self.planet_id,
        }