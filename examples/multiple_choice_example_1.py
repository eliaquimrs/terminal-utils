from terminal_utils.choices_via_terminal import ChoicesViaTerminal

LIST_OF_CHOICES = [
    'Option 1',
    'Option 2',
    'Option 3',
    'Option 4',
    'Option 5'
]
TITTLE = 'Choose an option'
response = ChoicesViaTerminal(TITTLE, LIST_OF_CHOICES,
                              mode='multiple_choices').main()

print('')
for chosen_option_index, chosen_option_text in response:
    print(
        '- Chosen option index: {}|Chosen option text: {}'.format(chosen_option_index,
                                                            chosen_option_text)
    )
