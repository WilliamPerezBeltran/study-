=begin
	Escape characters

	Escape characters allow you to type in representations of whitespace characters and 
	to include quotation marks inside your string without accidentally ending it. 
	As a reminder, escape characters only work inside double quotation marks.
=end

=begin

\\  #=> Need a backslash in your string?
\b  #=> Backspace
\r  #=> Carriage return, for those of you that love typewriters
\n  #=> Newline. You'll likely use this one the most.
\s  #=> Space
\t  #=> Tab
\"  #=> Double quotation mark
\'  #=> Single quotation mark

=end

puts "hello \n\n hello"