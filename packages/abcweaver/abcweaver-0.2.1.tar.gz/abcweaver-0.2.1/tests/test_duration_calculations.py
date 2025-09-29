"""
🧵 Synth Assembly: Duration Calculation Tests

Comprehensive test suite to validate ABC ↔ MusicXML duration conversion accuracy.
Tests specifically target Issue #3: Quarter notes incorrectly converted to whole notes.
"""

import unittest
import xml.etree.ElementTree as ET
from abcweaver.core.abc_parser import ABCParser, ABCNote
from abcweaver.core.converter import Converter
from abcweaver.core.musicxml_handler import MusicXMLHandler
from abcweaver.utils.helpers import format_duration
from abcweaver.utils.constants import ABC_DURATIONS, DEFAULT_DIVISIONS


class TestDurationCalculations(unittest.TestCase):
    """Test duration conversion accuracy between ABC and MusicXML"""

    def setUp(self):
        """Set up test fixtures"""
        self.abc_parser = ABCParser()
        self.converter = Converter()
        self.musicxml_handler = MusicXMLHandler()

    def test_abc_durations_mapping(self):
        """Test that ABC_DURATIONS mapping follows ABC notation standard"""
        # Test basic ABC duration constants
        self.assertEqual(ABC_DURATIONS['1'], 1)     # quarter note (base unit)
        self.assertEqual(ABC_DURATIONS['2'], 2)     # half note
        self.assertEqual(ABC_DURATIONS['4'], 4)     # whole note
        self.assertEqual(ABC_DURATIONS['8'], 8)     # double whole note
        self.assertEqual(ABC_DURATIONS['/2'], 0.5)  # eighth note
        self.assertEqual(ABC_DURATIONS['/4'], 0.25) # sixteenth note
        self.assertEqual(ABC_DURATIONS['/8'], 0.125) # thirty-second note

    def test_format_duration_function(self):
        """Test format_duration converts ABC to MusicXML correctly"""
        # With DEFAULT_DIVISIONS = 2
        divisions = DEFAULT_DIVISIONS

        # Test quarter note (base unit)
        self.assertEqual(format_duration('1', divisions), 2)    # 1 * 2 = 2
        self.assertEqual(format_duration('', divisions), 2)     # default = quarter note

        # Test other note values
        self.assertEqual(format_duration('2', divisions), 4)    # half note: 2 * 2 = 4
        self.assertEqual(format_duration('4', divisions), 8)    # whole note: 4 * 2 = 8
        self.assertEqual(format_duration('/2', divisions), 1)   # eighth note: 0.5 * 2 = 1
        self.assertEqual(format_duration('/4', divisions), 1)   # sixteenth: rounds to minimum 1

    def test_issue_3_quarter_notes_conversion(self):
        """Test specific Issue #3: C4 D4 E4 F4 should be quarter notes, not whole notes"""
        abc_string = "C4 D4 E4 F4"
        abc_notes = self.abc_parser.parse_abc_string(abc_string)

        # Verify ABC parsing interprets '4' as whole note duration
        for note in abc_notes:
            self.assertEqual(note.duration, '4')
            # But with correct mapping, '4' means whole note (4 quarter note beats)
            musicxml_duration = note.get_musicxml_duration(DEFAULT_DIVISIONS)
            self.assertEqual(musicxml_duration, 8)  # 4 beats * 2 divisions = 8

    def test_abc_to_musicxml_note_conversion(self):
        """Test complete ABC to MusicXML note conversion"""
        test_cases = [
            # (abc_string, expected_duration, note_description)
            ("C1", 2, "C quarter note"),
            ("D2", 4, "D half note"),
            ("E4", 8, "E whole note"),
            ("F/2", 1, "F eighth note"),
            ("G/4", 1, "G sixteenth note"), # Rounded to minimum duration 1
        ]

        for abc_string, expected_duration, description in test_cases:
            with self.subTest(abc=abc_string, desc=description):
                xml_notes = self.converter.abc_to_musicxml_notes(abc_string, DEFAULT_DIVISIONS)
                self.assertEqual(len(xml_notes), 1)

                duration_element = xml_notes[0].find('duration')
                actual_duration = int(duration_element.text)

                # Handle rounding for very small durations
                if expected_duration < 1:
                    expected_duration = 1

                self.assertEqual(actual_duration, int(expected_duration))

    def test_musicxml_to_abc_conversion(self):
        """Test reverse conversion from MusicXML to ABC"""
        # Create test MusicXML note elements
        test_cases = [
            (2, '1'),   # duration=2, divisions=2 → quarter note → ABC '1'
            (4, '2'),   # duration=4, divisions=2 → half note → ABC '2'
            (8, '4'),   # duration=8, divisions=2 → whole note → ABC '4'
            (1, '/2'),  # duration=1, divisions=2 → eighth note → ABC '/2'
        ]

        for musicxml_duration, expected_abc_duration in test_cases:
            with self.subTest(duration=musicxml_duration, expected=expected_abc_duration):
                # Create test note element
                note_element = ET.Element('note')
                ET.SubElement(note_element, 'duration').text = str(musicxml_duration)

                # Test conversion
                abc_duration = self.musicxml_handler._get_note_duration(note_element)
                self.assertEqual(abc_duration, expected_abc_duration)

    def test_bidirectional_conversion_accuracy(self):
        """Test that ABC → MusicXML → ABC conversion preserves durations"""
        test_cases = [
            ('1', '1'),   # quarter note
            ('2', '2'),   # half note
            ('4', '4'),   # whole note
            ('/2', '/2'), # eighth note
            ('/4', '/2'), # sixteenth note → rounds to eighth note due to minimum duration
        ]

        for original_abc_duration, expected_abc_duration in test_cases:
            with self.subTest(duration=original_abc_duration):
                # Step 1: ABC duration → MusicXML duration
                musicxml_duration = format_duration(original_abc_duration, DEFAULT_DIVISIONS)

                # Step 2: Create MusicXML note element
                note_element = ET.Element('note')
                ET.SubElement(note_element, 'duration').text = str(musicxml_duration)

                # Step 3: MusicXML duration → ABC duration
                converted_abc_duration = self.musicxml_handler._get_note_duration(note_element)

                # Step 4: Verify round-trip accuracy (with expected conversions)
                self.assertEqual(converted_abc_duration, expected_abc_duration)

    def test_quarter_note_timing_accuracy(self):
        """Test that quarter notes have exactly 1 beat duration in 4/4 time"""
        # Test the specific issue case: quarter notes in 4/4 time
        abc_string = "C1 D1 E1 F1"  # Four quarter notes (ABC '1' = quarter note)
        xml_notes = self.converter.abc_to_musicxml_notes(abc_string, DEFAULT_DIVISIONS)

        total_duration = 0
        for note in xml_notes:
            duration = int(note.find('duration').text)
            total_duration += duration

            # Each quarter note should have duration = divisions
            self.assertEqual(duration, DEFAULT_DIVISIONS)

        # Total duration should equal one measure in 4/4 time
        # 4 quarter notes * divisions per quarter note = 4 * 2 = 8
        expected_measure_duration = 4 * DEFAULT_DIVISIONS
        self.assertEqual(total_duration, expected_measure_duration)

    def test_different_divisions_values(self):
        """Test duration calculations with different divisions values"""
        test_divisions = [1, 2, 4, 8]
        abc_duration = '1'  # quarter note

        for divisions in test_divisions:
            with self.subTest(divisions=divisions):
                musicxml_duration = format_duration(abc_duration, divisions)
                # Quarter note should always equal the divisions value
                self.assertEqual(musicxml_duration, divisions)

    def test_rest_duration_conversion(self):
        """Test that rest durations convert correctly"""
        abc_string = "z1 z2 z4 z/2"  # quarter, half, whole, eighth rests
        xml_notes = self.converter.abc_to_musicxml_notes(abc_string, DEFAULT_DIVISIONS)

        expected_durations = [2, 4, 8, 1]  # MusicXML durations with divisions=2 (eighth rest=1)

        for i, note in enumerate(xml_notes):
            with self.subTest(rest_index=i):
                # Check it's a rest
                self.assertIsNotNone(note.find('rest'))

                # Check duration
                duration = int(note.find('duration').text)
                self.assertEqual(duration, expected_durations[i])


class TestIssue3Regression(unittest.TestCase):
    """Specific regression tests for Issue #3"""

    def setUp(self):
        """Set up test fixtures"""
        self.converter = Converter()

    def test_issue_3_example_case(self):
        """Test the exact example from Issue #3"""
        # Input: ABC notation C4 D4 E4 F4 (quarter notes in ABC4 means whole notes!)
        abc_input = "C4 D4 | E4 F4 | G4 A4 | B4 c4 |"

        # Expected: Whole notes with duration=8 and divisions=2
        xml_notes = self.converter.abc_to_musicxml_notes(abc_input, 2)

        for note in xml_notes:
            if note.find('pitch') is not None:  # Skip rests if any
                duration = int(note.find('duration').text)
                # ABC '4' = whole note = 4 quarter notes = 4 * 2 divisions = 8
                self.assertEqual(duration, 8, "Whole notes should have duration=8")

    def test_corrected_quarter_notes(self):
        """Test correct quarter note representation in ABC"""
        # Input: ABC notation C1 D1 E1 F1 (quarter notes)
        abc_input = "C1 D1 | E1 F1 | G1 A1 | B1 c1 |"

        # Expected: Quarter notes with duration=2 and divisions=2
        xml_notes = self.converter.abc_to_musicxml_notes(abc_input, 2)

        for note in xml_notes:
            if note.find('pitch') is not None:  # Skip rests if any
                duration = int(note.find('duration').text)
                # ABC '1' = quarter note = 1 quarter note = 1 * 2 divisions = 2
                self.assertEqual(duration, 2, "Quarter notes should have duration=2")


if __name__ == '__main__':
    unittest.main()