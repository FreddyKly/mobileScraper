from typing import Optional

class UrlBuilder:
    def __init__(self,
                 brand: Optional[str] = None,
                 maxPrice: Optional[str] = None,
                 category: Optional[str] = None,
                 firstRegistration: Optional[str] = None,
                 kilometer: Optional[str] = None,
                 minPower: Optional[str] = None):
        brands = {'Mitsubishi': '17700', 'Alfa Romeo': '900', 'Audi': '1900', 'BMW': '3500', 'Ford': '9000', 'Honda': '11000',
                  'Hyundai': '11600', 'Mazda': '16800', 'Nissan': '18700', 'Toyota': '24100'}
        self.brand = brands[brand]
        self.maxPrice = maxPrice
        self.category = category
        self.firstRegistration = firstRegistration
        self.kilometer = kilometer
        self.minPower = minPower

    def builder(self):
        url = f'https://suchen.mobile.de/fahrzeuge/search.html?categories={self.category}&isSearchRequest=true&\
makeModelVariant1.makeId={self.brand}&maxPowerAsArray=PS&maxPrice={self.maxPrice}&minPowerAsArray={self.minPower}&minPowerAsArray=PS'
        print(url)
        return url
