Arguments for python script:
`python3 wordle.py <word_pattern_correct_possition> <word_pattern_incorrect_position> <letters_not_present> <letters_present> <words_file>`

Example:
`python3 wordle.py .lock l.... headsunhb 0 words_alpha.txt`
That means the word ends with `lock`, doesn't have the `L` in the first position, doesn't have the letters `HEADSUNHB`, was not passed any present letters and the file containing the list of words is `words_alpha.txt`.
