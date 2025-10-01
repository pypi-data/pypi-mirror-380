# irtranslate

irtranslate یک کتابخانه ساده ترجمه متن بدون نیاز به API key است.

## نصب

```bash
pip install irtranslate
```

## استفاده

```python
from irtranslate import Translator

tr = Translator()
print(tr.translate("سلام دنیا", dest="en"))  # Hello world
```
