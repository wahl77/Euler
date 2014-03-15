class Prob6

  def self.run(n = 100)
    range = (1..n)
    sum_of_squares = range.map{|x| x*x}.reduce(:+)
    square_of_sum = begin
      sum = range.reduce(:+)
      sum * sum
    end
    square_of_sum - sum_of_squares
  end

end
