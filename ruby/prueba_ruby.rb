class Calculator
  def calculate_sum(a, b)
    number_a = a.join('').to_i
    number_b = b.join('').to_i
    return number_a + number_b 
  end
end

c = Calculator.new
puts c.calculate_sum([1,2,3], [2,3,1])

# ====================================
class Calculator
  def calculate_sum(a, b)
    if a.nil? or a.empty? or b.nil? or b.empty?
      raise("ArgumentError") 
  else     
      a.join('').to_i + b.join('').to_i
  end
  end
end

c = Calculator.new
puts c.calculate_sum([1,2,3], [2,3,1])
# ====================================

class CategoryTree
  def initialize()
    @hash_category = {}
  end

  

  def add_category(category, parent)
    if !category.nil? and parent.nil?
      @hash_category[category.downcase]=[]
      return @hash_category
    end

    if !category.nil? and !parent.nil?
      if @hash_category[category.downcase].exist?
        array = @hash_category[category.downcase]
        array.push(category)
      else
        raise("No encounter category")
      end
    end

  end

  def get_children(category)
    ary.find { |h| h['product'] == 'bcx' }['href']
    return []
  end

end

c = CategoryTree.new
puts c.add_category('A', nil)
puts c.add_category('b', nil)
puts c.add_category('b', nil)
c.add_category('B', 'A')
# c.add_category('C', 'A')
# puts (c.get_children('A') || []).join(',')

# ====================================
class Bank
  def least_number_of_dollars(dollars, amount)
    if dollars.nil? or dollars.empty? or amount.nil? 
      return raise("params are empty or nil") 
    else
     return nil if amount < 0
     return nil if amount != amount.floor

     parents = Array.new(amount + 1)
     parents[0] = 0
     listWorking = [[0, 0]]
     while parents[amount].nil? && !listWorking.empty? do
       base, starting_index = listWorking.shift
       starting_index.upto(dollars.size - 1) do |index|
         coin = dollars[index]
         pivot = base + coin
         if pivot <= amount && parents[pivot].nil?
           parents[pivot] = base
           listWorking << [pivot, index]
         end
       end
     end

     return nil if parents[amount].nil?
     result = []
     while amount > 0 do
       parent = parents[amount]
       result << amount - parent
       amount = parent
     end
     result.sort!.reverse!.length
   end

 end
end

amount = Bank.new
puts amount.least_number_of_dollars([1,2,5], 11)