File.readlines('titles.txt').each_with_index do |title,index|
	if index < 10
		index = "0#{index}"
	end
	title = title
	file_to_save = File.new("#{index}_#{title.capitalize.strip.tr(" ", "_")}.html",'w+')
	file_to_save.puts("<!DOCTYPE html>
						<html>
							<head>
								<title>my website</title>
							</head>
							<body>
							
							</body>
							<footer>
								<p>copy right</p>
							</footer>
						</html>")
	file_to_save.close
end