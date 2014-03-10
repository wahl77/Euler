require_relative "../main"

describe MyMath::Prime do
  before do
    @prime = MyMath::Prime.new
  end

  it "#is_prime?" do
    expect(@prime.is_prime?(3)).to be_true
    expect(@prime.is_prime?(5)).to be_true
    expect(@prime.is_prime?(101)).to be_true
    expect(@prime.is_prime?(4)).to be_false
    expect(@prime.is_prime?(1)).to be_false
    expect(@prime.is_prime?(10)).to be_false
    expect(@prime.is_prime?(102)).to be_false
  end
end

describe MyMath::PrimeCalculator do
  before do
    @calculator = MyMath::PrimeCalculator.new
  end

  it "#factors" do
    expect(@calculator.factors(20)).to eql([2, 2, 5])
  end

  it "#unique_factors" do
    expect(@calculator.factors(5)).to eql([5])
    expect(@calculator.factors(13195)).to eql([5, 7, 13, 29])
  end

end
