require_relative "../models/fib.rb"

describe MyMath::Fib do
  before :each do
    @fib = MyMath::Fib.new
  end

  it "#next" do
    expect(@fib).to receive(:numbers).and_return([3, 5, 9])
    expect(@fib.next).to eql(14)
  end

  it "#term" do
    expect(@fib.term(10)).to eql(89)
  end
end
