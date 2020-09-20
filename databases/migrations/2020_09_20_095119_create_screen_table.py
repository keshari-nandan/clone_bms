from orator.migrations import Migration


class CreateScreenTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('screens') as table:
            table.increments('id')
            table.string('name')
            table.integer('seats')
            table.integer('theater_id').unsigned()
            table.foreign('theater_id').references('id').on('theaters')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('screens')
