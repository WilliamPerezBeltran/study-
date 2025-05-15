require "pry"


p "-------------------"
p "-------------------"
p "-------------------"

def blank_seating_chart(number_of_rows, seats_per_row)
  # return a 2d array to represent a seating chart that contains
  # number_of_rows nested arrays, each with seats_per_row entries of nil to
  # represent that each seat is empty.

  # Example: blank_seating_chart(2, 3) should return:
  # [
  #   [nil, nil, nil],
  #   [nil, nil, nil]
  # ]

  # NOTE: if one of the nested arrays is changed, the others should **not**
  # change with it
  rta = Array.new()
  for x in (0..number_of_rows-1)
  	arra_1 = []
  	for y in (0..seats_per_row-1)
  		arra_1.push(nil)
  	end
  	rta.push(arra_1)
  end
  p rta
end


 blank_seating_chart(2, 3)
 blank_seating_chart(3, 2)
 blank_seating_chart(4, 5)
 blank_seating_chart(1, 3)



def add_seat_to_row(chart, row_index, seat_to_add)
  # take a chart (2d array)  and add seat_to_add to the end of the row that is
  # at row_index index of the chart, then return the chart
  # binding.pry

  p "chart: #{chart}"
  for x in (0..chart.length-1)
      
      if x == row_index
        # p "x: #{x}"
         chart[x].push(seat_to_add)
      end
  end
  p chart
end
 add_seat_to_row([[1,2],[3,4]], 1,100)
 add_seat_to_row([[nil, 'Bob', 'Joe'], [nil, nil, 'Bill', 'Jack']], 1, 'Jack')


 def count_empty_seats(chart)
 	binding.pry
  # take a chart and return the number of empty (nil) seats in it
  chart.flatten.select{|x| x.empty?}.count

  # NOTE: `chart` should **not** be mutated
end



p count_empty_seats([[nil, 'Bob', 'Joe'], [nil, nil, 'Bill']])