require "spec_helper"

require_relative "../count/count_using_each.rb"

describe " test with count" do 
	context "count_using_each" do 
		let(:obj) {CountUsingEach.new}

		it "test_count_count_words_with_e" do 
			expect(obj.test_count_count_words_with_e).to eq 3
		end 

		it "test_count_numbers_greater_than_17" do 
			expect(obj.test_count_numbers_greater_than_17).to eq 2
		end 

		it "test_count_words_that_are_uppercase" do 
			expect(obj.test_count_words_that_are_uppercase).to eq 3
		end 

		it "test_count_words_ending_in_ing" do 
			expect(obj.test_count_words_ending_in_ing).to eq 0
		end 

		it "test_count_even_numbers" do 
			expect(obj.test_count_even_numbers).to eq 4
		end 

		it "test_count_multiples_of_5" do 
			expect(obj.test_count_multiples_of_5).to eq 3
		end 

		it "test_count_round_prices" do 
			expect(obj.test_count_round_prices).to eq 2
		end 

		it "test_count_four_letter_words" do 
			expect(obj.test_count_four_letter_words).to eq 6
		end 


	end 
end 

