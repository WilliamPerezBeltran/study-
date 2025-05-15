require "spec_helper"

require_relative "../001_Two_Sum.rb"

describe "001_Two_Sum" do 
	context "001_Two_Sum" do 
		let(:obj) {LeetCode.new}

		it "test_1" do 
			expect( obj.two_sum([2,7,11,15], 9) ).to match_array([0,1]) 
		end 

        it "test_2" do 
			expect(obj.two_sum([1,2,3,4,5,6,7,8,9,10,11,12],23)).to match_array([10,11]) 
		end 

        it "test_3" do 
			expect(obj.two_sum([3,2,4], 6)).to match_array([1,2]) 
		end 

        it "test_4" do 
			expect(obj.two_sum([3,3], 6)).to match_array([0,1]) 
		end 
	end 
end 
