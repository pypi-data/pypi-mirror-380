"""
Transcript format converter - converts VTT, SRT, and other transcript formats to clean markdown.

Features:
- Removes timestamps and formatting artifacts
- Converts to paragraph format with proper spacing
- Preserves semantic breaks and speaker changes
- Handles multiple input formats (VTT, SRT, TTML, TXT)
"""

import re
from pathlib import Path
from typing import Optional, Union, List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class TranscriptConverter:
    """Converts transcript files to clean markdown format."""

    def __init__(self):
        self.supported_formats = ['.vtt', '.srt', '.ttml', '.txt', '.ass']

    def convert_to_markdown(
        self,
        input_file: Union[str, Path],
        output_file: Optional[Union[str, Path]] = None,
        paragraph_min_words: int = 15,
        preserve_speaker_labels: bool = True
    ) -> Dict[str, Any]:
        """
        Convert transcript file to clean markdown format.

        Args:
            input_file: Path to input transcript file
            output_file: Path for output markdown file (auto-generated if None)
            paragraph_min_words: Minimum words per paragraph before breaking
            preserve_speaker_labels: Whether to preserve speaker labels if found

        Returns:
            Dictionary with conversion results and metadata
        """
        input_path = Path(input_file)

        if not input_path.exists():
            raise FileNotFoundError(f"Transcript file not found: {input_path}")

        if input_path.suffix.lower() not in self.supported_formats:
            raise ValueError(f"Unsupported format: {input_path.suffix}")

        # Generate output filename if not provided
        if output_file is None:
            output_file = input_path.with_suffix('.md')
        else:
            output_file = Path(output_file)

        # Read and process the transcript
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Convert based on format
        format_type = input_path.suffix.lower()
        if format_type == '.vtt':
            markdown_text = self._convert_vtt(content, paragraph_min_words, preserve_speaker_labels)
        elif format_type == '.srt':
            markdown_text = self._convert_srt(content, paragraph_min_words, preserve_speaker_labels)
        elif format_type == '.ttml':
            markdown_text = self._convert_ttml(content, paragraph_min_words, preserve_speaker_labels)
        elif format_type in ['.txt', '.ass']:
            markdown_text = self._convert_generic(content, paragraph_min_words, preserve_speaker_labels)
        else:
            markdown_text = self._convert_generic(content, paragraph_min_words, preserve_speaker_labels)

        # Write markdown output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_text)

        # Generate statistics
        original_size = len(content)
        markdown_size = len(markdown_text)
        word_count = len(markdown_text.split())
        paragraph_count = len([p for p in markdown_text.split('\n\n') if p.strip()])

        result = {
            'success': True,
            'input_file': str(input_path),
            'output_file': str(output_file),
            'input_format': format_type,
            'original_size': original_size,
            'markdown_size': markdown_size,
            'compression_ratio': (original_size - markdown_size) / original_size,
            'word_count': word_count,
            'paragraph_count': paragraph_count,
            'average_words_per_paragraph': word_count / paragraph_count if paragraph_count > 0 else 0
        }

        logger.info(f"Converted {input_path} to {output_file}: {word_count} words, {paragraph_count} paragraphs")
        return result

    def _convert_vtt(self, content: str, min_words: int, preserve_speakers: bool) -> str:
        """Convert WebVTT format to markdown."""
        lines = content.split('\n')
        text_lines = []

        # Skip WEBVTT header and metadata
        in_cue = False
        current_text = []

        for line in lines:
            line = line.strip()

            # Skip empty lines, WEBVTT header, and NOTE blocks
            if not line or line.startswith('WEBVTT') or line.startswith('NOTE'):
                continue

            # Skip timestamp lines (contains -->)
            if '-->' in line:
                in_cue = True
                continue

            # If we're in a cue and this is text
            if in_cue and line:
                # Remove VTT formatting tags
                cleaned = self._clean_vtt_formatting(line)
                if cleaned:
                    current_text.append(cleaned)
            elif not line and current_text:
                # End of cue block
                text_lines.extend(current_text)
                current_text = []
                in_cue = False

        # Add any remaining text
        if current_text:
            text_lines.extend(current_text)

        return self._format_as_paragraphs(text_lines, min_words, preserve_speakers)

    def _convert_srt(self, content: str, min_words: int, preserve_speakers: bool) -> str:
        """Convert SRT format to markdown."""
        lines = content.split('\n')
        text_lines = []

        for line in lines:
            line = line.strip()

            # Skip empty lines, sequence numbers, and timestamp lines
            if not line or line.isdigit() or '-->' in line:
                continue

            # Remove SRT formatting tags
            cleaned = self._clean_srt_formatting(line)
            if cleaned:
                text_lines.append(cleaned)

        return self._format_as_paragraphs(text_lines, min_words, preserve_speakers)

    def _convert_ttml(self, content: str, min_words: int, preserve_speakers: bool) -> str:
        """Convert TTML/XML format to markdown."""
        # Remove XML tags but preserve text content
        import xml.etree.ElementTree as ET

        try:
            # Parse as XML
            root = ET.fromstring(content)
            text_lines = []

            # Extract all text content
            for elem in root.iter():
                if elem.text and elem.text.strip():
                    cleaned = elem.text.strip()
                    if cleaned:
                        text_lines.append(cleaned)
                if elem.tail and elem.tail.strip():
                    cleaned = elem.tail.strip()
                    if cleaned:
                        text_lines.append(cleaned)
        except ET.ParseError:
            # If XML parsing fails, fall back to regex
            text_lines = self._extract_text_from_xml_regex(content)

        return self._format_as_paragraphs(text_lines, min_words, preserve_speakers)

    def _convert_generic(self, content: str, min_words: int, preserve_speakers: bool) -> str:
        """Convert generic text format to markdown."""
        lines = content.split('\n')
        text_lines = []

        for line in lines:
            line = line.strip()

            # Skip obvious timestamp patterns
            if self._is_timestamp_line(line):
                continue

            if line:
                text_lines.append(line)

        return self._format_as_paragraphs(text_lines, min_words, preserve_speakers)

    def _clean_vtt_formatting(self, text: str) -> str:
        """Remove VTT formatting tags and artifacts."""
        # Remove VTT tags like <c>, <i>, <b>, etc.
        text = re.sub(r'<[^>]+>', '', text)

        # Remove speaker labels in format [Speaker: text] if not preserving
        text = re.sub(r'\[([^:]+):\s*', r'\1: ', text)

        # Clean HTML entities
        text = self._clean_html_entities(text)

        # Clean up whitespace
        text = ' '.join(text.split())

        return text.strip()

    def _clean_srt_formatting(self, text: str) -> str:
        """Remove SRT formatting tags."""
        # Remove HTML-style tags
        text = re.sub(r'<[^>]+>', '', text)

        # Remove SRT formatting like {italic}, {bold}
        text = re.sub(r'\{[^}]+\}', '', text)

        # Clean HTML entities
        text = self._clean_html_entities(text)

        # Clean up whitespace
        text = ' '.join(text.split())

        return text.strip()

    def _clean_html_entities(self, text: str) -> str:
        """Clean HTML entities and special characters."""
        import html

        # Decode HTML entities
        text = html.unescape(text)

        # Replace common entities manually if html.unescape doesn't catch them
        entity_replacements = {
            '&nbsp;': ' ',
            '&ndash;': '—',
            '&mdash;': '—',
            '&ldquo;': '"',
            '&rdquo;': '"',
            '&lsquo;': "'",
            '&rsquo;': "'",
            '&amp;': '&',
            '&lt;': '<',
            '&gt;': '>',
        }

        for entity, replacement in entity_replacements.items():
            text = text.replace(entity, replacement)

        return text

    def _extract_text_from_xml_regex(self, content: str) -> List[str]:
        """Extract text from XML using regex as fallback."""
        # Remove XML/HTML tags
        text = re.sub(r'<[^>]+>', '', content)

        # Split into lines and clean
        lines = text.split('\n')
        cleaned_lines = []

        for line in lines:
            line = line.strip()
            if line and not self._is_timestamp_line(line):
                cleaned_lines.append(line)

        return cleaned_lines

    def _is_timestamp_line(self, line: str) -> bool:
        """Check if line contains timestamp patterns."""
        timestamp_patterns = [
            r'\d{2}:\d{2}:\d{2}',  # HH:MM:SS
            r'\d{1,2}:\d{2}\.\d{3}',  # M:SS.mmm
            r'-->', # SRT/VTT separator
            r'^\d+$'  # SRT sequence numbers
        ]

        return any(re.search(pattern, line) for pattern in timestamp_patterns)

    def _detect_speaker_changes(self, lines: List[str]) -> List[str]:
        """Detect and preserve speaker changes."""
        processed_lines = []

        for line in lines:
            # Look for speaker patterns
            speaker_match = re.match(r'^([A-Z][^:]{0,20}):\s*(.+)', line)
            if speaker_match:
                speaker, text = speaker_match.groups()
                processed_lines.append(f"**{speaker}:** {text}")
            else:
                processed_lines.append(line)

        return processed_lines

    def _format_as_paragraphs(self, lines: List[str], min_words: int, preserve_speakers: bool) -> str:
        """Format text lines as markdown paragraphs."""
        if not lines:
            return ""

        # Detect speaker changes if requested
        if preserve_speakers:
            lines = self._detect_speaker_changes(lines)

        paragraphs = []
        current_paragraph = []
        current_word_count = 0

        for line in lines:
            words = line.split()
            word_count = len(words)

            # Check if this should start a new paragraph
            should_break = (
                current_word_count >= min_words and (
                    line.startswith('**') or  # Speaker change
                    current_word_count + word_count > min_words * 2 or  # Too long
                    self._is_natural_break(line)  # Natural break point
                )
            )

            if should_break and current_paragraph:
                paragraphs.append(' '.join(current_paragraph))
                current_paragraph = [line]
                current_word_count = word_count
            else:
                current_paragraph.append(line)
                current_word_count += word_count

        # Add final paragraph
        if current_paragraph:
            paragraphs.append(' '.join(current_paragraph))

        # Join paragraphs with double newlines
        markdown_text = '\n\n'.join(paragraphs)

        # Clean up excessive whitespace
        markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)
        markdown_text = re.sub(r' {2,}', ' ', markdown_text)

        return markdown_text.strip()

    def _is_natural_break(self, line: str) -> bool:
        """Check if line represents a natural paragraph break."""
        # Sentence endings followed by capital letters
        if re.search(r'[.!?]\s+[A-Z]', line):
            return True

        # Question or exclamation at start
        if line.strip().startswith(('What', 'How', 'Why', 'When', 'Where', 'Who')):
            return True

        # Transition words/phrases
        transitions = ['However', 'Meanwhile', 'Furthermore', 'In addition', 'On the other hand', 'First', 'Second', 'Finally']
        if any(line.strip().startswith(trans) for trans in transitions):
            return True

        return False


# Convenience function
def convert_transcript_to_markdown(
    input_file: Union[str, Path],
    output_file: Optional[Union[str, Path]] = None,
    paragraph_min_words: int = 15,
    preserve_speaker_labels: bool = True
) -> Dict[str, Any]:
    """
    Convert a transcript file to clean markdown format.

    Args:
        input_file: Path to input transcript file (.vtt, .srt, .ttml, .txt)
        output_file: Path for output markdown file (auto-generated if None)
        paragraph_min_words: Minimum words per paragraph
        preserve_speaker_labels: Whether to preserve speaker labels

    Returns:
        Dictionary with conversion results and metadata
    """
    converter = TranscriptConverter()
    return converter.convert_to_markdown(
        input_file, output_file, paragraph_min_words, preserve_speaker_labels
    )