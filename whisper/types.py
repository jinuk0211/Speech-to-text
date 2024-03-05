# AlignedTranscriptionResult 클래스: 음성 인식 결과를 나타내는 클래스입니다.
class AlignedTranscriptionResult(TypedDict): #transcript 변환
  """
  음성의 segment와 word segment list 정렬된   A list of segments and word segments of a speech.
  """
  segments: List[SingleAlignedSegment]
  word_segments: List[SingleWordSegment]
class TranscriptionResult(TypedDict):
"""
음성의 segment와 word segment list    A list of segments and word segments of a speech.
"""
segments: List[SingleSegment]
language: str

class SingleAlignedSegment(TypedDict):
  """
두개 이상 문장으로 구성된 음성의 정렬된 단어들
"""

  start: float
  end: float
  text: str
  words: List[SingleWordSegment]
  chars: Optional[List[SingleCharSegment]]

class SingleSegment(TypedDict):
  """
2개이상 문장 음성의
단어들
"""

  start: float
  end: float
  text: str

class SingleCharSegment(TypedDict):
  """
음성에서의 문자
"""
  char: str
  start: float
  end: float
  score: float

class SingleWordSegment(TypedDict):
  """
음성의 단어들
"""
  word: str
  start: float
  end: float
  score: float
