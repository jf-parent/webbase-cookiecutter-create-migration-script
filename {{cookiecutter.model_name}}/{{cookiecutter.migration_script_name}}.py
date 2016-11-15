from server.model.migrationbase import MigrationBase


class Migration(MigrationBase):
    def update(self, session):
        self.add_field('<Modelname>', '<new_field_name>', '<default_value>')

    def roll_back(self, session):
        self.remove_field('<Modelname>', '<new_field_name>')
