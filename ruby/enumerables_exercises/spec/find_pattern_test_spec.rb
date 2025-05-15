require "spec_helper"

require_relative "../find/find_pattern_test.rb"

describe "select pattern test" do 
	context "test_capitalize" do 
		let(:obje) {FindPatternTest.new}

		it "test_pick_even_numbers" do 
			# expect(obje.test_find_first_seven_letter_word).to match("unicorn")
			expect(obje.test_find_first_seven_letter_word).to eq "unicorn"
		end 

		it "test_no_waldo" do 
			expect(obje.test_no_waldo).to eq nil
		end 

		it "test_find_waldo" do 
			expect(obje.test_find_waldo).to eq "waldo"
		end 

		it "test_cannot_find_3_letter_words" do 
			expect(obje.test_cannot_find_3_letter_words).to eq nil
		end 

		it "test_find_13" do 
			expect(obje.test_find_13).to eq 13
		end 

		it "test_find_first_even_number" do 
			expect(obje.test_find_first_even_number).to eq 10
		end 

		it "test_find_first_multiple_of_3" do 
			expect(obje.test_find_first_multiple_of_3).to eq 9
		end 

		it "test_find_first_word_starting_with_q" do 
			expect(obje.test_find_first_word_starting_with_q).to eq "quill"
		end 

		it "test_find_first_word_ending_with_er" do 
			expect(obje.test_find_first_word_ending_with_er).to eq "finger"
		end 

		it "test_find_first_number_greater_than_20" do 
			expect(obje.test_find_first_number_greater_than_20).to eq 21
		end 


	end 
end 

