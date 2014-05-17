class Prob12
  attr_reader :answer

  attr_accessor :current_counter
  attr_accessor :number_of_divisor
  def initialize(number_of_divisor)
    @number_of_divisor = number_of_divisor
    @current_counter = 0
    go
  end

  def self.run(number_of_divisor = 500)
    prob = new(number_of_divisor)
    prob.answer
  end

  def go
    check_num = next_triangle
    while (MyMath.num_divisors(check_num) <= number_of_divisor)
      check_num = next_triangle(check_num)
    end
    @answer = check_num
  end

  private

  def next_triangle(check_num = 0)
    check_num += (current_counter)
  end

  def current_counter
    @current_counter += 1
  end

end
