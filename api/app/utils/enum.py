import enum


class SongGenre(str, enum.Enum):
    afro_beats = 'Afro beats'
    jazz = 'Jazz'
    rock = 'Rock'
    folk_music = 'Folk music'
    blues = 'Blues'
    rythm_and_blues = 'Rythm and blues'
    pop_music = 'Pop music'
    country_music = 'Country music'
    hip_hop_music = 'Hip hop music'
    musical_theatre = 'Musical theatre'
    classical_music = 'Classical music'
    popular_music = 'Popular music'
    funk = 'Funk'
    raggae = 'Raggae'
    punk_rock = 'Punk rock'
    heavy_metal = 'Heavy metal'
    dance_music = 'Dance music'
    techno = 'Techno'

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)


