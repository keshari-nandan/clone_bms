from orator.migrations import Migration


class CreateMovieBookingTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('movie_bookings') as table:
            table.increments('id')
            table.integer('show_id').unsigned()
            table.foreign('show_id').references('id').on('movie_shows')
            table.integer('user_id').unsigned()
            table.foreign('user_id').references('id').on('users')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('movie_bookings')
