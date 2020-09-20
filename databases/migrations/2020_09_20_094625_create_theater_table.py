from orator.migrations import Migration


class CreateTheaterTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('theaters') as table:
            table.increments('id')
            table.string('name')
            table.integer('city_id').unsigned()
            table.foreign('city_id').references('id').on('cities')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('theaters')
