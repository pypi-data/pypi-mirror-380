import requests
from .exceptions import TranslationError


class Translator:
    """کتابخونه irtranslate - مترجم ساده بدون API key.

    مثال:
        >>> from irtranslate import Translator
        >>> tr = Translator()
        >>> tr.translate("سلام دنیا", src="fa", dest="en")
        'Hello world'
    """

    BASE_URL = "https://translate.googleapis.com/translate_a/single"

    def __init__(self, default_dest="en"):
        self.default_dest = default_dest

    def translate(self, text: str, src: str = "auto", dest: str = None) -> str:
        dest = dest or self.default_dest
        if not text.strip():
            raise TranslationError("متن خالی است.")

        params = {
            "client": "gtx",
            "sl": src,
            "tl": dest,
            "dt": "t",
            "q": text,
        }
        try:
            resp = requests.get(self.BASE_URL, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            return "".join([seg[0] for seg in data[0]])
        except Exception as e:
            raise TranslationError(f"خطا در ترجمه: {e}")
