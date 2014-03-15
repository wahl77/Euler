class Prob3
  def self.run(n = 600851475143)
    calc = MyMath::PrimeCalculator.new
    calc.factors(n).last
  end
end
