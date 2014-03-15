class Prob5
  def self.run(n = 20)
    number = 20
    while true
      pass = true
      (2..n).each do |j|
        if number % j != 0
          pass = false
          break
        end
      end
      return number if pass
      number += 20
    end

  end
end
