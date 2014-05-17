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


end
