# Rexa Usage Guide

Rexa is a Python library for regex operations and text preprocessing, supporting validation, extraction, conversion, formatting, pattern generation, and NLP tasks.

## Getting Started

Install via pip:
```
pip install rexa
```

Import:
```python
import rexa
```

**Dependencies**: Python 3.10+, regex, dateparser, pydantic, nltk, langdetect.  
**Source**: [GitHub](https://github.com/arshia82sbn/rexa) | [Issues](https://github.com/arshia82sbn/rexa/issues)

## Validator (validation.py)

| Method | Description | Example |
|--------|-------------|---------|
| Is_Email(s) | Validates email format | rexa.Is_Email("user@example.com") → True |
| Match_Email(s) | Returns email Match object | rexa.Match_Email("bad@") → None |
| Is_URL(s) | Validates HTTP/HTTPS URLs | rexa.Is_URL("https://site.io") → True |
| Match_URL(s) | Matches URL, captures path/query | rexa.Match_URL("site.com/path") |
| Is_Date_ISO(s) | Validates YYYY-MM-DD format | rexa.Is_Date_ISO("2025-08-02") → True |
| Match_Date_ISO(s) | Matches ISO date | rexa.Match_Date_ISO("02/08/2025") → None |
| Is_Date_EU(s) | Validates DD/MM/YYYY format | rexa.Is_Date_EU("02/08/2025") → True |
| Match_Date_EU(s) | Matches EU date | rexa.Match_Date_EU("2025-08-02") → None |
| Is_Time(s) | Validates HH:MM(:SS) format | rexa.Is_Time("14:30") → True |
| Match_Time(s) | Matches time | rexa.Match_Time("14:30:45") |
| Is_IranianPhone(s) | Validates Iranian mobile numbers | rexa.Is_IranianPhone("09121234567") → True |
| Match_IranianPhone(s) | Matches Iranian phone | rexa.Match_IranianPhone("+989121234567") |
| Is_InternationalPhone(s) | Validates international phone numbers | rexa.Is_InternationalPhone("+123456789") → True |
| Match_InternationalPhone(s) | Matches international phone | rexa.Match_InternationalPhone("123456789") |
| Is_UUID4(s) | Validates UUID v4 format | rexa.Is_UUID4("123e4567-e89b-12d3-a456-426614174000") → True |
| Match_UUID4(s) | Matches UUID v4 | rexa.Match_UUID4("invalid-uuid") → None |
| Is_IranNationalCode(s) | Validates 10-digit Iranian code | rexa.Is_IranNationalCode("1234567890") → True |
| Match_IranNationalCode(s) | Matches Iranian code | rexa.Match_IranNationalCode("1234567890") |
| Is_ISBN10(s) | Validates ISBN-10 format | rexa.Is_ISBN10("123456789X") → True |
| Match_ISBN10(s) | Matches ISBN-10 | rexa.Match_ISBN10("1234567890") |
| Is_ISBN13(s) | Validates ISBN-13 format | rexa.Is_ISBN13("1234567890123") → True |
| Match_ISBN13(s) | Matches ISBN-13 | rexa.Match_ISBN13("1234567890123") |
| Is_HexColor(s) | Validates hex color (#RGB or #RRGGBB) | rexa.Is_HexColor("#1a2b3c") → True |
| Match_HexColor(s) | Matches hex color | rexa.Match_HexColor("#fff") |
| Is_ScientificNumber(s) | Validates scientific notation | rexa.Is_ScientificNumber("1.23e-4") → True |
| Match_ScientificNumber(s) | Matches scientific number | rexa.Match_ScientificNumber("1.23e-4") |
| Is_ThousandSepNumber(s) | Validates comma-separated numbers | rexa.Is_ThousandSepNumber("1,234,567") → True |
| Match_ThousandSepNumber(s) | Matches thousand-separated number | rexa.Match_ThousandSepNumber("1,234.56") |
| Is_Mention(s) | Validates @username format | rexa.Is_Mention("@user123") → True |
| Match_Mention(s) | Matches mention | rexa.Match_Mention("@user123") |
| Is_MarkdownLink(s) | Validates markdown link format | rexa.Is_MarkdownLink("[text](url)") → True |
| Match_MarkdownLink(s) | Matches markdown link | rexa.Match_MarkdownLink("[text](url)") |
| Is_HTMLTag(s) | Validates HTML tag format | rexa.Is_HTMLTag("<div>") → True |
| Match_HTMLTag(s) | Matches HTML tag | rexa.Match_HTMLTag("<p>Hello</p>") |
| Is_MultipleEmails(s) | Validates comma-separated emails | rexa.Is_MultipleEmails("a@a.com,b@b.org") → True |
| Match_MultipleEmails(s) | Matches multiple emails | rexa.Match_MultipleEmails("a@a.com,b@b.org") |
| Is_Base64(s) | Validates base64 string | rexa.Is_Base64("SGVsbG8=") → True |
| Match_Base64(s) | Matches base64 string | rexa.Match_Base64("SGVsbG8=") |

## Extractor (extraction.py)

| Method | Description | Example |
|--------|-------------|---------|
| Extract_Emails(text) | Extracts all email addresses | rexa.Extract_Emails("a@a.com b@b.org") → ["a@a.com", "b@b.org"] |
| Extract_URLs(text) | Extracts web links (http/https/ftp) | rexa.Extract_URLs("Go to http://x.com") → ["http://x.com"] |
| Extract_Dates(text) | Extracts ISO/EU dates | rexa.Extract_Dates("2021-01-01 or 01/01/2021") → ["2021-01-01", "01/01/2021"] |
| Extract_Phones(text) | Extracts phone numbers | rexa.Extract_Phones("+123456789, 09121234567") → ["+123456789", "09121234567"] |
| Extract_IPv4(text) | Extracts IPv4 addresses | rexa.Extract_IPv4("192.168.1.1") → ["192.168.1.1"] |
| Extract_UUIDs(text) | Extracts UUID v4 strings | rexa.Extract_UUIDs("123e4567-e89b-12d3-a456-426614174000") → ["123e4567-e89b-12d3-a456-426614174000"] |
| Extract_HexColors(text) | Extracts hex colors | rexa.Extract_HexColors("#fff #1a2b3c") → ["#fff", "#1a2b3c"] |
| Extract_ScientificNumbers(text) | Extracts scientific notation | rexa.Extract_ScientificNumbers("1.23e-4") → ["1.23e-4"] |
| Extract_ThousandSepNumbers(text) | Extracts comma-separated numbers | rexa.Extract_ThousandSepNumbers("1,234,567") → ["1,234,567"] |
| Extract_Mentions(text) | Extracts @usernames | rexa.Extract_Mentions("@user1 @user2") → ["@user1", "@user2"] |
| Extract_MarkdownLinks(text) | Extracts markdown links | rexa.Extract_MarkdownLinks("[text](url)") → ["[text](url)"] |
| Extract_HTMLTags(text) | Extracts HTML tags | rexa.Extract_HTMLTags("<p>Hello</p>") → ["<p>", "</p>"] |
| Extract_Base64(text) | Extracts base64 strings | rexa.Extract_Base64("SGVsbG8=") → ["SGVsbG8="] |

## Converter (conversion.py)

| Method | Description | Example |
|--------|-------------|---------|
| Convert_MultipleSpaces(text) | Collapses multiple spaces | rexa.Convert_MultipleSpaces("A   B") → "A B" |
| Convert_ThousandSeparatedNumbers(text) | Removes commas from numbers | rexa.Convert_ThousandSeparatedNumbers("1,234,567") → "1234567" |
| Convert_DateFormat(s, from_sep, to_sep) | Changes date separators | rexa.Convert_DateFormat("01.01.2025", ".", "/") → "01/01/2025" |
| Slugify(text) | Creates SEO-friendly slugs | rexa.Slugify("Hello World!") → "hello-world" |

## Formatter (formatting.py)

| Method | Description | Example |
|--------|-------------|---------|
| Strip_HTMLTags(s) | Removes HTML tags | rexa.Strip_HTMLTags("<b>Hi</b>") → "Hi" |
| Normalize_Spaces(s) | Collapses whitespace to single spaces | rexa.Normalize_Spaces("A   B") → "A B" |
| Remove_ThousandSeparators(s) | Removes commas from numbers | rexa.Remove_ThousandSeparators("1,234") → "1234" |
| Normalize_DateSeparator(s, sep) | Standardizes date delimiters | rexa.Normalize_DateSeparator("2021/01.01", "-") → "2021-01-01" |

## Regex Mapper (regex_mapper.py)

| Method | Description | Example |
|--------|-------------|---------|
| string_to_regex(text, use_anchors=False, use_char_map=True, detailed=False) | Generates fuzzy regex pattern | rexa.string_to_regex("i'm") → "\b[iIíìîïİ1!|]['‘’][mM]\b" |
| string_to_breakdown(text, use_char_map=True, detailed=False) | Breaks text into regex components | rexa.string_to_breakdown("i'm") → [{"type": "LETTER", "pattern": "[iIíìîïİ1!|]", ...}, ...] |
| get_all_patterns() | Returns predefined patterns | rexa.get_all_patterns() → {"email": "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", ...} |

## TextTools (texttools.py)

| Method | Description | Example |
|--------|-------------|---------|
| to_lower(s) | Converts to lowercase | rexa.to_lower("HELLO") → "hello" |
| to_upper(s) | Converts to uppercase | rexa.to_upper("hi") → "HI" |
| remove_emojis(s) | Removes Unicode emojis | rexa.remove_emojis("I ❤️ you") → "I  you" |
| remove_numbers(s) | Removes digits | rexa.remove_numbers("a1b2") → "ab" |
| remove_usernames(s) | Removes @usernames | rexa.remove_usernames("@me hi") → " hi" |
| remove_urls_emails(s) | Removes URLs and emails | rexa.remove_urls_emails("a@b.com http://x") → " " |
| remove_punctuation(s) | Removes punctuation | rexa.remove_punctuation("Hey!?@") → "Hey" |
| remove_stopwords(s) | Removes common words | rexa.remove_stopwords("the cat sits") → "cat sits" |
| lemmatize_text(s) | Lemmatizes tokens | rexa.lemmatize_text("running") → "run" |
| stem_text(s) | Stems tokens | rexa.stem_text("running") → "run" |
| normalize_whitespace(s) | Collapses whitespace | rexa.normalize_whitespace(" A  B\n") → "A B" |
| normalize_arabic(s) | Normalizes Persian/Arabic chars | rexa.normalize_arabic("كیف") → "کیف" |
| count_tokens(s) | Counts word tokens | rexa.count_tokens("a b c") → 3 |
| remove_short_long_words(s, min, max) | Keeps words in length range | rexa.remove_short_long_words("a bb ccc", 2, 3) → "bb ccc" |
| detect_language(s) | Detects text language | rexa.detect_language("hello") → "en" |
| clean_text(s, **kwargs) | Applies cleaning pipeline | rexa.clean_text("Hi @you 123 😊", lowercase=True, remove_emoji=True) → "hi" |

## Quick Tips
- **Combine Functions**: Chain methods (e.g., `clean_text` → `Extract_Emails`).
- **Fuzzy Matching**: Use `string_to_regex(use_char_map=True)` for robust patterns.
- **Performance**: Batch large texts with `map()` or multiprocessing.
- **Extensibility**: Subclass Rexa for custom patterns.
- **Debugging**: Enable logging via `utils.Logger`.

## Example Workflow
```python
import rexa
text = "Contact: alice@example.com, bob@TEST.org  Date: 2025-08-02 😊"
cleaned = rexa.clean_text(text, lowercase=True, remove_emoji=True)
emails = rexa.Extract_Emails(cleaned)
is_valid_date = rexa.Is_Date_ISO("2025-08-02")
pattern = rexa.string_to_regex("alice", use_char_map=True)
print(cleaned)  # contact: alice@example.com, bob@test.org date: 2025-08-02
print(emails)   # ['alice@example.com', 'bob@test.org']
print(is_valid_date)  # True
print(pattern)  # \b[aAáàâäãåā@4][lL1|][iIíìîïİ1!|][cCçćč][eEéèêëē3]\b
```

Feedback? [Open an issue](https://github.com/arshia82sbn/rexa/issues).