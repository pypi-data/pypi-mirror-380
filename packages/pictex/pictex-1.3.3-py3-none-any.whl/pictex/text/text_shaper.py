import skia
from typing import List
from .typeface_loader import TypefaceLoader
from .font_manager import FontManager
from ..models import Style, Line, TextRun
import re

class TextShaper:
    def __init__(self, style: Style, font_manager: FontManager):
        self._style = style
        self._font_manager = font_manager

    def shape(self, text: str, max_width: float = None) -> List[Line]:
        """
        Breaks a text string into lines and runs, applying font fallbacks.
        This is the core of the text shaping and fallback logic.
        If max_width is provided, performs word wrapping.
        """

        shaped_lines: list[Line] = []
        font_height = self._get_primary_font_height()
        
        for line_text in text.split('\n'):
            if not line_text:
                shaped_lines.append(self._create_empty_line())
                continue
            
            if max_width is not None:
                wrapped_lines = self._wrap_line_to_width(line_text, max_width)
                for wrapped_line_text in wrapped_lines:
                    if not wrapped_line_text:
                        shaped_lines.append(self._create_empty_line())
                        continue
                    runs: list[TextRun] = self._split_line_in_runs(wrapped_line_text)
                    line = self._create_line(runs, font_height)
                    shaped_lines.append(line)
            else:
                runs: list[TextRun] = self._split_line_in_runs(line_text)
                line = self._create_line(runs, font_height)
                shaped_lines.append(line)
        
        return shaped_lines

    def _get_primary_font_height(self) -> float:
        font_metrics = self._font_manager.get_primary_font().getMetrics()
        return -font_metrics.fAscent + font_metrics.fDescent + font_metrics.fLeading

    def _create_empty_line(self) -> Line:
        """Handle empty lines by creating a placeholder with correct height"""

        primary_font = self._font_manager.get_primary_font()
        line = Line(runs=[], height=0, width=0, bounds=skia.Rect.MakeEmpty())
        font_metrics = primary_font.getMetrics()
        line.bounds = skia.Rect.MakeLTRB(0, font_metrics.fAscent, 0, font_metrics.fDescent)
        return line
    
    def _create_line(self, runs: list[TextRun], font_height: float) -> Line:
        line_width = 0
        for run in runs:
            run.width = run.font.measureText(run.text)
            line_width += run.width

        return Line(runs=runs, width=line_width, height=font_height, bounds=skia.Rect.MakeWH(line_width, font_height))
    
    def _split_line_in_runs(self, line_text: str) -> list[TextRun]:
        primary_font = self._font_manager.get_primary_font()
        line_runs: list[TextRun] = []
        current_run_text = ""

        for char in line_text:
            if self._is_glyph_supported_for_typeface(char, primary_font.getTypeface()):
                current_run_text += char
                continue

            if current_run_text:
                run = TextRun(current_run_text, primary_font)
                line_runs.append(run)
                current_run_text = ""

            fallback_font = self._get_fallback_font_for_glyph(char, primary_font)
            is_same_font_than_last_run = len(line_runs) > 0 and line_runs[-1].font.getTypeface() == fallback_font.getTypeface()
            if is_same_font_than_last_run:
                # we join contiguous runs with same font
                line_runs[-1] = TextRun(line_runs[-1].text + char, fallback_font)
            else:
                line_runs.append(TextRun(char, fallback_font))
        
        # Add the last run
        if current_run_text:
            run = TextRun(current_run_text, primary_font)
            line_runs.append(run)
        
        return line_runs

    def _get_fallback_font_for_glyph(self, glyph: str, primary_font: skia.Font) -> skia.Font:
        fallback_typefaces = self._font_manager.get_fallback_font_typefaces()
        for typeface in fallback_typefaces:
            if self._is_glyph_supported_for_typeface(glyph, typeface):
                fallback_font = primary_font.makeWithSize(primary_font.getSize())
                fallback_font.setTypeface(typeface)
                return fallback_font

        # if we don't find a font supporting the glyph, we try to find one in the system
        font_style = skia.FontStyle(
            weight=self._style.font_weight.get(),
            width=skia.FontStyle.kNormal_Width,
            slant=self._style.font_style.get().to_skia_slant()
        )
        system_typeface = TypefaceLoader.load_for_glyph(glyph, font_style)
        if system_typeface:
            fallback_font = primary_font.makeWithSize(primary_font.getSize())
            fallback_font.setTypeface(system_typeface)
            return fallback_font

        # if we don't find any font in the system supporting the glyph, we just use the primary font
        return primary_font

    def _is_glyph_supported_for_typeface(self, glyph: str, typeface: skia.Typeface) -> bool:
        return typeface.unicharToGlyph(ord(glyph)) != 0

    def _wrap_line_to_width(self, text: str, max_width: float) -> List[str]:
        """
        Wraps a single line of text to fit within the specified width.
        Words are treated as indivisible units.
        """
        # Split into words and spaces, keeping both
        tokens = re.findall(r'\S+|\s+', text)
        if not tokens:
            return ['']

        primary_font = self._font_manager.get_primary_font()
        wrapped_lines = []
        current_line = []
        current_width = 0

        for token in tokens:
            token_width = primary_font.measureText(token)

            # If it's the first token, add it regardless
            if not current_line:
                current_line.append(token)
                current_width = token_width
                continue

            potential_width = current_width + token_width

            if potential_width <= max_width:
                # Token fits, add it
                current_line.append(token)
                current_width = potential_width
            else:
                # Token doesn't fit, start new line
                wrapped_lines.append(''.join(current_line).strip())
                current_line = [token]
                current_width = token_width

        if current_line:
            wrapped_lines.append(''.join(current_line).strip())

        if len(wrapped_lines) == 1:
            # This is to avoid removing spaces at the begining or at the end of a line
            # when the line was not actually wrapped.
            # When the line is wrapped we must remove spaces at the begining and at the end of each line
            # to obtain an useful behavior (avoid single spaces at the begining of a line, for example)
            return [text]
        
        return wrapped_lines if wrapped_lines else ['']
    
    def _measure_word_width(self, word: str) -> float:
        """
        Measures the width of a word, accounting for font fallbacks.
        """
        primary_font = self._font_manager.get_primary_font()
        total_width = 0
        current_run_text = ""
        
        for char in word:
            if self._is_glyph_supported_for_typeface(char, primary_font.getTypeface()):
                current_run_text += char
                continue
            
            # Measure current run with primary font
            if current_run_text:
                total_width += primary_font.measureText(current_run_text)
                current_run_text = ""
            
            # Measure fallback character
            fallback_font = self._get_fallback_font_for_glyph(char, primary_font)
            total_width += fallback_font.measureText(char)
        
        # Measure remaining text with primary font
        if current_run_text:
            total_width += primary_font.measureText(current_run_text)
        
        return total_width
    