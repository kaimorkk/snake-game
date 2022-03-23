class Tageless:
    def __init__(self,_first_name,_middle_name,_last_name):
        self._first_name='kelvin'
        self._middle_name='kipruto'
        self._last_name='kaimor'

    def get_first_name(self):
        return self._first_name
    def get_middle_name(self):
        return self._middle_name
    def get_last_name(self):
        return self._last_name
tageless=Tageless('kelvin','kipruto','kaimor')
print(tageless.get_last_name(),tageless.get_middle_name(),tageless.get_last_name())
