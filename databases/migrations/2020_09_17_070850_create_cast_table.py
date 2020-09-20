from orator.migrations import Migration


class CreateCastTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('casts') as table:
            table.increments('id')
            table.string('name')
            table.string('role')
            table.string('role_name')
            table.integer('movie_id').unsigned()
            table.foreign('movie_id').references('id').on('movies')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('casts')
