defmodule Prime do
  def is_prime(num) do
    if num <= 1 do
      false
    else
      Enum.all?(2..Integer.floor(Math.sqrt(num)), fn i -> rem(num, i) != 0 end)
    end
  end

  def print_primes(n) do
    IO.puts("Prime numbers between 1 and #{n} are:")
    Enum.each(2..n, fn i ->
      if is_prime(i) do
        IO.write("#{i} ")
      end
    end)
    IO.puts()
  end
end

IO.puts("Enter n: ")
n = IO.read(:line) |> String.trim() |> String.to_integer()

Prime.print_primes(n)
