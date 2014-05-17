require_relative "../main"

require 'minitest/autorun'

class FibTest < Minitest::Test
  def test_term
    fib = MyMath::Fib.new
    assert_equal 89, fib.term(10)
  end
end

class PrimeTest < Minitest::Test
  def setup
    @prime = MyMath::Prime.new
    @calculator = MyMath::PrimeCalculator.new
  end

  def test_is_prime
    assert_equal true, (@prime.is_prime? 2)
    assert_equal true, (@prime.is_prime? 5)
    assert_equal true, (@prime.is_prime? 101)
    assert_equal false,(@prime.is_prime? 4)
    assert_equal false,(@prime.is_prime? 102)
    assert_equal false,(@prime.is_prime? 10)
    assert_equal false,(@prime.is_prime? 1)
  end

  def test_factors
    assert_equal [2, 2, 5], (@calculator.factors(20))
  end

  def test_unique_factors
    assert_equal [5], @calculator.unique_factors(5)
    assert_equal [5, 7, 13, 29], @calculator.unique_factors(13195)
  end
end

class ProblembsTest < Minitest::Test
  def test_prob_1
    assert_equal 23, Prob1.run(10)
    assert_equal 233168, Prob1.run
  end

  def test_prob_2
    assert_equal 4613732, Prob2.run
  end

  def test_prob_3
    assert_equal 6857, Prob3.run
  end

  def test_prob_4
    assert_equal 9009, Prob4.run(2)
    assert_equal 906609, Prob4.run
  end

  def test_prob_5
    assert_equal 2520, Prob5.run(10)
    assert_equal 232792560, Prob5.run
  end

  def test_prob_6
    assert_equal 2640, Prob6.run(10)
    assert_equal 25164150, Prob6.run
  end

  def test_prob_7
    assert_equal 13, Prob7.run(6)
    assert_equal 104743, Prob7.run
  end

  def test_prob_8
    assert_equal 40824, Prob8.run
  end

  def test_prob_9
    assert_equal 60, Prob9.run(12)
    assert_equal 31875000, Prob9.run
  end

  def test_prob_10
    assert_equal 17, Prob10.run(10)
    assert_equal 142913828922, Prob10.run
  end

  def test_prob_11
    assert_equal 70600674, Prob11.run
  end

  def test_prob_12
    assert_equal 28, Prob12.run(5)
    assert_equal 76576500, Prob12.run
  end

  def test_prob_13
    assert_equal 5537376230, Prob13.run
  end

  def test_prob_14
    assert_equal [13, 40, 20, 10, 5, 16, 8, 4, 2, 1], Prob14.new.send(:chain, 13)
    assert_equal 837799, Prob14.run
  end

  def test_prob_15
    assert_equal 6, Prob15.run(grid: 2)
    assert_equal 137846528820, Prob15.run
  end
end


puts "run test with\nruby #{__FILE__}.rb --name method_name"
