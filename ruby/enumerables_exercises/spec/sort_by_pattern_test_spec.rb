require "spec_helper"

require_relative "../sort_by/sort_by_pattern_test.rb"

describe "SortByPatternTest" do 
	context "SortByPatternTest" do 
		let(:obje) {SortByPatternTest.new}

		it "test_sort_alphabetically" do 
			expect(obje.test_sort_alphabetically).to match_array(["Bacon", "broccoli", "candy", "Carrots", "FISH"])
		end 

		it "test_sort_alphabetically_by_last_letter" do 
			expect(obje.test_sort_alphabetically_by_last_letter).to match_array ["sponge", "pill", "water", "glass", "box"]
		end 

		it "test_sort_by_distance" do 
			expect(obje.test_sort_by_distance).to match_array(["1cm", "2cm", "3cm", "4cm", "9cm"])
		end 

		it "test_sort_by_distance_2" do 
			expect(obje.test_sort_by_distance_2).to match_array(["1cm", "2cm", "4cm", "9cm", "30cm"])
		end 

		it "test_sort_by_length" do 
			expect(obje.test_sort_by_length).to match_array(["bug", "heteromorph", "mathematical", "ancyloceratina", "bioengineering"])
		end 

		it "test_sort_by_proximity_to_ten" do 
			expect(obje.test_sort_by_proximity_to_ten).to match_array([10.01, 9.91, 11.0, 3.02, 17.9])
		end 

		it "test_sort_by_number_of_cents" do 
			expect(obje.test_sort_by_number_of_cents).to match_array([11.0, 10.01, 3.02, 7.9, 9.91])
		end 
	end 
end 

