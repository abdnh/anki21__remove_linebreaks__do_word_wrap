# License AGPLv3


from aqt import mw


def gc(arg, fail=False):
    conf = mw.addonManager.getConfig(__name__)
    if conf:
        return conf.get(arg, fail)
    else:
        return fail
        

def get_anki_version():
    try:
        # 2.1.50+ because of bdd5b27715bb11e4169becee661af2cb3d91a443, https://github.com/ankitects/anki/pull/1451
        from anki.utils import point_version
    except:
        try:
            # introduced with 66714260a3c91c9d955affdc86f10910d330b9dd in 2020-01-19, should be in 2.1.20+
            from anki.utils import anki_point_version
        except:
            # <= 2.1.19
            from anki import version as anki_version
            return int(anki_version.split(".")[-1]) 
        else:
            return anki_point_version()
    else:
        return point_version()
anki_point_version = get_anki_version()
