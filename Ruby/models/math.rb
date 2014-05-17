class MyMath
  def self.num_divisors(remainder)
    counter = 0
    (1..(remainder**0.5).to_i).each do |dividor|
      counter += 2 if remainder % dividor == 0
    end
    counter
  end
end
