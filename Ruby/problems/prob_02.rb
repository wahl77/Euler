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
