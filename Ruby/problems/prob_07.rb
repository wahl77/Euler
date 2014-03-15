class Prob7
  def self.run(n=10_001)
    prime = MyMath::Prime.new
    while prime.primes.count < n
      prime.next
    end
    prime.value
  end
end
