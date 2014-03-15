class Prob9
  def self.run(n=1000)
    (1..n).to_a.each do |i|
      (i..n).to_a.each do |j|
        k = n - i - j
        return i*j*k if self.is_pyth?(i, j, k)
      end
    end
  end

  private
  def self.is_pyth?(a, b, c)
    a*a + b*b == c*c
  end
end
