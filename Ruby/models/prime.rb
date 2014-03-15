class MyMath

  class Prime
    attr_accessor :value, :primes

    def initialize
      @primes = []
    end

    def is_prime?(n)
      return true if n == 2 || n == 3 || n == 5
      return false if n < 5
      upper_limit = (n ** 0.5).to_i
      while value < upper_limit
        self.next
      end
      primes.each do |i|
        return false if n % i == 0
      end
      true
    end

    def next
      value_to_test = 2 if primes.count == 0
      value_to_test = 3 if primes.count == 1
      value_to_test ||= primes[-1] + 2

      until is_prime? value_to_test
        value_to_test += 2
      end
      primes << value_to_test
      value_to_test
    end

    def value
      primes[-1] || self.next
    end

  end

  class PrimeCalculator
    attr_accessor :factors, :prime_numbers

    def factors(value)
      factors = []
      prime_number = Prime.new
      prime_number.next
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
end
