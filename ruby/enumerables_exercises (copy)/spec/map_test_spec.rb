require "spec_helper"

require_relative "../map/map_test.rb"

describe "map map_test" do 
	context "test_capitalize" do 
		let(:mapTest) {MapTest.new}
		it "test_capitalize" do 
			expect(mapTest.test_capitalize).to match_array(["Alice", "Bob", "Charlie"])
		end 
		it "test_doubles" do 
			expect(mapTest.test_doubles).to match_array([2, 4, 6, 8, 10])
		end 

		it "test_squares" do 
			expect(mapTest.test_squares).to match_array([1, 4, 9, 16, 25])
		end 

		it "test_lengths" do 
			expect(mapTest.test_lengths).to match_array([5, 3, 7, 5, 3])
		end 

		it "test_normalize_zip_codes" do 
			expect(mapTest.test_normalize_zip_codes).to match_array(["00234", "00010", "09119", "38881"])
		end 


		it "test_backwards" do 
			expect(mapTest.test_backwards).to match_array(["ecila", "bob", "eilrahc", "divad", "eve"])
		end 
		it "test_words_with_no_vowels" do 
			expect(mapTest.test_words_with_no_vowels).to match_array(["grn", "shp", "trvl", "lst", "bt"])
		end 
				
	end 
end 



# rspec spec/map_pattern_test_spec.rb