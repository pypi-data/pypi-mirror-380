try:
    from argparse import BooleanOptionalActionx
except ImportError:
    from argparse import Action
    class BooleanOptionalAction(Action):
        def __init__(self,
                     option_strings,
                     dest,
                     default=None,
                     type=None,
                     choices=None,
                     required=False,
                     help=None,
                     metavar=None):

            _option_strings = []
            for option_string in option_strings:
                _option_strings.append(option_string)

                if option_string.startswith('--'):
                    option_string = '--no-' + option_string[2:]
                    _option_strings.append(option_string)

            super().__init__(
                option_strings=_option_strings,
                dest=dest,
                nargs=0,
                default=default,
                type=type,
                choices=choices,
                required=required,
                help=help,
                metavar=metavar)


        def __call__(self, parser, namespace, values, option_string=None):
            if option_string in self.option_strings:
                setattr(namespace, self.dest, not option_string.startswith('--no-'))

        def format_usage(self):
            return ' | '.join(self.option_strings)

class EnumAction(Action):
    def __init__(self,
                 option_strings,
                 dest,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None):

        if type is None:
            type = default.__class__
        else:
            if default is not None:
                assert isinstance(default.__class__, type)

        self.enum_type = type

        metavar = '{' + ','.join([ _.name for _ in type ]) + '}',

        super().__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=1,
            default=default,
            type=str,
            choices=choices,
            required=required,
            help=help,
            metavar=metavar)

    def converter(self, value):
        value = value.lower()
        for e in self.enum_type:
            if value == e.name.lower():
                return e

        s = f"invalid choice {value} for e"
        raise ValueError(s)

    def __call__(self, parser, namespace, values, option_string=None):
        assert len(values) == 1
        e = self.converter(values[0])
        setattr(namespace, self.dest, e)

class EnumOrIntAction(EnumAction):
    def converter(self, value):
        try:
            return self.enum_type(int(value))
        except ValueError:
            return super().converter(value)
