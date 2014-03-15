class Prob4
  def self.run(n = 3)
    largest = 0
    biggest_num = ("9"*n).to_i
    smallest_num = ("1"+("0"*(n-1))).to_i
    (smallest_num..biggest_num).to_a.reverse.each do |i|
      (smallest_num..biggest_num).to_a.reverse.each do |j|
        val = i * j
        largest = val if (val.to_s.reverse == val.to_s) && val > largest
      end
    end
    largest
  end
end
