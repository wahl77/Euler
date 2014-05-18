class Prob17
  attr_accessor :num
  def initialize(opts = {})
    @num = opts[:num] || 1000
  end

  def calculate
    length = 0
    (1..num).each do |i|
      length += num_to_string(i).delete(' ').length
    end
    length
  end

  def self.run(opts = {})
    new(opts).calculate
  end

  private

  def num_to_string(n)
    string = ""
    if n > 999
      string += numbers[n / 1000] + " "
      string += "thousand "
      n = n % 1000
    end
    if n > 99
      string += numbers[n / 100] + " "
      string += "hundred "
      if n % 100 != 0
        string +="and "
      else
        return string
      end
      n = n % 100
    end
    if n >= 20
      string += numbers[(n/10) * 10] + " "
      n = n % 10
    end
    if n < 20 and n != 0
      string += numbers[n] + " "
    end
	  string
  end


  def numbers
    {
      1 => "one",
      2 =>  "two",
      3 =>  "three",
      4 =>  "four",
      5 =>  "five",
      6 =>  "six",
      7 =>  "seven",
      8 =>  "eight",
      9 =>  "nine",
      10 =>  "ten",
      11 =>  "eleven",
      12 =>  "twelve",
      13 =>  "thirteen",
      14 =>  "fourteen",
      15 =>  "fifteen",
      16 =>  "sixteen",
      17 =>  "seventeen",
      18 =>  "eighteen",
      19 =>  "nineteen",
      20 =>  "twenty",
      30 =>  "thirty",
      40 =>  "forty",
      50 =>  "fifty",
      60 =>  "sixty",
      70 =>  "seventy",
      80 =>  "eighty",
      90 =>  "ninety",
      100 =>  "hundred"
    }
  end

end
