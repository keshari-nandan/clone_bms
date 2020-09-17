from orator.migrations import Migration


class CreateStateTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('states') as table:
            table.increments('id')
            table.integer('country_id').unsigned()
            table.foreign('country_id').references('id').on('countries')
            table.string('name')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('states')
