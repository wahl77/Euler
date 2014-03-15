class Prob1
  def self.run(number = 1000)
    (1..number-1).select{ |x| x % 3 == 0 || x % 5 == 0}.reduce(:+)
  end
end
