notes = {"до": "до-о",
         "ре": "ре-э",
         "ми": "ми-и",
         "фа": "фа-а",
         "соль": "со-оль",
         "ля": "ля-а",
         "си": "си-и"}
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


# class is_long:
#     def __init__(self, long=False):
#         self.long = long

class Note:
    def __init__(self, note, is_long=False):
        self.note = note
        self.is_long = is_long
        if self.is_long:
            self.note_ind = LONG_PITCHES.index(notes[note])
        else:
            self.note_ind = PITCHES.index(note)

    def __str__(self):
        if self.is_long:
            return notes[self.note]
        else:
            return self.note

    def __eq__(self, other):
        return self.note_ind == other.note_ind

    def __ne__(self, other):
        return self.note_ind != other.note_ind

    def __gt__(self, other):
        return self.note_ind > other.note_ind

    def __lt__(self, other):
        return self.note_ind < other.note_ind

    def __ge__(self, other):
        return self.note_ind >= other.note_ind

    def __le__(self, other):
        return self.note_ind <= other.note_ind

    def __lshift__(self, other):
        if self.is_long:
            if self.note_ind - other < 0:
                return LONG_PITCHES[len(LONG_PITCHES) - 1 + self.note_ind - other]
            else:
                return LONG_PITCHES[self.note_ind - other]
        else:
            if self.note_ind + other < 0:
                return PITCHES[len(PITCHES) - 1 + self.note_ind - other]
            else:
                return PITCHES[self.note_ind - other]

    # Двоичный
    # сдвиг
    # влево, оператор <<.

    def __rshift__(self, other):
        if self.is_long:
            if self.note_ind + other > len(LONG_PITCHES) - 1:
                return LONG_PITCHES[self.note_ind + other - len(LONG_PITCHES)]
            else:
                return LONG_PITCHES[self.note_ind + other]
        else:
            if self.note_ind + other > len(PITCHES) - 1:
                return PITCHES[self.note_ind + other - len(PITCHES)]
            else:
                return PITCHES[self.note_ind + other]

    # Двоичный
    # сдвиг
    # вправо, оператор >>.

    def get_interval(self, other):
        if other.note_ind > self.note_ind:
            return INTERVALS[other.note_ind - self.note_ind]
        else:
            return INTERVALS[self.note_ind - other.note_ind]


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


fa1 = Note("фа", True)
fa2 = Note("фа")
print(fa1 == fa2)
print(fa1 > fa2)
print(fa1 < fa2)
print(fa1 <= fa2)

la = Note("ля", True)
print(fa1 < la)

fa2 = Note("фа")
la = Note("ля", True)
print(la >> 1)
print(la >> 2)
x = fa2 << 4
print(x)

fa1 = Note("фа", True)
fa2 = Note("фа")
la = Note("ля", True)
print(la.get_interval(fa1))
print(fa1.get_interval(fa2))
print(fa1.get_interval(Note('си')))
