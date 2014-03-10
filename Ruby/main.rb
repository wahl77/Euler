require 'pry'

class MyMath

  class Prime
    attr_accessor :value

    def initialize
      @value = 2
    end

    def is_prime?(n)
      return false if n < 2
      return true if n == 2
      (2..(n**0.5).to_i).step(1).each do |i|
        return false if n % i == 0
      end
      true
    end

    def next
      @value += 1
      while !is_prime?(value)
        @value += 1
      end
      @value
    end

  end

  class PrimeCalculator
    attr_accessor :factors, :prime_numbers

    def factors(value)
      factors = []
      prime_number = Prime.new
      while value != 1
        if value % prime_number.value == 0
          factors << prime_number.value
          value = value / prime_number.value
        else
          prime_number.next
        end
      end
      factors
    end

    def unique_factors(n)
      factors(n).uniq
    end
  end

  class Fib
    attr_accessor :numbers
    def initialize(args = {})
      num1 = args[:first_number] || 1
      num2 = args[:second_number] || 2
      @numbers = [num1, num2]
    end

    def next
      current = numbers
      @numbers << (current[-1] + current[-2])
      @numbers[-1]
    end

    def term(n)
      while @numbers.count < n
        self.next
      end
      @numbers[-1]
    end

  end
end

class Prob1
  def self.run(number = 1000)
    (1..number-1).select{ |x| x % 3 == 0 || x % 5 == 0}.reduce(:+)
  end
end

class Prob2
  def self.run(n = 4_000_000)
    term = 0
    fib = MyMath::Fib.new({first_number: 0, second_number: 1})
    value = fib.next
    while value < n
      term += value if (value % 2 == 0)
      value = fib.next
    end
    term
  end
end

class Prob3
  def self.run(n = 600851475143)
    calc = MyMath::PrimeCalculator.new
    calc.factors(n).last
  end
end

class Prob4
  def self.run(n = 3)
    largest = 0
    biggest_num = ("9"*n).to_i
    smallest_num = ("1"+("0"*(n-1))).to_i
    (smallest_num..biggest_num).to_a.reverse.each do |i|
      (smallest_num..biggest_num).to_a.reverse.each do |j|
        val = i * j
        largest = val if (val.to_s.reverse == val.to_s) && val > largest
      end
    end
    largest
  end
end

class Prob5
  def self.run
  end
end

class Prob6
  def self.run
  end
end

class Prob7
  def self.run
  end
end

class Prob8
  def self.run
  end
end

class Prob9
  def self.run
  end
end

class Prob10
  def self.run
  end
end

class Prob11
  def self.run
  end
end

class Prob12
  def self.run
  end
end

class Prob13
  def self.run
  end
end

class Prob14
  def self.run
  end
end

class Prob15
  def self.run
  end
end

class Prob16
  def self.run
  end
end

class Prob17
  def self.run
  end
end

class Prob18
  def self.run
  end
end

class Prob19
  def self.run
  end
end

class Prob20
  def self.run
  end
end

class Prob21
  def self.run
  end
end

class Prob22
  def self.run
  end
end

class Prob23
  def self.run
  end
end

class Prob24
  def self.run
  end
end

class Prob25
  def self.run
  end
end

class Prob26
  def self.run
  end
end

class Prob27
  def self.run
  end
end

class Prob28
  def self.run
  end
end

class Prob29
  def self.run
  end
end

class Prob30
  def self.run
  end
end

class Prob31
  def self.run
  end
end

class Prob32
  def self.run
  end
end

class Prob33
  def self.run
  end
end

class Prob34
  def self.run
  end
end

class Prob35
  def self.run
  end
end

class Prob36
  def self.run
  end
end

class Prob37
  def self.run
  end
end

class Prob38
  def self.run
  end
end

class Prob39
  def self.run
  end
end

class Prob40
  def self.run
  end
end

class Prob41
  def self.run
  end
end
