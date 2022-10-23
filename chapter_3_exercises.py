names = ['emin','yusa','yusuf','melih','unal']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

n = 0
while n < 5:
	message = f"Hello dear {names[n].title()}."
	print(message)
	n += 1
print("You all welcome to Python Crash Course.")

universities = ['durham', 'manchester', 'newcastle' , "king's college london", 'queen marry']
message = f"I hope I'll become a student at the university of {universities[0].title()} soon."
print(message)

#Chapter 3.4

guest_list = ['messi','ronaldo','neymar','yazici']
print(f"Dear {guest_list[0].title()}, the honor of your presence is requested for dinner on Saturday,Third September 2022 at seven in the evening at Eyuboglu Mention, London, United Kingdom.")
print(f"Dear {guest_list[1].title()}, the honor of your presence is requested for dinner on Saturday,Third September 2022 at seven in the evening at Eyuboglu Mention, London, United Kingdom.")
print(f"Dear {guest_list[2].title()}, the honor of your presence is requested for dinner on Saturday,Third September 2022 at seven in the evening at Eyuboglu Mention, London, United Kingdom.")
print(f"Dear {guest_list[3].title()}, the honor of your presence is requested for dinner on Saturday,Third September 2022 at seven in the evening at Eyuboglu Mention, London, United Kingdom.")

unfortunate_absence = guest_list.pop(1)
print(f"Due to unexpected events, Dear {unfortunate_absence.title()} won't be able to attend the event. I wish my best to him.")
