def is_prime(num)
    return false if num <= 1
  
    (2..Math.sqrt(num).to_i).each do |i|
      return false if num % i == 0
    end
  
    true
  end
  
  print 'Enter n: '
  num = gets.chomp.to_i
  puts 'Prime Numbers are:'
  (2...num).each do |i|
    puts i if is_prime(i)
  end
  