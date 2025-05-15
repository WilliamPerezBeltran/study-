require "spec_helper"

require_relative "../map/map_pattern_test.rb"

describe "map pattern test" do 
	context "test_capitalize" do 
		let(:patern) {MapPatternTest.new}
		it " has default damage rating of 10" do 
			expect(patern.test_capitalize).to match_array(["Alice", "Bob", "Charlie"])
		end 

		it "test_doubles" do
			expect(patern.test_doubles).to match_array([2, 4, 6, 8, 10])
		end 

		it "test_squares" do
			expect(patern.test_squares).to match_array([1, 4, 9, 16, 25])
		end 

		it "test_lengths" do
			expect(patern.test_lengths).to match_array([5, 3, 7, 5, 3])
		end 
		it "test_normalize_zip_codes" do 
			expect(patern.test_normalize_zip_codes).to match_array(["00234", "00010", "09119", "38881"])
		end 

		it "test_normalize_zip_codes" do 
			expect(patern.test_normalize_zip_codes_1).to match_array(["00234", "00010", "09119", "38881"])
		end 

		it "test_normalize_zip_codes" do 
			expect(patern.test_backwards).to match_array(["ecila", "bob", "eilrahc", "divad", "eve"])
		end 

		it "test_words_with_no_vowels" do 
			expect(patern.test_words_with_no_vowels).to match_array(["grn", "shp", "trvl", "lst", "bt"])
		end 
	end 
end 



# rspec spec/map_pattern_test_spec.rb