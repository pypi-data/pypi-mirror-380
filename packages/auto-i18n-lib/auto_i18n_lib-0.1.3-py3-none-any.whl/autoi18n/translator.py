# src/autoi18n/translator.py
import os
import re
import json
from html.parser import HTMLParser
from openai import OpenAI


def should_translate(text: str, tag: str = None) -> bool:
    """
    Определяем, нужно ли переводить текст.
    🚫 Отсекаем числа, GUIDы, чистую латиницу, логины, коды и тех. элементы.
    """
    text = text.strip()
    if not text:
        return False

    # 1. Числа
    if text.isdigit():
        return False
    if re.fullmatch(r"[\d\s\.,:/\-]+", text):
        return False

    # 2. GUID / UUID / хэши
    if re.fullmatch(r"[A-Fa-f0-9\-]{8,}", text):
        return False

    # 3. Чистая латиница (без кириллицы)
    if re.fullmatch(r"[A-Za-z0-9_\-\s\.:/]+", text):
        return False

    # 4. Таблицы
    if tag in ("table", "tr", "td", "th"):
        return False

    # 5. Интерактивные элементы
    if tag in ("input", "textarea", "select", "option"):
        return False

    return True


def cleanup_cache(cache: dict) -> dict:
    """
    Чистим словарь переводов от мусора.
    🚫 Удаляем числа, GUIDы, логины, коды, чистую латиницу.
    """
    cleaned = {}
    for key, value in cache.items():
        text = key.strip()
        if not text:
            continue
        if text.isdigit():
            continue
        if re.fullmatch(r"[\d\s\.,:/\-]+", text):
            continue
        if re.fullmatch(r"[A-Fa-f0-9\-]{8,}", text):
            continue
        if re.fullmatch(r"[A-Za-z0-9_\-\s\.:/]+", text):
            continue
        cleaned[key] = value
    return cleaned


class SimpleHTMLTranslator(HTMLParser):
    """
    HTML парсер: обходит дерево и подставляет переводы только в нужные места.
    """
    def __init__(self, translate_callback):
        super().__init__()
        self.result = []
        self.translate_callback = translate_callback
        self._current_tag = None
        self._inside_skip = False

    def handle_starttag(self, tag, attrs):
        self._current_tag = tag
        self._inside_skip = False

        if tag in ("script", "style"):
            self._inside_skip = True

        # Кнопка langSwitch: содержимое пропускаем, сам тег сохраняем
        for attr, value in attrs:
            if attr == "id" and value == "langSwitch":
                self._inside_skip = True

        self.result.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._inside_skip:
            self._inside_skip = False
        if tag == "button" and self._inside_skip:
            self._inside_skip = False
        self.result.append(f"</{tag}>")

    def handle_data(self, data):
        if self._inside_skip:
            self.result.append(data)
        elif not should_translate(data, self._current_tag):
            self.result.append(data)
        elif self._current_tag == "button":
            translated = self.translate_callback(data, prompt_type="button")
            self.result.append(translated)
        else:
            translated = self.translate_callback(data)
            self.result.append(translated)

    def get_html(self):
        return "".join(self.result)


class Translator:
    """
    Основной класс переводчика:
    - ведёт кэш переводов (JSON по страницам/языкам);
    - фильтрует мусор;
    - вызывает OpenAI только для нужных текстов.
    """
    def __init__(self, cache_dir="./translations", api_key=None):
        self.source_lang = os.getenv("SOURCE_LANG", "ru")
        self.cache_dir = cache_dir
        self.client = OpenAI(api_key=api_key)
        self._current_file = None
        self._cache = {}

    def _file_path(self, page_name: str, lang: str) -> str:
        filename = f"{page_name}.{lang}.json"
        return os.path.join(self.cache_dir, filename)

    def _load_storage(self, page_name: str, lang: str):
        path = self._file_path(page_name, lang)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                self._cache = json.load(f)
        else:
            self._cache = {}
        self._current_file = path
        # Очистка мусора
        self._cache = cleanup_cache(self._cache)
        self._save_storage()

    def _save_storage(self):
        if self._current_file:
            os.makedirs(self.cache_dir, exist_ok=True)
            with open(self._current_file, "w", encoding="utf-8") as f:
                json.dump(self._cache, f, ensure_ascii=False, indent=2)

    def translate_text(self, text: str, target_lang: str, page_name="page", prompt_type="normal") -> str:
        text = text.strip()
        if not text:
            return text
        if target_lang == self.source_lang:
            return text
        if not self._current_file:
            self._load_storage(page_name, target_lang)

        if not should_translate(text):
            return text
        if text in self._cache:
            return self._cache[text]

        if prompt_type == "button":
            prompt = f"Translate this button label briefly from {self.source_lang} to {target_lang}:\n\n{text}"
        else:
            prompt = f"Translate this text from {self.source_lang} to {target_lang}:\n\n{text}"

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        translated = response.choices[0].message.content.strip()

        self._cache[text] = translated
        self._save_storage()
        return translated

    def translate_html(self, html: str, target_lang: str, page_name="page") -> str:
        if target_lang == self.source_lang:
            return html

        self._load_storage(page_name, target_lang)
        current_texts = []

        def translate_with_chunks(text: str, prompt_type: str = "normal") -> str:
            text = text.strip()
            if not text:
                return text
            current_texts.append(text)

            if not should_translate(text):
                return text
            if text in self._cache:
                return self._cache[text]

            if len(text) > 2000:
                step = 1500
                chunks = [text[i:i + step] for i in range(0, len(text), step)]
            else:
                chunks = [text]

            translated_parts = []
            for chunk in chunks:
                if prompt_type == "button":
                    prompt = f"Translate this button label to {target_lang}. Keep it short:\n\n{chunk}"
                else:
                    prompt = f"Translate to {target_lang}. Return only the translated text:\n\n{chunk}"

                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                )
                translated_parts.append(response.choices[0].message.content.strip())

            translated_text = " ".join(translated_parts)
            self._cache[text] = translated_text
            self._save_storage()
            return translated_text

        parser = SimpleHTMLTranslator(translate_callback=translate_with_chunks)
        parser.feed(html)

        # Синхронизация — убираем устаревшие ключи
        for old_key in list(self._cache.keys()):
            if old_key not in current_texts:
                self._cache.pop(old_key)
        self._save_storage()

        return parser.get_html()

    def detect_browser_lang(self, accept_language: str) -> str:
        if not accept_language:
            return self.source_lang
        return accept_language.split(",")[0].split("-")[0]

    def get_alternative_lang(self, current_lang: str, browser_lang: str) -> str:
        if current_lang == browser_lang:
            return "en"
        return browser_lang
