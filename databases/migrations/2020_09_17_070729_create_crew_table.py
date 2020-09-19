from orator.migrations import Migration


class CreateCrewTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('Crew') as table:
            table.increments('id')
            table.string('name')
            table.string('role')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('Crew')
