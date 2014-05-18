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
    expect(Prob5.run(10)).to eql(2520)
    expect(Prob5.run).to eql(232792560)
  end

  it "solves Problem 6" do
    expect(Prob6.run(10)).to eql(2640)
    expect(Prob6.run).to eql(25164150)
  end

  it "solves Problem 7" do
    expect(Prob7.run(6)).to eql(13)
    expect(Prob7.run).to eql(104743)
  end

  it "solves Problem 8" do
    expect(Prob8.run).to eql(40824)
  end

  it "solves Problem 9" do
    expect(Prob9.run(12)).to eql(60)
    expect(Prob9.run).to eql(31875000)
  end

  it "solves Problem 10" do
    expect(Prob10.run(10)).to eql(17)
    expect(Prob10.run).to eql(142913828922)
  end

  it "solves Problem 11" do
    expect(Prob11.run).to eql(70600674)
  end

  it "solves Problem 12" do
    expect(Prob12.run(5)).to eql(28)
    expect(Prob12.run).to eql(76576500)
  end

  it "solves Problem 13" do
    expect(Prob13.run).to eql(5537376230)
  end

  it "solves Problem 14" do
    expect(Prob14.new.send(:chain, 13)).to eql([13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    expect(Prob14.run).to eql(837799)
  end

  it "solves Problem 15" do
    expect(Prob15.run(grid: 2)).to eql(6)
    expect(Prob15.run).to eql(137846528820)
  end

  it "solves Problem 16" do
    expect(Prob16.run(num: 15)).to eql(26)
    expect(Prob16.run).to eql(1366)
  end

  it "solves Problem 17" do
    pending
    #expect(Prob17.run).to eql()
  end

  it "solves Problem 18" do
    pending
    #expect(Prob18.run).to eql()
  end

  it "solves Problem 19" do
    pending
    #expect(Prob19.run).to eql()
  end

  it "solves Problem 20" do
    pending
    #expect(Prob20.run).to eql()
  end

  it "solves Problem 21" do
    pending
    #expect(Prob21.run).to eql()
  end

  it "solves Problem 22" do
    pending
    #expect(Prob22.run).to eql()
  end

  it "solves Problem 23" do
    pending
    #expect(Prob23.run).to eql()
  end

  it "solves Problem 24" do
    pending
    #expect(Prob24.run).to eql()
  end

  it "solves Problem 25" do
    pending
    #expect(Prob25.run).to eql()
  end

  it "solves Problem 26" do
    #expect(Prob26.run).to eql()
  end

  it "solves Problem 27" do
    pending
    #expect(Prob27.run).to eql()
  end

  it "solves Problem 28" do
    pending
    #expect(Prob28.run).to eql()
  end

  it "solves Problem 29" do
    pending
    #expect(Prob29.run).to eql()
  end

  it "solves Problem 30" do
    pending
    #expect(Prob30.run).to eql()
  end

  it "solves Problem 31" do
    pending
    #expect(Prob31.run).to eql()
  end

  it "solves Problem 32" do
    pending
    #expect(Prob32.run).to eql()
  end

  it "solves Problem 33" do
    pending
    #expect(Prob33.run).to eql()
  end

  it "solves Problem 34" do
    pending
    #expect(Prob34.run).to eql()
  end

  it "solves Problem 35" do
    pending
    #expect(Prob35.run).to eql()
  end

  it "solves Problem 36" do
    pending
    #expect(Prob36.run).to eql()
  end

  it "solves Problem 37" do
    pending
    #expect(Prob37.run).to eql()
  end

  it "solves Problem 38" do
    pending
    #expect(Prob38.run).to eql()
  end

  it "solves Problem 39" do
    pending
    #expect(Prob39.run).to eql()
  end

  it "solves Problem 40" do
    pending
    #expect(Prob40.run).to eql()
  end

  it "solves Problem 41" do
    pending
    #expect(Prob41.run).to eql()
  end

  it "solves Problem 42" do
    pending
    #expect(Prob42.run).to eql()
  end

  it "solves Problem 43" do
    pending
    #expect(Prob43.run).to eql()
  end

  it "solves Problem 44" do
    pending
    #expect(Prob44.run).to eql()
  end

  it "solves Problem 45" do
    pending
    #expect(Prob45.run).to eql()
  end

  it "solves Problem 46" do
    pending
    #expect(Prob46.run).to eql()
  end

  it "solves Problem 47" do
    pending
    #expect(Prob47.run).to eql()
  end

  it "solves Problem 48" do
    pending
    #expect(Prob48.run).to eql()
  end

  it "solves Problem 49" do
    pending
    #expect(Prob49.run).to eql()
  end

  it "solves Problem 50" do
    pending
    #expect(Prob50.run).to eql()
  end

  it "solves Problem 51" do
    pending
    #expect(Prob51.run).to eql()
  end

  it "solves Problem 52" do
    pending
    #expect(Prob52.run).to eql()
  end

  it "solves Problem 53" do
    pending
    #expect(Prob53.run).to eql()
  end
end
