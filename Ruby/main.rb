require 'pry'

if defined? RSpec
  RSpec.configure do |config|
    # Use color in STDOUT
    config.color_enabled = true

    # Use color not only in STDOUT but also in pagers and files
    config.tty = true

    # Use the specified formatter
    config.formatter = :documentation # :progress, :html, :textmate
  end
end


Dir[File.dirname(__FILE__) + '/models/*.rb'].each {|file| require file }
Dir[File.dirname(__FILE__) + '/problems/*.rb'].each {|file| require file }

number = ARGV[0].to_i.to_s

#puts eval("Prob"+number+".run") if ARGV.length > 0
