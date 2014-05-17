class Prob15
  attr_accessor :grid
  def initialize(opts = {})
    @grid = opts[:grid] || 20
  end

  def calculate
    MyMath.choose(2*grid, grid)
  end

  def self.run(opts = {})
    new(opts).calculate
  end
end
