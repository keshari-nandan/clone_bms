from orator.seeds import Seeder


class CityTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        cities = ['Delhi', 'Bangalore', 'Gurgaon', 'Hyderabad']
        for city in cities:
            self.db.table('cities').insert({
                'name': city
            })

