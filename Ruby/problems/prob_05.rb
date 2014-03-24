class Prob5
  def self.run(n = 20)
    num=1
    (1..n).each do |i|
      num = num.lcm(i)
    end
    num
  end
end
