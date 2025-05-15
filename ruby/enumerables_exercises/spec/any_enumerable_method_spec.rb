require "spec_helper"

require_relative "../any/any_enumerable_method.rb"

describe "any_using_each" do 
	context "any" do 
		let(:obj) {AnyEnumerableMethod.new}

		it "test_has_at_least_one_zero" do 
			expect(obj.test_has_at_least_one_zero).to be(true)
		end 

		it "test_does_not_have_any_zeros" do 
			expect(obj.test_does_not_have_any_zeros).to be false
		end 

		it "test_has_at_least_one_alice" do 
			expect(obj.test_has_at_least_one_alice).to be true
		end 

		it "test_no_alices" do 
			expect(obj.test_no_alices).to be false
		end 

		it "test_has_a_multi_word_phrase" do 
			expect(obj.test_has_a_multi_word_phrase).to be true
		end 

		it "test_no_monkeys" do 
			expect(obj.test_no_monkeys).to be false
		end 

		it "test_no_multiples_of_five" do 
			expect(obj.test_no_monkeys).to be false
		end 
	end 
end 

