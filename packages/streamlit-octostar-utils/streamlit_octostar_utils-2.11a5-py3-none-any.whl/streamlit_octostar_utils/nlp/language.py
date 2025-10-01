import re
import py3langid as langid
import iso639 as languages


def alpha2_to_language(alpha2: str) -> str:
    if not alpha2:
        return None
    code = alpha2.strip().lower()
    return languages.to_name(code)

def language_to_alpha2(language_name: str) -> str:
    if not language_name:
        return None
    name = language_name.strip().lower()
    data = languages.find(name)
    return data["iso639_1"]

def detect_language(text, min_confidence=None):
    detector = langid.langid.LanguageIdentifier.from_pickled_model(
        langid.langid.MODEL_FILE, norm_probs=True
    )
    detected_lang, confidence = detector.classify(text)
    if min_confidence and confidence < min_confidence:
        return None, confidence
    detected_lang = re.sub("[^A-Za-z]", "", detected_lang).lower()
    detected_lang = languages.to_name(detected_lang).lower()
    return detected_lang, confidence
