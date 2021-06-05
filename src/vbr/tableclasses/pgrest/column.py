__all__ = ['Column', 'ForeignKey']


class PgRestColumn(object):
    DATA_TYPE = None
    PYTHON_TYPE = None

    @classmethod
    def properties(cls):
        return {'data_type': cls.DATA_TYPE}

    @classmethod
    def validate(cls, value):

        if value is None:
            return True

        if cls.PYTHON_TYPE is None:
            return True
        else:
            return isinstance(value, cls.PYTHON_TYPE)


class ForeignKey(object):
    def __init__(self, source, on_delete='cascade', on_update='cascade'):
        self.FK = True
        (self.reference_table, self.reference_column) = source.split('.')
        self.on_delete = on_delete
        self.on_update = on_update

    def properties(self):
        return {
            'FK': self.FK,
            'reference_table': self.reference_table,
            'reference_column': self.reference_column,
            'on_delete': self.on_delete
        }


class Column(object):
    """PgREST Column
    """
    def __init__(
            self,
    #   cname,
            ctype,
            *args,
            primary_key=False,
            unique=False,
            nullable=False,
            default=None,
            comment=None,
            **kwargs):

        # self.cname = cname
        self.ctype = ctype
        if self.ctype.validate(default):
            self.default = default
        else:
            raise ValueError('Invalid type for default')

        self.primary_key = primary_key
        self.unique = unique
        self.nullable = nullable
        self.comment = comment
        self.relations = []

        self.fk = None
        for a in args:
            if isinstance(a, ForeignKey):
                self.fk = a

    def property(self):
        all_props = self.ctype.properties()
        if self.default is not None:
            all_props['default'] = self.default
        if self.primary_key:
            all_props['primary_key'] = True
        if self.unique:
            all_props['unique'] = True
        all_props['null'] = self.nullable
        if self.comment is not None:
            all_props['comment'] = self.comment

        if self.fk is not None:
            fk_props = self.fk.properties()
            self.relations.append(fk_props['reference_table'])
            all_props = {**all_props, **fk_props}

        return all_props
