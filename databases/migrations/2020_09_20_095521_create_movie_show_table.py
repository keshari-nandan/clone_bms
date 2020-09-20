from orator.migrations import Migration


class CreateMovieShowTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('movie_shows') as table:
            table.increments('id')
            table.integer('movie_id').unsigned()
            table.foreign('movie_id').references('id').on('movies')
            table.integer('screen_id').unsigned()
            table.foreign('screen_id').references('id').on('screens')
            table.time('show_time')
            table.date('show_date')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('movie_shows')
