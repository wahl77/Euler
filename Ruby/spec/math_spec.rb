require_relative "../main"

describe MyMath do
  before do
    @math = MyMath
  end

  it "#num_divisors" do
    expect(@math.num_divisors(5)).to eql(2)
    expect(@math.num_divisors(6)).to eql(4)
    expect(@math.num_divisors(28)).to eql(6)
  end

  it "#fact" do
    expect(@math.fact(5)).to eql(120)
    expect(@math.fact(6)).to eql(720)
  end

  it "#choose" do
    expect(@math.choose(5, 2)).to eql(10)
    expect(@math.choose(5, 3)).to eql(10)
    expect(@math.choose(5, 3)).to eql(10)
    expect(@math.choose(15, 7)).to eql(6435)
  end


end
