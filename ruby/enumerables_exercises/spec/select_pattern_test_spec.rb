require "spec_helper"

require_relative "../select/select_pattern_test.rb"

describe "select pattern test" do 
	context "test_capitalize" do 
		let(:obje) {SelectPatternTest.new}

		it " has default damage rating of 10" do 
			expect(obje.test_pick_even_numbers).to match_array( [2, 4, 6, 8, 10])
		end 

		it " test_pick_odd_numbers" do 
			expect(obje.test_pick_odd_numbers).to match_array([1, 3, 5, 7, 9])
		end 

		it " test_pick_words_with_three_letters" do 
			expect(obje.test_pick_words_with_three_letters).to match_array(["bad", "cat", "dog", "red"])
		end 

		it " test_pick_words_with_more_than_three_letters" do 
			expect(obje.test_pick_words_with_more_than_three_letters).to match_array(["pill", "finger", "blue", "table"])
		end 

		it " test_pick_words_ending_in_e" do 
			expect(obje.test_pick_words_ending_in_e).to match_array(["are", "strike", "piece", "warble", "pipe"])
		end 

		it " test_pick_words_ending_in_ing" do 
			expect(obje.test_pick_words_ending_in_ing).to match_array(["bring", "singing"])
		end 

		it " test_pick_words_containing_e" do 
			expect(obje.test_pick_words_containing_e).to match_array(["red", "five", "blue", "purple"])
		end 

		it " test_pick_dinosaurs" do 
			expect(obje.test_pick_words_containing_e).to match_array(["red", "five", "blue", "purple"])
		end 

		it " test_pick_floats" do 
			expect(obje.test_pick_floats).to match_array([1.4, 3.5, 4.9, 9.1, 8.0])
		end 

		it " test_pick_arrays" do 
			expect(obje.test_pick_arrays).to match_array([["dog"], [56, 3, 8]])
		end 

		it " test_pick_hashes" do 
			expect(obje.test_pick_hashes).to match_array( [{:dog=>"fido"}, {:stuff=>"things"}])
		end 

		
	end 
end 



# rspec spec/map_pattern_test_spec.rb