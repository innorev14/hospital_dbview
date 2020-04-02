import random


class MasterSlaveRouter:

    def db_for_read(self, model, **hints):
        return random.choice(['read1', 'read2'])

    def db_for_write(self, model, **hints):
        return 'master'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('master', 'read1', 'read2')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True