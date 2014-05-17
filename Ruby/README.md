# Ruby project Euler Implemenation
This is a ruby implementation of project Euler problems


## Testing

### RSpec
To run a single rspec test do
```bash
rspec spec/problem_spec.rb -e "solves Problem <problem_number>"
```

to run all rspec tests do 
```bash
rspec spec/
```

### Minitest
to run a single unit test do 
```bash
ruby -Itest test/main_test.rb -n test_prob_<problem_number>
```

or with color
```bash
ruby -rminitest/pride test/main_test.rb -n test_prob_<problem_number>
```

to run all tests
```bash
ruby -Itest test/main_test.rb
```
