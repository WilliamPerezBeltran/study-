require_relative '../greeter.rb'

RSpec.describe Greeter do
  describe '#greet' do
    it "says hello" do
      expect(Greeter.new.greet).to eq("Hello, world!")
    end
  end
end

