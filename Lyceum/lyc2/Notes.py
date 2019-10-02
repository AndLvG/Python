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
N = 7


class Note:
    def __init__(self, note, is_long=False):
        self.note = note
        self.is_long = is_long
        if self.is_long:
            self.note_ind = LONG_PITCHES.index(notes[note])
            self.real_name = notes[self.note]
        else:
            self.note_ind = PITCHES.index(note)
            self.real_name = self.note

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
        ind = self.note_ind - other
        while ind < 0:
            ind = len(LONG_PITCHES) + self.note_ind - other
            other -= N

        if self.is_long:
            return Note(PITCHES[ind], True)
        else:
            return Note(PITCHES[ind])

    # Двоичный    сдвиг    влево, оператор <<.

    def __rshift__(self, other):
        ind = self.note_ind + other
        while ind > N - 1:
            ind = self.note_ind + other - N
            other -= N

        if self.is_long:
            return Note(PITCHES[ind], True)
        else:
            return Note(PITCHES[ind])

    # Двоичный сдвиг вправо, оператор >>.

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


class Melody:
    def __init__(self, *args):
        self.Notes_list = []
        if len(args) > 0:
            for arg in args[0]:
                self.Notes_list.append(arg)

    def __str__(self):
        ret = ''
        for n in self.Notes_list:
            ret += f'{n.real_name}, '
        ret = ret[0:-2]
        return ret.capitalize()

    def replace_last(self, new_note):
        self.Notes_list[-1] = new_note

    def remove_last(self):
        self.Notes_list = self.Notes_list[:-1]

    def append(self, new_note):
        self.Notes_list.append(new_note)

    def __len__(self):
        return len(self.Notes_list)

    def clear(self):
        self.Notes_list.clear()

    def __lshift__(self, other):
        melod = Melody()
        for note in self.Notes_list:
            if note.note_ind - other >= 0:
                melod.append(note << other)
            else:
                return self
        return melod

    def __rshift__(self, other):
        melod = Melody()
        for note in self.Notes_list:
            if note.note_ind + other < N:
                melod.append(note >> other)
            else:
                return self
        return melod


melody = Melody([Note('ля'), Note('соль'), Note('ми'), Note('до', True)])
print(melody)
print(Melody() >> 2)
melody_up = melody >> 1
melody_down = melody << 1
melody.replace_last(Note('соль'))
print('>> 1:', melody_up)
print('<< 1:', melody_down)
print(melody)
