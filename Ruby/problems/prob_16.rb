class Prob16

  attr_accessor :num

  def initialize(opts = {})
    @num = opts[:num] || 1000
  end

  def calculate
    (2**num).to_s.split("").map{|x| x.to_i}.reduce(:+)
  end

  def self.run(opts = {})
    new(opts).calculate
  end

  private


end
