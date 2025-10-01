class CityLocation:

    def __init__(self, city: str, state_province: str = None, country: str = None):
        self._city = city
        self._state_province = state_province
        self._country = country

    @property
    def city(self) -> str:
        return self._city
    
    @property
    def state_province(self) -> str:
        return self._state_province
    
    @property
    def country(self) -> str:
        return self._country
    
    def __repr__(self):
        return f"CityLocation(city={self.city}, state_province={self.state_province}, country={self.country})"

    @classmethod
    def from_string(cls, data: str) -> "CityLocation":
        #'Nova Friburgo, Rio de Janeiro, Brazil'
        parts = data.split(", ")
        if len(parts) == 3:
            city, state_province, country = parts
            return cls(city=city, state_province=state_province, country=country)
        if len(parts) == 2:
            city, state_province = parts
            return cls(city=city, state_province=state_province)
        elif len(parts) == 1:
            city = parts[0]
            return cls(city=city)
        else:
            raise ValueError("Invalid city location string format")