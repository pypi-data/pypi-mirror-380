import requests
from time import sleep
from .exceptions import TranslationError

class Translator:
    BASE_URL = "https://translate.googleapis.com/translate_a/single"

    def __init__(self, default_dest="en", retries=3, delay=1, cache_enabled=True):
        """
        :param default_dest: زبان پیش‌فرض مقصد
        :param retries: تعداد تلاش دوباره در صورت خطا
        :param delay: فاصله بین تلاش‌ها (ثانیه)
        :param cache_enabled: فعال بودن cache داخلی برای ترجمه‌های تکراری
        """
        self.default_dest = default_dest
        self.retries = retries
        self.delay = delay
        self.cache_enabled = cache_enabled
        self._cache = {}

    def translate(self, text, src="auto", dest=None, return_detected_lang=False):
        """
        ترجمه متن
        :param text: متن یا لیست متن‌ها
        :param src: زبان مبدا ('auto' برای تشخیص خودکار)
        :param dest: زبان مقصد، یا لیست زبان‌ها
        :param return_detected_lang: اگر True، زبان تشخیص داده شده برگردانده می‌شود
        :return: ترجمه یا دیکشنری ترجمه‌ها
        """
        dest = dest or self.default_dest

        # چند متن
        if isinstance(text, list):
            return [self._translate_single(t, src, dest, return_detected_lang) for t in text]
        # چند زبان مقصد
        elif isinstance(dest, list):
            return {d: self._translate_single(text, src, d, return_detected_lang) for d in dest}
        else:
            return self._translate_single(text, src, dest, return_detected_lang)

    def _translate_single(self, text, src, dest, return_detected_lang=False):
        if not text.strip():
            raise TranslationError("متن خالی است.")

        cache_key = (text, src, dest)
        if self.cache_enabled and cache_key in self._cache:
            return self._cache[cache_key]

        lines = text.split("\n")
        translated_lines = []
        detected_language = None

        for line in lines:
            if not line.strip():
                translated_lines.append("")
                continue

            params = {
                "client": "gtx",
                "sl": src,
                "tl": dest,
                "dt": "t",
                "q": line,
            }

            for attempt in range(1, self.retries + 1):
                try:
                    resp = requests.get(self.BASE_URL, params=params, timeout=10)
                    resp.raise_for_status()
                    data = resp.json()
                    translated_lines.append("".join([seg[0] for seg in data[0]]))
                    if return_detected_lang:
                        # Google زبان مبدا را در data[2] می‌دهد
                        detected_language = data[2] if len(data) > 2 else src
                    break
                except requests.exceptions.RequestException as e:
                    if attempt == self.retries:
                        translated_lines.append(f"[NetworkError: {e}]")
                    else:
                        sleep(self.delay)
                except Exception as e:
                    raise TranslationError(f"خطا در ترجمه: {e}")

        result = "\n".join(translated_lines)

        if self.cache_enabled:
            self._cache[cache_key] = result

        if return_detected_lang:
            return {"translation": result, "detected_lang": detected_language}
        return result
