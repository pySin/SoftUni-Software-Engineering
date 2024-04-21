from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands: list = []
        self.musicians: list = []
        self.concerts: list = []

    def create_musician(self, musician_type: str, name: str, age: int):
        valid_musicians = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

        if musician_type not in valid_musicians:
            raise ValueError("Invalid musician type!")

        if name == next((m.name for m in self.musicians if m.name == name), None):
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(valid_musicians[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name == next((b.name for b in self.bands if b.name == name), None):
            raise Exception(f"{name} band is already created!")

        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        place_taken = next((p for p in self.concerts if p.place == place), None)
        if place_taken:
            raise Exception(f"{place} is already registered for {genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        band = next((b for b in self.bands if b.name == band_name), None)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        musician = next((m for m in self.musicians if m.name == musician_name), None)
        band = next((b for b in self.bands if b.name == band_name), None)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        if musician not in band.mambers:
            raise f"{musician_name} isn't a member of {band_name}!"

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = next((b for b in self.bands if b.name == band_name), None)

        current_musician_types = [mt.__class__.__name__ for mt in band.members]
        for musician_type in ['Singer', 'Drummer', 'Guitarist']:
            if musician_type not in current_musician_types:
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = next((c for c in self.concerts if c.place == concert_place), None)

        concert_genres = {"Rock": {
                                  "Drummer": ["play the drums with drumsticks"],
                                  "Singer": ["sing high pitch notes"],
                                  "Guitarist": ["play rock"]
                                  # "is_concert_ok": False
                              },
                          "Metal": {
                                  "Drummer": ["play the drums with drumsticks"],
                                  "Singer": ["sing low pitch notes"],
                                  "Guitarist": ["play metal"]
                                  # "is_concert_ok": False
                              },
                          "Jazz": {
                                  "Drummer": ["play the drums with drum brushes"],
                                  "Singer": ["sing high pitch notes", "sing low pitch notes"],
                                  "Guitarist": ["play jazz"]
                                  # "is_concert_ok": False
                              }
                          }

        cleared_musicians = 0
        for musician in concert_genres[concert.genre]:
            # print(musician)
            for band_musician in band.members:
                if band_musician.__class__.__name__ == musician:
                    # print(set(concert_genres[concert.genre][musician]))
                    # print(set(band_musician.skills))
                    if set(band_musician.skills) >= set(concert_genres[concert.genre][musician]):
                        # print("SUBSET")
                        cleared_musicians += 1
        if cleared_musicians == 3:
            profit = (concert.audience * concert.ticket_price) - concert.expenses
            return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
        else:
            return f"The {band_name} band is not ready to play at the concert!"


