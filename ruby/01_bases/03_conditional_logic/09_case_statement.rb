grade = 'F'

case grade
when 'A'
  puts "You're a genius"
  future_bank_account_balance += 5000000
when 'D'
  puts "Better luck next time"
  can_i_retire_soon = false
else
  puts "McDonald's is hiring!"
  fml = true
end

puts fml