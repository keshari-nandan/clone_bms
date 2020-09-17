from orator.migrations import Migration


class CreateCountryTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('countries') as table:
            table.increments('id')
            table.string('name')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('countries')
