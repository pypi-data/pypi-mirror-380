# -*- coding: latin -*-

class TypeTheme:
    light = 'light'
    dark = 'dark'

    @classmethod
    def list(cls):
        return [cls.light, cls.dark]

class Global:
    theme : TypeTheme = TypeTheme.light
    app_color = '#4c94f4'






