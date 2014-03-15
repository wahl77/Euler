class Prob10
  def self.run(n = 2_000_000)
    sieve = (3..n).step(2).to_a
    sum = 2
    while sieve.count != 0
      value = sieve.shift
      sieve.select!{|x| x % value != 0}
      sum += value
    end
    sum
  end
end
