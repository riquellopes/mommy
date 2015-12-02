from mixer.backend.sqlalchemy import Mixer
from son import Son


mixer = Mixer()
son = mixer.blend(Son, name="Henrique", last_name="Lopes")


def test_creating_model():
    assert son.full_name == "Henrique Lopes"
