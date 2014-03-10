require_relative "../main"


describe "Problems" do
  it "solves Problem 1" do
    expect(Prob1.run(10)).to eql(23)
    expect(Prob1.run).to eql(233168)
  end

  it "solves Problem 2" do
    expect(Prob2.run).to eql(4613732)
  end

  it "solves Problem 3" do
    expect(Prob3.run).to eql(6857)
  end

  it "solves Problem 4" do
    expect(Prob4.run(2)).to eql(9009)
    expect(Prob4.run).to eql(906609)
  end

  it "solves Problem 5" do
    expect(Prob5.run).to eql(232792560)
  end
end
