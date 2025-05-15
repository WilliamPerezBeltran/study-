require "spec_helper"

require_relative "../group_by/group_by_enumerable_method.rb"

describe "group_by_enumerable_method" do 
	context "group_by_enumerable_method" do 
		let(:obj) {GroupByEnumerableMethod.new}

		it "test_group_words_by_length" do 
			expect(obj.test_group_words_by_length).to eq({3=>["sue", "dog", "cat"], 4=>["adam", "fort", "tops"], 5=>["alice", "steve", "sally"]})
		end 


		it "test_group_numbers_by_odd_and_even" do 
			expect(obj.test_group_numbers_by_odd_and_even).to eq({1=>[1, 1, 3, 5, 13, 21, 55], 0=>[2, 8, 34]})
		end 

		it "test_group_words_by_first_letter" do 
			expect(obj.test_group_words_by_first_letter).to eq({"a"=>["ant", "axis", "albatross"], "b"=>["bolt", "badge", "butter"], "c"=>["car", "cdr", "column"]}) 
		end 

		it "test_group_words_by_uniqueness" do 
			expect(obj.test_group_words_by_uniqueness).to eq({"one"=>["one", "one", "one"], "two"=>["two", "TWO"], "three"=>["three", "three", "three", "three"]}) 
		end 

		it "test_group_by_number_of_zeros" do 
			expect(obj.test_group_by_number_of_zeros).to eq({0=>[1, 3], 2=>[500, 200], 3=>[4000, 3000], 4=>[10000], 1=>[90, 20], 5=>[500000]}) 
		end 

		it "test_group_by_order_of_magnitude" do 
			expect(obj.test_group_by_order_of_magnitude).to eq({1=>[1, 3], 2=>[93, 21], 3=>[503, 239], 4=>[4938, 3932], 5=>[19982], 6=>[501787]}) 
		end 


		
	end 
end 

