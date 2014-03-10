require_relative "main"
require 'test/unit'

class FibTest < Test::Unit::TestCase
  def test_term
    fib = MyMath::Fib.new
    assert_equal 89, fib.term(10)
  end
end

class PrimeTest < Test::Unit::TestCase
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

class ProblembsTest < Test::Unit::TestCase
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
    assert_equal 232792560, Prob5.run
  end
end


puts "run test with\nruby #{__FILE__}.rb --name method_name"
