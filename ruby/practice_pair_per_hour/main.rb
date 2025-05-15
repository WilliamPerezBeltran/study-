require "./configuration"
require 'date'
require 'pry'
class App
	include Configuration
end


app = App.new
puts "===============app.price_plans==============="
puts app.price_plans
puts "===============app.smart_meter_to_price_plan_accounts==============="
puts app.smart_meter_to_price_plan_accounts
puts "===============app.smart_meter_to_price_plan_accounts==============="
puts app.readings
puts "===============app.readings_per_hour==============="
puts app.hour
