class Prob14
  def calculate
    longest = 0
    starting = 0
    (1..(1_000_000-1)).each do |starting_number|
      chain_length = chain(starting_number).length
      if (chain_length > longest)
        longest = chain_length
        starting = starting_number
      end
    end
    starting
  end

  def self.run
    new.calculate
  end

  private

  def chain(num)
    chain = [num]
    number = chain.last
    while number != 1
      number_to_push = (number % 2 == 0) ? number / 2 : 3 * number + 1
      chain << number_to_push
      number = chain.last
    end
    chain
  end

end
