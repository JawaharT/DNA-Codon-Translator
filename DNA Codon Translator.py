import tkinter as tk
from tkinter import messagebox
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import seq3


#Updates user entered sequence in the GUI
def nucleotide_entered(nucleotide):
    '''The DNA base (nucleotide) entered by user is added to new sequence or adds to
    existing sequence.

    Parameters
    __________
    nucleotide: str, not optional
        The user entered DNA base.

    Return
    ______
    updated sequence to user's UI.'''
    
    if sequence_text.get() != "Enter Sequence":
        sequence_text.set(sequence_text.get() + nucleotide)
    else:
        sequence_text.set(nucleotide)


#Converts the DNA sequence entered by the user
def get_protein():
    ''' Translates DNA sequence entered by user.
    Parameters
    __________
    No parameters only global variable sequence_text required.

    Return
    ______
    Separate showinfo box with converted amino acid sequence.'''

    str_sequence_text = str(sequence_text.get())
    if (((len(str_sequence_text)) % 3) == 0) and (len(str_sequence_text) != 0):
        dna = Seq(str_sequence_text, IUPAC.unambiguous_dna)
        mrna = dna.transcribe()
        protein = mrna.translate()
        three_letter_aa = str(seq3(protein))
        new_dashed_3_letter_aa = ""
        for index,letter in enumerate(three_letter_aa):
            if (index % 3 == 0) and (index != 0):
                new_dashed_3_letter_aa += "-"
            new_dashed_3_letter_aa += letter
        messagebox.showinfo("!", "Final Converted Protein is: " + new_dashed_3_letter_aa)
    else:
        messagebox.showerror("!", "Sequence needs to be a multiple of 3 or sequence should not be 0.")


#Deletes the latest nucletide entered in the sequence
def backspace():
    '''Removes the last entered DNA base in sequence.

    Parameters
    __________
    No sepecifc parameter other than global variable sequence_text.

    Returns
    ______
    new sequence with only last entered DNA base removed.'''
    
    return sequence_text.set(str(sequence_text.get())[:-1])


#The main GUI control centre
def main():        
    global sequence_text
    
    root = tk.Tk()
    frame = tk.Frame(root)
    root.title('DNA Codon to Amino Acid Translator')
    frame.pack()

    sequence_text, protein_text = tk.StringVar(frame), tk.StringVar(frame, value = "Converted Protein")
    tk.Label(frame, text = "Sequence: ").pack(side = "top")
    sequence_label = tk.Label(frame, textvariable = sequence_text).pack(side = "top")
    
    A_button = tk.Button(frame, text = "Adenine", fg = "red", command = lambda: nucleotide_entered("A")).pack(side = "left", pady = 10, padx = 10)
    G_button = tk.Button(frame, text = "Guanine", fg = "green", command = lambda: nucleotide_entered("G")).pack(side = "left", pady = 10, padx = 10)
    C_button = tk.Button(frame, text = "Cytosine", fg = "blue", command = lambda: nucleotide_entered("C")).pack(side = "left", pady = 10, padx = 10)
    T_button = tk.Button(frame, text = "Thymine", fg = "brown", command = lambda: nucleotide_entered("T")).pack(side = "left", pady = 10, padx = 10)
    
    sequence_confirmed_button = tk.Button(frame, text = "Confirm Sequence", fg = "black", command = get_protein).pack(side = "right", pady = 10, padx = 10)

    #Resets the sequence to empty string
    reset_button = tk.Button(frame, text = "Reset", fg = "orange", command = lambda: sequence_text.set("")).pack(side = "right", pady = 10, padx = 10)
    backspace_button = tk.Button(frame, text = "<--", fg = "orange", command = backspace).pack(side = "right", pady = 10, padx = 10)

    root.mainloop()


if __name__ == '__main__':
    main()
