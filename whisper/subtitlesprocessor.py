import math
import textIO
from conjunctions import get_conjunctions, get_comma #접속사,콤마

def round(n): #.round()함수
  if n - math.floor(n) < 0.5: #ex) 3.4 -> 3 / 3.4 - 3 = 0.4 따라서 false
    return math.floor(n)
  return math.ceil(n)
    
def format_timestep(seconds : float, is_vtt : bool =  False):
  assert seconds >=0, '시간이 음수가 되서는 안된다.' 
  milliseconds = round(seconds * 1000.0) #ex 2.123초 => 2123 밀리초

  hours = milliseconds // 3600000 # 밀리초를 시간으로 되돌림
  milliseconds -= hours * 3600000

  minutes = milliseconds // 60000
  milliseconds -= minutes * 60000 # 분을 밀리초로 변환해서 빼줌

  seconds = milliseconds // 1000
  milliseconds -= seconds * 1000 # 초를 밀리초로 변환해서 빼줌

  seperator = '.' if is_vtt ',' 
  #hours 가 3일경우 03반환  
  hoursmarker = f'{hours : 02d}:'
  return (f'{hoursmarker}{minutes:02d}:{seconds:02d}{seperator}{milliseconds:02d}'
  )

  class SubtitlesProcessor:
    def __init__(self, segments, lang, max_line_length = 45, min_char_length_splitter = 30, is_vtt = False):
    
    def estimate_timestamp_for_word(self, words, i, next_segment_start_time=None):

    def process_segments(self, advanced_splitting=True):

    def determine_advanced_split_points(self, segment, next_segment_start_time=None):

    def save(self, filename="subtitles.srt", advanced_splitting=True):
    def generate_subtitles_from_split_points(self, segment, split_points, next_start_time=None):
