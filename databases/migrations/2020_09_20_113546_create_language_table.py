from orator.migrations import Migration


class CreateLanguageTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('languages') as table:
            table.increments('id')
            table.string('name')
            table.integer('movie_id').unsigned()
            table.foreign('movie_id').references('id').on('movies')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('languages')
