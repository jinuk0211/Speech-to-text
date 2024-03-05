LANGUAGES = {
    "en": "english",
    "zh": "chinese",
    "de": "german",
    "es": "spanish",
    "ru": "russian",
    "ko": "korean",
    "fr": "french",
    "ja": "japanese",
    "pt": "portuguese",
    "tr": "turkish",
    "pl": "polish",
    "ca": "catalan",
    "nl": "dutch",
    "ar": "arabic",
    "sv": "swedish",
    "it": "italian",
    "id": "indonesian",
    "hi": "hindi",
    "fi": "finnish",
    "vi": "vietnamese",
    "he": "hebrew",
    "uk": "ukrainian",
    "el": "greek",
    "ms": "malay",
    "cs": "czech",
    "ro": "romanian",
    "da": "danish",
    "hu": "hungarian",
    "ta": "tamil",
    "no": "norwegian",
    "th": "thai",
    "ur": "urdu",
    "hr": "croatian",
    "bg": "bulgarian",
    "lt": "lithuanian",
    "la": "latin",
    "mi": "maori",
    "ml": "malayalam",
    "cy": "welsh",
    "sk": "slovak",
    "te": "telugu",
    "fa": "persian",
    "lv": "latvian",
    "bn": "bengali",
    "sr": "serbian",
    "az": "azerbaijani",
    "sl": "slovenian",
    "kn": "kannada",
    "et": "estonian",
    "mk": "macedonian",
    "br": "breton",
    "eu": "basque",
    "is": "icelandic",
    "hy": "armenian",
    "ne": "nepali",
    "mn": "mongolian",
    "bs": "bosnian",
    "kk": "kazakh",
    "sq": "albanian",
    "sw": "swahili",
    "gl": "galician",
    "mr": "marathi",
    "pa": "punjabi",
    "si": "sinhala",
    "km": "khmer",
    "sn": "shona",
    "yo": "yoruba",
    "so": "somali",
    "af": "afrikaans",
    "oc": "occitan",
    "ka": "georgian",
    "be": "belarusian",
    "tg": "tajik",
    "sd": "sindhi",
    "gu": "gujarati",
    "am": "amharic",
    "yi": "yiddish",
    "lo": "lao",
    "uz": "uzbek",
    "fo": "faroese",
    "ht": "haitian creole",
    "ps": "pashto",
    "tk": "turkmen",
    "nn": "nynorsk",
    "mt": "maltese",
    "sa": "sanskrit",
    "lb": "luxembourgish",
    "my": "myanmar",
    "bo": "tibetan",
    "tl": "tagalog",
    "mg": "malagasy",
    "as": "assamese",
    "tt": "tatar",
    "haw": "hawaiian",
    "ln": "lingala",
    "ha": "hausa",
    "ba": "bashkir",
    "jw": "javanese",
    "su": "sundanese",
    "yue": "cantonese",
}
#  alias
# 프로그래밍 언어에서 변수, 함수, 클래스 등을 지칭하는 다른 이름을 의미.
# 예를 들어, int는 integer의 별칭.
TO_LANGUAGE_CODE = {
    **{language: code for code, language in LANGUAGES.items()},
    "burmese": "my",
    "valencian": "ca",
    "flemish": "nl",
    "haitian": "ht",
    "letzeburgesch": "lb",
    "pushto": "ps",
    "panjabi": "pa",
    "moldavian": "ro",
    "moldovan": "ro",
    "sinhalese": "si",
    "castilian": "es",
}
system_encoding = sys.getdefaultencoding()
if system_encoding != 'utf-8': # 영어
  def make_safe(string):
        #utf8이 아닌경우 round trip을 해야함
    return string.encode(system_encoding, errors="replace").decode(system_encoding)
  def(make_safe):
    return string
       # round-trip encoding - 데이터를 인코딩하고 다시 디코딩하여 원본 데이터를 손실 없이 복원하는 과정
      # but utf8은 모든 어느 유니코드든 인코드 가능해서 round=trip encoding필요가없음
def exact_div(x,y):
  assert x % y == 0: #나머지가 남지않음
  return x // y

def str2bool(string):
  str2bool = {"True": True, "False": False}
  if string in str2bool:
    return str2bool[string]
  else:
    raise ValueError(f'{set(str2bool.keys())}중에 값을 입력해주세요')

def optional_int(string):

def optional_float(string):

def compression_ratio(text) -> float:

def format_timestamp(
    seconds: float, always_include_hours: bool = False, decimal_marker: str = "."
):

class ResultWriter:
    extension: str

class WriteTXT(ResultWriter):
    extension: str = "txt"

class SubtitlesWriter(ResultWriter): # subtitle = 부가설명
    always_include_hours: bool
    decimal_marker: str
   def iterate_result(self, result: dict, options: dict):
        raw_max_line_width: Optional[int] = options["max_line_width"]
        max_line_count: Optional[int] = options["max_line_count"]
        highlight_words: bool = options["highlight_words"]
        max_line_width = 1000 if raw_max_line_width is None else raw_max_line_width
        preserve_segments = max_line_count is None or raw_max_line_width is None
        
        if len(result["segments"]) == 0:
            return
          
        def iterate_subtitles():

# **SRT (SubRip Text)**와 **VTT (Web Video Text Tracks)**는 모두 자막 파일 형식이지만,
          # 몇 가지 주요 차이점이 있습니다.

# SRT: 주로 일반 비디오 파일 (MP4, AVI 등)과 함께 사용됩니다.
# VTT: 주로 HTML5 웹 비디오와 함께 사용됩니다.
class WriteVTT(SubtitlesWriter):
  
  def write_result(self, result: dict, file: TextIO, options: dict):
    
class WriteSRT(SubtitlesWriter):

  def write_result(self, result: dict, file: TextIO, options: dict):
class WriteTSV(ResultWriter): # tab-separated values
  def write_result(self, result: dict, file: TextIO, options: dict):

class WriteJSON(ResultWriter):
    extension: str = "json"

    def write_result(self, result: dict, file: TextIO, options: dict):


def get_writer(
    output_format: str, output_dir: str
) -> Callable[[dict, TextIO, dict], None]:

def interpolate_nans(x, method='nearest'):
