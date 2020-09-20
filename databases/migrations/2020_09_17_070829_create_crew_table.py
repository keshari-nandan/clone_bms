from orator.migrations import Migration


class CreateCrewTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('crews') as table:
            table.increments('id')
            table.integer('movie_id').unsigned()
            table.foreign('movie_id').references('id').on('movies')
            table.string('name')
            table.string('role')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('crews')
