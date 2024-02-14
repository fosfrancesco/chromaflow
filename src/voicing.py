#make a class of voicing

class Voicing:
    
    
    #define the class
    def __init__(self):
        self.natures = {'maj', 'm', 'm6', 'm7', 'dom_7', 'maj7', 'o7', 'o', 'sus', 'sus2', 'sus7', 'ø7', 'power', 'm_maj7'}
        self.alter = {'add #11', 'add #5', 'add #7', 'add #9', 'add 13', 'add 2', 'add 5', 'add 6', 'add 7', 'add 8', 'add 9', 'add b13', 'add b2', 'add b6', 'add b9', 'alter #11', 'alter #5', 'alter #7', 'alter #9', 'alter b5', 'alter b9'}

        self.structural_elements = {'.', '|', ':|', '|:', '/', 'N.C.'} #to add the maj token 

        self.voicing = ['v_0', 'v_1', 'v_2', 'v_3']

        self.all_notes = {
            'C': 48, 'C#': 49, 'Db': 49, 'D': 50, 'D#': 51, 'Eb': 51, 'E': 52, 'F': 53, 'F#': 54, 'Gb': 42, 'G': 43, 'G#': 44, 'Ab':44, 'A': 45, 'A#': 46, 'Bb': 46, 'B': 47, 
            'A##': 47, 'Abb': 43, 'Abbb': 42, 'B#': 48, 'B##': 49, 'Bbb': 45, 'Bbbb': 44, 
            'C#': 49, 'C##': 50, 'C###': 51, 'Cb': 59, 'Cbb': 58, 'D##': 52, 'Dbb': 48, 'Dbbb': 47, 'E##': 54, 'Ebb': 50, 'Ebbb': 49, 
            'F##': 55, 'F###': 56, 'Fb': 52, 'Fbb': 51, 'G##': 45, 'Gb': 42, 'Gbb': 41
            }
        
        #define voicing for natures
        self.maj = {'v_0':[0, 7, 12, 16], 'v_1':[0, 7, 16, 19], 'v_2':[0, 4, 7, 12], 'v_3':[0, 7, 16, 19]}
        self.maj7 = {'v_0':[0, 11, 14, 16, 19], 'v_1':[0, 11, 16, 19], 'v_2':[0, 11, 14, 16], 'v_3':[0, 11, 14, 16, 19]}
        self.m = {'v_0':[0, 12, 15, 19], 'v_1':[0, 15, 19, 24], 'v_2':[0, 19, 24, 27], 'v_3':[0, 12, 19, 24, 27]}
        self.m7 = {'v_0':[0, 10, 15, 19], 'v_1':[0, 7, 10, 15], 'v_2':[0, 10, 14, 15], 'v_3':[0, 10, 14, 15]}
        self.dom_7 = {'v_0':[0, 7, 10, 16, 19], 'v_1':[0, 10, 16, 19], 'v_2':[0, 10, 14, 16], 'v_3':[0, 10, 14, 16, 19]}
        self.ø7 =  {'v_0':[0, 15, 18, 22], 'v_1':[0, 10, 15, 18], 'v_2':[0, 15, 18, 22, 24], 'v_3':[0, 6, 10, 15, 18]}
        self.o7 = {'v_0':[0, 15, 18, 21], 'v_1':[0, 15, 18, 21, 24], 'v_2':[0, 18, 21, 24, 27], 'v_3':[0, 12, 15, 18, 21]}
        self.sus = {'v_0':[0, 12, 17, 19], 'v_1':[0, 17, 19, 24], 'v_2':[0, 19, 24, 29], 'v_3':[0, 12, 19, 24, 29]} 
        self.sus7 = {'v_0':[0, 10, 17, 19], 'v_1':[0, 10, 14, 17, 19], 'v_2':[0, 10, 14, 17], 'v_3':[0, 10, 14, 17, 19]}
        self.sus2 = {'v_0':[0, 14, 19, 24], 'v_1':[0, 12, 19, 24, 26], 'v_2':[0, 19, 24, 26], 'v_3':[0, 12, 19, 24, 26]}

        # Define the voicing dictionaries
        self.chord_voicing = {'maj': self.maj, 'maj7': self.maj7, 'm': self.m, 'm7': self.m7, 'dom_7': self.dom_7, 'ø7': self.ø7, 'o7': self.o7, 'sus': self.sus, 'sus7': self.sus7, 'sus2': self.sus2}
    
    def add_maj_token(self, sequence):
        new_sequence = []
        for song in sequence:
            new_song = []
            for i in range(len(song)):
                element = song[i]
                new_song.append(element)
                if element in self.all_notes.keys() and (i == len(song) - 1 or song[i + 1] in self.structural_elements 
                                                         or song[i + 1].startswith('Form_')) and song[i-1] != '/':
                    new_song.append('maj')
            new_sequence.append(new_song)
        
        return new_sequence