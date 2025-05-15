require "spec_helper"

require_relative "../reject/reject_enumerable_method.rb"

describe "reject_enumerable_method" do 
	context "reject_enumerable_method" do 
		let(:obj) {RejectEnumerableMethod.new}

		it "test_remove_zeros" do 
			expect(obj.test_remove_zeros).to match_array [2, 93, 7, 1, 31, 368]
		end 

		it "test_remove_vowels" do 
			expect(obj.test_remove_vowels).to match_array ["l", "l", " ", "y", "r", " ", "b", "s", " ", "r", " ", "b", "l", "n", "g", " ", "t", " ", "s"]
		end 

		it "test_remove_numbers_divisible_by_3" do 
			expect(obj.test_remove_numbers_divisible_by_3).to match_array [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20] 
		end 

		it "test_remove_words_with_more_than_three_letters" do 
			expect(obj.test_remove_words_with_more_than_three_letters).to match_array ["bad", "cat", "dog", "red"]
		end 

		it "test_remove_words_ending_in_e" do 
			expect(obj.test_remove_words_ending_in_e).to match_array ["you", "thinking", "belt", "sing"]
		end 

		it "test_remove_words_ending_in_ing" do 
			expect(obj.test_remove_words_ending_in_ing).to match_array  ["finger", "drought", "bingo", "purposeful"]
		end 

		it "test_remove_words_containing_e" do 
			expect(obj.test_remove_words_containing_e).to match_array ["four", "pizza"]
		end 

		it "test_remove_dinosaurs" do 
			expect(obj.test_remove_dinosaurs).to match_array ["narwhal", "eel"]
		end 

		it "test_remove_numbers" do 
			expect(obj.test_remove_numbers).to match_array ["cat", "dog", "aimless"]
		end 

		it "test_remove_floats" do 
			expect(obj.test_remove_floats).to match_array ["cat", "dog", 23, 56, "aimless"]
		end 

		it "test_remove_animals_starting_with_vowels" do 
			expect(obj.test_remove_animals_starting_with_vowels).to match_array ["bonobo", "cat", "dog"]
		end 

		it "test_remove_capitalized_words" do 
			expect(obj.test_remove_capitalized_words).to match_array ["dog", "Trevor", "butter"]
		end 

		it "test_remove_arrays" do 
			expect(obj.test_remove_arrays).to match_array ["CAT", 23, "AIMLESS", 43, "butter"]
		end 

		it "test_remove_hashes" do 
			expect(obj.test_remove_hashes).to match_array ["cat", 23, "aimless", 43]
		end 


	end 
end 

