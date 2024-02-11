from utils import *
from formats import *
import xml.etree.ElementTree as ET

def repleaceTheseChords(mySequence, verbose = False):
    sequence = []
    correct_this = {
        "9sus4 add 4 subtract 3 add b9 add 4 subtract 3 add b9 alter #5": "sus add b2 add 8",
        "7 add 4 subtract 3 add b9 add 4 subtract 3 add b9 alter #5": "sus add b2 add 8",
        "7 add b9 add 4 subtract 3 add b9 add 4 subtract 3": "sus add b2 add 8",
        "13sus4 add 4 subtract 3 add b9 add 4 subtract 3": "sus add b2 add 8 add 6",
        "9sus4 add 4 subtract 3 add b9 add 4 subtract 3": "sus add b2 add 8",
        "7 add 4 subtract 3 add b9 add 4 subtract 3": "sus add b2 add 8",
        "13sus4 add 4 subtract 3 add 4 subtract 3": "sus add b2 add 6 add 8",
        "9sus4 add 4 subtract 3 add 4 subtract 3": "sus add 9",
        "9sus4 add 4 subtract 3 add #9 alter #5": "sus add b2 add 8",
        "9sus4 add 4 subtract 3 add b9 alter #5": "7 sus add b9",
        "9sus4 alter #5 add b9 add 4 subtract 3": "7 sus add 9",
        "7sus4 add 7 add b9 add 4 subtract 3": "7 sus",
        "13sus4 add 4 subtract 3 alter #11": "7 sus add 6",
        "13sus4 add 4 subtract 3 alter b9": "7 sus add 6",
        "13sus4 add 4 subtract 3 alter #5": "7 sus add 6",
        "9sus4 add 4 subtract 3 alter #5": "7 sus add 6 add 9",
        "13sus4 add 4 subtract 3 add #11": "7 sus add 6",
        "9sus4 alter b5 add 4 subtract 3": "7 sus add 6",
        "13sus4 add #11 add 4 subtract 3": "7 sus add 6",
        "13sus4 add 4 subtract 3 add b13": "7 sus add 6",
        "9sus4 alter #5 add 4 subtract 3": "7 sus add 9",
        "9sus4 add 4 subtract 3 alter b5": "7 sus add 9",
        "13sus4 add 4 subtract 3 add #9": "7 sus add 6 add 9",
        "9sus4 add 4 subtract 3 add #11": "7 sus add 9",
        "13sus4 add 4 subtract 3 add b9": "7 sus add b2 add 8 add 6",
        "9sus4 add 4 subtract 3 add b9": "7 sus add b2 add 8",
        "13sus4 add 4 subtract 3 add 7": "7 sus add 6",
        "9sus4 add 4 subtract 3 add 9": "7 sus add 9",
        "7sus4 add 4 subtract 3 add 7": "7 sus",
        "m69 add 4 subtract 3 add 9": "7 sus add 6 add 9",
        "7 add #11 add b9 alter #11": "7 add #11 add b9",
        "13sus4 add 4 subtract 3": "7 sus add 6",
        "m69 add 9 add #7 add 9": "m7 add 9 alter #7",
        "9sus4 add 4 subtract 3": "7 sus add 9",
        "alter #5 add b9 sus": "7 sus alter #5 add b9",
        "add b9 sus add b9": "7 sus add b9",
        "add 4 subtract 3": "sus",
        "m69 add 9 add 9 add 9": "m7 add 6 add 9",
        "7alt alter b5 add #9": "7 alter b5 add #9",
        "7sus4 add 7 alter b9": "sus add b2 add 8",
        "m7 alter b5 alter b9": "m7 alter b5 add b9",
        "7 alter b9 alter #5": "7 alter b5 add b9",
        "maj9 add #11 add b9": "maj7 add 9 add #11",
        "m69 add 9 alter #5": "m6 add 9",
        "maj9 add #11 add 7": "maj7 add 9 add #11",
        "m69 add 9 alter b5": "m6 add 9",
        "7 alter b9 add b13": "7 add b9 add b13",
        "7 alter #11 add b9": "7 add b9 add #11",
        "69 add 9 alter b5": "6 add 9 alter b5",
        "69 alter b5 add 9": "6 add 9 alter b5",
        "69 add 9 alter #5": "6 add 9 alter b5",
        "maj9 add #11": "maj7 add 9 add #11",
        "7sus4 add 9 add 7": "7 sus add 9",
        "7sus4 add #11 add 7": "7 sus add #11",
        "7sus4 alter #5 add 7": "7 sus alter #5",
        "sus4 alter b5 add 7": "sus alter b5",
        "7sus4 add b13 add 7": "7 sus add b13",
        "add #11 add #9 add #11 add #9": "add #9 add #11",
        "add #11 add #11" : "add #11",
        "77 sus add 9": "7 sus add 9",
        "7sus4 add 7 add 7": "7 sus",
        "7sus4 add 7": '7 sus',
        "7susadd3": '7 sus',
        "9 sus alter #5": "7 sus",
        "add b9 add b9 add 9": "add b9",
        "7 sus add 7": '7 sus',
        "7 sus alter b5": "7 sus",
        "7 7 sus add b13": "7 add b13",
        "maj7 7 sus alter #5": "maj7",
        "maj7 sus add #11": "maj7 add #11",
        "*..........*": "",
        "13 sus alter #11": "sus add #11",
        "13 sus alter b9": "sus add b9",
        "9 7 sus add #11": "7 sus add #11",
        "alter b5 add b9 alter #5": "alter b5 add b9 add b13",
        "alter b5 alter b5 alter b5": "alter b5",
        "alter b5 add #9 alter #5": "alter b5 add #9 add b13",
        "dim(maj7)": "m7 alter #7",
        "add 9 add 9 add 9": "add 9",
        "add b9 add b9 add b9": "add b9",
        "add b9 add b9 alter #5": "add b9 alter #5",
        "add b9 add b9": "add b9",
        "add 9 add 9": "add 9",
        "alter b5 alter b5": "alter b5",
        "add #7 add #7": "add #7",
        "add #9 add #9": "add #9",
        "add b9 sus add b9 alter #5": "sus add b9 alter #5",
        "add b9 sus add b9": "sus add b9",
        "alter b5 sus": "sus alter b5",
        "add 7 add b9 sus": "7 sus add b9",
        "add b9 add 9": "add b9",
        "m69 add 9": "m6 add 9",
        " m(add9)": "m add 9",
        " *-add9*": "m add 9",
        "*7b5#5*": "7 alter b5",
        "alter #5 alter #5": "alter #5",
        "alter #5 alter b5": "alter b5",
        "alter b5 alter #5": "alter b5",
        "alter #5 sus": "7 sus alter #5",
        "alter #5 add b9 sus": "7 sus add b9 alter #5",
        "alter b5 add #9 add b9": "alter b5 add b9",
        "*sus4*": "7 sus",
        "maj13": "maj7 add 13",
        "*6#9*": "6 add #9",
        "*ø11*": "m7 alter b5",
        "*dim*": "dim7",
        "*mb9*": "m add b9",
        "*-add9*": "m add 9",
        "*mM7*": "m7 alter #7",
        "*-b5*": "m7 alter b5",
        "*6b5*": "6 add 9 alter b5",
        "7alt": "7 add #11 add b9",
        "7#5#9": "7 add #5 add #9",
        "m(add9)": "m add 9",
        "add b13 sus": "7 sus add b13",
        "add #11 sus": "7 sus add #11",
        "add b9 sus": "sus add b9",
        "add b9 sus add #9 alter #5": "sus add b9 alter #5",
        "7 7 sus add b9": "7 sus add b9",
        "*7+*": "maj7",
        "*m7*": "m7",
        "*-3*": "m",
        "maj9": "maj7 add 9",
        "-N3": "m",
        "*m*": "m",
        "*O*": "dim7",
        "-7s": "m7",
        "77": "7",
        "m7 sus": "m7",
        "**": "",
        "N.C.": ""
    }
    
    #for key, value in correct_this.items():
    #    print('translating', key, 'to', value)
    #    mySequence = np.vectorize(lambda x: x.replace(key, value))(mySequence)
    
    #keys = list(correct_this.keys())
    #values = list(correct_this.values())

    for song in tqdm(mySequence):
        tmp = []  
        for element in song:            
            for key, value in correct_this.items():
                if key in element:
                    if (verbose):
                        print(element, '-->', value)
                    element = element.replace(key, value)
                    break
            tmp.append(element)
        sequence.append(tmp)
    sequence = np.array(sequence, dtype=object) 
    
    x = 0
    for song in sequence:
        y = 0
        for chord in song:
            s = chord.split(' ')
            if len(s) >= 5:
                #print(x)
                if s[1]+s[2] == s[3]+s[4]:
                    #print(x, y, chord)
                    sequence[x][y]=s[0]+' '+s[1]+' '+s[2]
                    #print(sequence[x][y])
            y+=1
        x+=1
             
    return sequence

#------------------------------------------------------------------
def parse_info_from_XML(path):
    '''
    Populate a chord sequence and an offset sequence from a XML file
    '''
    chord_sequence_list = []
    offset_sequence_list = []
    meta_info_list = []
    
    for file in tqdm(os.listdir(path)):
    
        if (file == '.DS_Store'):
            continue
            
        song_path = path+'/'+file
        #print(song_path)
        
        meta_info = get_metadata(song_path)
        #print(meta_info)
        
        tree = ET.parse(song_path)
        root = tree.getroot()

        #possible_types = ['segno', 'rehearsal', 'coda', 'words']

        bar = '|'
        song_form = ''
        tone = ''
        coda = ''
        chord = ''
        nature = ''
        extension = ''
        slash = ''
        offset = 0
        the_chord_sequence = []
        the_offset_sequence = []

        #Division is the number of ticks per quarter note
        division = int(root.find('part').find('measure').find('attributes').find('divisions').text)
        #print(division)


        #define the Style
        style_token = '<style>'
        the_chord_sequence.append(style_token)
        the_offset_sequence.append(offset)
        the_chord_sequence.append(meta_info['style'])
        the_offset_sequence.append(offset)

        for measure in root.iter('measure'):
            #get the offset reference
            measure_number = int(measure.attrib.get('number'))
            #print(measure_number, '->', offset)
        
            #get the bars
            bar = '|'
            barline = measure.find('barline')
            if barline != None:
                repeat = barline.find('repeat')
                if repeat != None:
                    direction = repeat.attrib.get('direction')
                    if direction == 'forward':
                        bar = '|:'
                    
            #print(bar)
            the_chord_sequence.append(bar)
            the_offset_sequence.append(offset)
            #get the Form
            direction = measure.find('direction')
            if direction != None:
                direction_type = direction.find('direction-type')
                
                segno = direction_type.find('segno')
                if segno != None:
                    song_form = 'Form_Segno'
                    #print(song_form)
                    the_chord_sequence.append(song_form)
                    the_offset_sequence.append(offset)
                
                coda = direction_type.find('coda')
                if coda != None:
                    song_form = 'Form_Coda'
                    #print(song_form)
                    the_chord_sequence.append(song_form)
                    the_offset_sequence.append(offset)
                    
                form = direction_type.find('rehearsal')
                if form != None:
                    song_form = 'Form_'+form.text
                    #print(song_form)
                    the_chord_sequence.append(song_form)
                    the_offset_sequence.append(offset)
                    
            #get the repetition info
            barline = measure.find('barline')
            if barline != None:
                ending = barline.find('ending')
                if ending != None:
                    number = ending.attrib.get('number')
                    if number != None:
                        bar = 'Repeat_'+ str(number) #this section defines the bar to be repeated
                        #print(bar)
                        the_chord_sequence.append(bar)
                        the_offset_sequence.append(offset)
                            
            #get the chords
            for harmony in measure.iter('harmony'):
                root = harmony.find('root')
                note = root.find('root-step')
                sharp = root.find('root-alter')
                if sharp != None:
                    sharp = sharp.text
                    if sharp == '-1': #Remember to check double sharp and double flat
                        tone = 'b'
                    elif sharp == '1':
                        tone = '#'
                    elif sharp == '0':
                        tone = ''
                
                note = note.text+tone
                kind = harmony.find('kind')
                nature = kind.attrib.get('text')
                
                #get nature of the chord
                if nature == None:
                    nature = ''
                
                #get the extension
                degree = harmony.find('degree')
                extension = ''
                if degree != None:
                    for degree in measure.iter('degree'):
                        
                        degree_type = degree.find('degree-type').text
                        relatedNote = degree.find('degree-value').text
                        degree_sharp = degree.find('degree-alter').text
                        if degree_sharp == '-1':
                            relatedNote = 'b'+relatedNote
                        elif degree_sharp == '-2':
                            relatedNote = 'bb'+relatedNote
                        elif degree_sharp == '1':
                            relatedNote = '#'+relatedNote
                        elif degree_sharp == '2':
                            relatedNote = '##'+relatedNote
                            
                        extension += ' ' + degree_type + ' ' +relatedNote
                else:
                    extension = ''
                
                #get slash chord
                bass = harmony.find('bass')
                if bass != None:
                    bass_step = bass.find('bass-step')
                    slash = '/'+bass_step.text
                else :
                    slash = ''
                    
                chord = note + str(nature) + extension + str(slash)
                #print(chord)
                the_chord_sequence.append(chord)
            
            #get durations offset
            for note_element in measure.iter('note'):
                duration = int(note_element.find('duration').text) / division
                the_offset_sequence.append(offset)
                offset += duration
                #print(offset)
                
            #this second bar is relevant to close the section
            #Find all barline elements within the measure
            barlines = measure.findall('barline')

            # Iterate through barlines and extract information
            for barline in barlines:
                repeat = barline.find('repeat')
                if repeat != None:
                    direction = repeat.attrib.get('direction')
                    if direction == 'backward':
                        bar = ':|'
                        #print(bar)
                        the_chord_sequence.append(bar)
                        the_offset_sequence.append(offset)

        the_chord_sequence = np.array(the_chord_sequence, dtype=object)
        the_offset_sequence = np.array(the_offset_sequence, dtype=float)

        #print(the_chord_sequence.shape, the_offset_sequence.shape)

        #divide the chords into sections base, nature, extension, slash
        #the first two elements are the style 
        the_sequence = the_chord_sequence[2:]
        the_offset = the_offset_sequence[2:]

        format = the_chord_sequence[0:2].tolist()

        offset_format = the_offset_sequence[0:2].tolist()

        the_sequence, the_offset = getArrayOfElementsInChord(the_sequence, the_offset)
        the_offset = offset_format + the_offset
        the_sequence = format + the_sequence

        #adjust the offset sequence
        the_sequence = np.array(the_sequence, dtype=object)
        the_offset = np.array(the_offset, dtype=float)
        
        chord_sequence_list.append(the_sequence)
        offset_sequence_list.append(the_offset)
        meta_info_list.append(meta_info)
    
    chord_sequence_list = np.array(chord_sequence_list, dtype=object)
    offset_sequence_list = np.array(offset_sequence_list, dtype=object)
    meta_info_list = np.array(meta_info_list, dtype=object)
    
    print(chord_sequence_list.shape, offset_sequence_list.shape)
    return chord_sequence_list, offset_sequence_list, meta_info_list

#----------------------------------------------------------------------------------
#expand the song form
def expand_song_structure(song_structure, id = 0):
    status = True
    
    if '|:' not in song_structure:
        print('No repetition data found')
        print("-----------------------------\n")    
        return song_structure, status
    
    #convert numpy into array
    song_structure = song_structure.tolist()
    
    print('Length of sequence:', len(song_structure))
    #identify the location of the repetition symbols
    
    form_zone = {'start': 0, 'end': 0, id: 0}
    inner_zone = {'start': 0, 'end': 0, id: 0}
    #rest_zone = {'start': 0, 'end': 0, id: 0}
    
    
    #jump to the third element and save the prior information
    intro_data = song_structure[0:2]
    sequence = song_structure[2:]
    
    #get the location of the repetition symbols
    #find :| and Repeat_
    close = []
    repeat = []
    c_id = 0
    r_id = 0
    for i, e in enumerate(sequence):
        close_repetition = {'loc': 0, 'done': False, 'id': 0}
        repeat_section = {'loc': 0, 'done': False, 'id': 0}
        if e == ':|':
            close_repetition['loc'] = i
            close_repetition['id'] = c_id
            #print(close_repetition)
            close.append(close_repetition)
            c_id += 1
        if e.startswith('Repeat'):
            repeat_section['loc'] = i
            repeat_section['id'] = r_id
            #print(repeat_section)
            repeat.append(repeat_section)
            r_id += 1
    
    if len(repeat) == 1:
        # Substring to search for
        substring = 'Repeat_'

        # Find the index of the first element containing the substring
        index = next((i for i, element in enumerate(sequence) if substring in element), None)
        #erase the location element
        del sequence[index]
        
    #print(repeat, len(repeat))
    #Start the process
    stepper = 0
    copy_section = []
    repeat_times = 0
    control_loop = 0
    repeat_bar = 0
    
    #r_id = 0
    repeat_done = False
    done = True
    this_repeat = None
    next_repeat = None
    
    while done:
        #grab the element 
        e = sequence[stepper]
        #print(stepper, e)
        if e == '|:':
            form_zone['start'] = stepper  
        
        if e.startswith('Repeat') and repeat_done == False:
            #find the repeat that is located in that stepper
            for current in repeat:
            # Check if the 'loc' value of the current dictionary matches the stepper value
                if current['loc'] == stepper:
                    # If it matches, store the dictionary and break the loop
                    this_repeat = current
                    this_id = current['id']
                    break 
            #Ask if this repeat is done
            if this_repeat['done'] == False:
                inner_zone['start'] = stepper 
                id = this_repeat['id']   
                print('first repeat done', stepper, id)           
                #move forward
                stepper += 1
                e = sequence[stepper]
                repeat[id]['done'] = True
                
                #Ask which is the next available repeat? 
                for current in repeat:
                    if current['done'] == False:
                        next_repeat = current
                        print('next repeat:', next_repeat['loc'], next_repeat['id'])
                        break
                if (next_repeat == None):
                    print('All repetitions done 0')
                    done = False
                    break
            
            elif this_repeat['done'] == True and next_repeat['done'] == False and repeat[this_id]['id'] < len(repeat)-1:
                #jump to the next repeat jumping ':|', '|' and 'Repeat_'
                next_loc = next_repeat['loc'] + 1
                stepper = next_loc
                e = sequence[stepper]
                
                id_next = next_repeat['id']
                repeat[id_next]['done'] = True
                print('second repeat done at', 'stepper:', stepper, 'id:', id)
                
            elif repeat[repeat_times]['done'] == True and repeat[this_id]['id'] == len(repeat)-1:
                #repeat_done = True
                #TODO: check if this section is needed
                print('All repetitions done')
                #done = False #close the loop
                #e = 'None'
            
        
        if e == ':|':
            current = close[repeat_bar]
            #check the current repetition turn
            if current['done'] == True and repeat_bar < len(close)-1:
                repeat_bar += 1
                current = close[repeat_bar]
                #print('next close repetition')
            
            #do the repetition    
            if current['done'] == False:
                
                #save location 
                form_zone['end'] = stepper
                inner_zone['end'] = stepper
                
                #move to the original location
                stepper = form_zone['start'] + 1
                e = sequence[stepper]
                
                #update its information
                close[repeat_bar]['done'] = True  
                current['done'] = True    
                #print('repetition done', repeat_bar)
        
        #copy the information    
        copy_section.append(e)
        stepper += 1
        control_loop += 1
        if stepper == len(sequence):
            done = False
        if control_loop > 3000:
            print('ERROR: -----> Control loop break! \nid:', id)
            status = False
            return 0, status
    
    copy_section = intro_data + copy_section
    copy_section = [x.replace(':|', '|') for x in copy_section]
    copy_section = [x.replace('|:', '|') for x in copy_section]
    
    print('Process completed successfully..', 'New form length:', len(copy_section))
    print("-----------------------------\n")
    return copy_section, status 
#----------------------------------------------------------------------------------
def formatChordsVocabulary(theChordsSequence, theOffetsSequence, blockSize):
    chord_sequence_list = []
    offset_sequence_list = []
    i = 0
    for theChords, theOffets in zip(theChordsSequence, theOffetsSequence):
        theChords = np.array(theChords, dtype=object)
        theOffets = np.array(theOffets, dtype=float)
        
        #divide the chords into sections base, nature, extension, slash
        #the first two elements are the style 
        the_sequence = theChords[2:]
        the_offset = theOffets[2:]

        format = theChords[0:2].tolist()
        offset_format = theOffets[0:2].tolist()

        the_sequence, the_offset = getArrayOfElementsInChord(the_sequence, the_offset)
        the_offset = offset_format + the_offset
        the_sequence = format + the_sequence

        #the final format of the sequence is:
        the_sequence = format_start_end(the_sequence)
        the_offset = format_start_end(the_offset)
        
        #if (the_sequence.shape[0] > 768):
        #    print(i, the_sequence.shape[0], the_offset.shape[0], format)
        
        the_sequence = padding(the_sequence, blockSize)
        the_offset = padding(the_offset, blockSize)
        
        chord_sequence_list.append(the_sequence)
        offset_sequence_list.append(the_offset)
        i+=1
            
    chord_sequence_list = np.array(chord_sequence_list, dtype=object)
    offset_sequence_list = np.array(offset_sequence_list, dtype=object)
    print(chord_sequence_list.shape, offset_sequence_list.shape)
    return chord_sequence_list, offset_sequence_list


def correctDuplicatedExtensions(dataset, offset):
    corrected_datset = []
    corrected_offset = []
    #i = 0
    for song, off in zip(dataset, offset):
        cleaned_list = []
        cleanned_offset = []
        for chord, ofNum in zip(song, off):
            new = []
            s = chord.split(' ')
            if len(s) >= 2 and len(s) % 2 == 0:
                tmp = s[0] + ' ' + s[1]
                new.append(tmp)
                for i in range(2, len(s), 2):
                    r = s[i]+ ' ' + s[i+1]
                    if tmp != r:
                        new.append(r)
                        
            else:
                new.append(chord)
            
            new = ' '.join(new)
            cleaned_list.append(new)
            cleanned_offset.append(ofNum)
        #i+=1
        corrected_datset.append(cleaned_list)
        corrected_offset.append(cleanned_offset)
    corrected_datset = np.array(corrected_datset, dtype=object)
    corrected_offset = np.array(corrected_offset, dtype=object)
    print(corrected_datset.shape, corrected_offset.shape)
    return corrected_datset, corrected_offset

#----------------------------------------------------------------------------
#Chel for all chords that can not be read by music21
def checkIncompatibleChords(data):
    #save all chords not compatible with music21
    incompatible_chords = []
    s_id = 0
    for songs in tqdm(data):
        #let's pass the starting and style elements
        for i in range(len(songs)):
            element = songs[i]
            if element.find('b') > 0 and element[1:2] == 'b':
                element = element[0:1] + '-' + element[2:]
            try:
                tmp = m21.harmony.ChordSymbol(element)
            except:
                #erase the first character
                print(s_id, element)
                if element[1:2] == '-' or element[1:2] == '#':
                    element = element[2:]
                else:
                    element = element[1:]
                if element.find('/'):
                    s = element.split('/')
                    element = s[0]
                incompatible_chords.append(element)
        s_id += 1

    incompatible_chords = list(set(incompatible_chords))
    print(incompatible_chords)
    return incompatible_chords