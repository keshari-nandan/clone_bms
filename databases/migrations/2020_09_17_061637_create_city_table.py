from orator.migrations import Migration


class CreateCityTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cities') as table:
            table.increments('id')
            table.string('name')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cities')
