require 'pry'

Dir[File.dirname(__FILE__) + '/models/*.rb'].each {|file| require file }
Dir[File.dirname(__FILE__) + '/problems/*.rb'].each {|file| require file }

number = ARGV[0].to_i.to_s

#puts eval("Prob"+number+".run") if ARGV.length > 0
