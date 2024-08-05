class MyAppRouter:
    def db_for_read(self, model, **hints):
        if model.__name__ == 'Student':
            return 'default'
        elif model.__name__ == 'Employee':
            return 'secondary'
        return 'default'

    def db_for_write(self, model, **hints):
        if model.__name__ == 'Student':
            return 'default'
        elif model.__name__ == 'Employee':
            return 'secondary'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name in ['student', 'employee'] and obj2._meta.model_name in ['student', 'employee']:
            return obj1._state.db == obj2._state.db
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app':  # Replace with your app name
            if model_name in ['student']:
                return db == 'default'
            elif model_name in ['employee']:
                return db == 'secondary'
        return db == 'default'