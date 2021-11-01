# Translation for HeschyApps.

def translate(word, args):

	if(len(args) == 0): return '[An Error occured in translation progress]';

	for i in range(len(args)):
		args[i] = '(' + str(args[i]) + ')';

	temp = '';
	for i in range(len(args)):
		temp += args[i];

	args = temp;

	if args != '(noargs)': word = args + word;

	if   word == 'unbekannt': return 'unknown';
	elif word == 'Unbekannt': return 'Unknown';
	elif word == '(LOWERCASE)Klasse': return 'class';
	elif word == '(UPPERCASE)Klasse': return 'Class';
	elif word == '(LOWERCASE)Raumschiff': return 'spaceship';
	elif word == '(UPPERCASE)Raumschiff': return 'Spaceship';
	elif word == '(LOWERCASE)Sternenschiff': return 'starship';
	elif word == '(UPPERCASE)Sternenschiff': return 'Starship';
	elif word == 'MHN': return 'EMH';
	elif word == '(LOWERCASE)(COMPLETE)MHN': return 'Emergency Medical Holographic program';
	elif word == '(UPPERCASE)(COMPLETE)MHN': return 'Emergency Medical Holographic program';
	elif word == '(LOWERCASE)Notfall': return 'emergency';
	elif word == '(UPPERCASE)Notfall': return 'Emergceny';
	else: return word;
	