notes = {"до": "до-о",
         "ре": "ре-э",
         "ми": "ми-и",
         "фа": "фа-а",
         "соль": "со-оль",
         "ля": "ля-а",
         "си": "си-и"}
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


# class is_long:
#     def __init__(self, long=False):
#         self.long = long

class Note:
    def __init__(self, note, is_long=False):
        self.note = note
        self.is_long = is_long

    def __str__(self):
        if self.is_long:
            return notes[self.note]
        else:
            return self.note


class LoudNote(Note):
    def __str__(self):
        if self.is_long:
            return notes[self.note].upper()
        else:
            return self.note.upper()


class NoteWithOctave(Note):
    def __init__(self, note, octa, is_long=False):
        super(NoteWithOctave, self).__init__(octa)
        self.is_long = is_long
        self.octa = octa
        self.note = note

    def __str__(self):
        if self.is_long:
            return f"{notes[self.note]} ({self.octa})"
        return f"{self.note} ({self.octa})"


class DefaultNote(Note):
    def __init__(self, note="до", is_long=False):
        super(DefaultNote, self).__init__(note)
        self.note = note
        self.is_long = is_long
