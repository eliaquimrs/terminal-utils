from terminal_utils.choices_via_terminal import ChoicesViaTerminal

LIST_OF_CHOICES = [
    'Option 1',
    'Option 2',
    'Option 3',
    'Option 4',
    'Option 5'
]
TITTLE = 'Choose an option'
response = ChoicesViaTerminal(TITTLE, LIST_OF_CHOICES).main()
chosen_option_index, chosen_option_text = response[0]

print()
print('Chosen option index: {}\n'
      'Chosen option text: {}'.format(chosen_option_index, chosen_option_text))
