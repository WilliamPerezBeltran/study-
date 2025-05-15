require "spec_helper"

require_relative "../reduce/reduce_enumerable_method.rb"

describe "ReduceUsingEach" do 
	context "ReduceUsingEach" do 
		let(:obj) {ReduceEnumerableMethod.new}

		it "test_sum_a_list_of_numbers" do 
			expect(obj.test_sum_a_list_of_numbers).to eq 473
		end 

		it "test_subtract_list_of_numbers" do 
			expect(obj.test_subtract_list_of_numbers).to eq -170
		end 

		it "test_multiply_list_of_numbers" do 
			expect(obj.test_multiply_list_of_numbers).to eq 210
		end 

		it "test_capitalize_keywords_in_phrase_one_fish_two_fish_red_fish_blue_fish" do 
			expect(obj.test_capitalize_keywords_in_phrase_one_fish_two_fish_red_fish_blue_fish).to eq 'one FISH two FISH red FISH BLUE FISH'
		end 

		it "test_divide_560_by_a_bunch_of_numbers" do 
			expect(obj.test_divide_560_by_a_bunch_of_numbers).to eq 2
		end 

		it "test_subtract_smallest_values_from_100" do 
			expect(obj.test_subtract_smallest_values_from_100).to eq 88
		end 

		it "test_add_all_the_second_values_together" do 
			expect(obj.test_add_all_the_second_values_together).to eq 31
		end 
	end 
end 

