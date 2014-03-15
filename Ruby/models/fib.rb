class MyMath

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
