
# Dictonary that contains every sample types
# Each one of them have a set of strings that the sample
# name have to match to be sorted in that category.

sample_types = {

    # From less ambiguous to more ambiguous

    # Bass
    "basses": ["bass"],
    "808s": ["808"],

    # voxes
    "voxes/shouts": ["shout"],
    "voxes/voices": ["voiced"],
    "voxes/vocals": ["vocal"],
    "voxes/acapella": ["acapella"],

    # Transitions
    "transitions/impacts": ["impact"],
    "transitions/risers": ["riser"],
    "transitions/uplifter": ["uplifter"],
    "transitions/sweeps": ["sweep"],
    "transitions/fills": ["fill"],
    "transitions/whooshs": ["whoosh"],

    # Ambiences
    "ambiences/rains": ["rain"],
    "ambiences/forests": ["forest"],
    "ambiences/natures": ["nature"],
    "ambiences/beaches": ["beach"],
    "ambiences/nights": ["night"],
    "ambiences/cities": ["city"],
    "ambiences/streets": ["street"],
    "ambiences/crowds": ["crowd"],
    "ambiences/thunderstorms": ["thunderstorm"],
    "ambiences/birds": ["bird"],
    "ambiences/others": ["ambiance", "ambience"],

    # Instruments
    "instruments/kalimbas": ["kalimba"],
    "instruments/guitars": ["guitar"],
    "instruments/flutes": ["flute"],
    "instruments/banjos": ["banjo"],
    "instruments/pianos": ["piano"],
    "instruments/violins": ["violin", "vio"],
    "instruments/saxophones": ["saxo", "sax"],
    "instruments/bells": ["bell"],
    "instruments/tambourines": ["tambourine", "tambo"],
    "instruments/triangles": ["triangle"],
    "instruments/synths": ["synth"],
    "instruments/marimbas": ["marimba"],
    "instruments/steelpans": ["steelpan"],
    "instruments/horns": ["horn"],
    "instruments/sitars": ["sitar"],
    "instruments/harp": ["harp"],
    "instruments/xylophones": ["xylo"],
    "instruments/trumpets": ["trumpet"],
    "instruments/brasses": ["brass"],

    # Fxs
    "fx/guns": ["gun", "rifle"],
    "fx/clocks": ["clock"],
    "fx/alarms": ["alarm"],
    "fx/sirens": ["siren"],
    "fx/coins": ["coin"],
    "fx/honks": ["honk"],
    "fx/others": ["fx", "effect"],

    # Drums
    "kicks": ["kick"],
    "snares": ["snare", "snr"],
    "claps": ["clap"],
    "rims": ["rim"],
    "toms": ["tom"],
    "timbales": ["timbale", "tim"],
    "hats/others": ["hat"],
    "cymbals": ["cymbal", "cym"],
    "crashes": ["crash", "crs", "crh"],
    "sizzles": ["sizzle"],
    "gongs": ["gong"],
    "pangs": ["pang"],
    "rides": ["ride"],
    "splashes": ["splash"],

    # Percs
    "percs/snaps": ["snap"],
    "percs/sticks": ["stick"],
    "percs/woodblocks": ["woodblock"],
    "percs/maracas": ["maraca"],
    "percs/shakers": ["shaker"],
    "percs/cowbells": ["cowbell"],
    "percs/bongos": ["bongo"],
    "percs/djembe": ["djembe"],
    "percs/timpanies": ["timpani"],
    "percs/castanets": ["castanet"],
    "percs/congas": ["conga"],
    "percs/others": ["perc", "prc"],

    # Transitions #2 (more ambiguous)
    "transitions/hits": ["hit"],

    # Textures
    "textures/vinyl": ["vinyl"],
    "textures/others": ["texture"],

    # Voice #2 (more ambiguous)
    "voxes/woo": ["woo"],
    "voxes/yeah": ["yeah"],
    "voxes/uh": ["uh"],
    "voxes/hey": ["hey"],
    "voxes/breath": ["breath"],
}
