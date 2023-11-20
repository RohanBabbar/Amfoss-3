use std::io;

fn is_prime(num: u32) -> bool {
    if num <= 1 {
        return false;
    }
    for i in 2..=num.sqrt() as u32 {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn print_primes(n: u32) {
    println!("Prime numbers between 1 and {} are:", n);
    for i in 2..=n {
        if is_prime(i) {
            print!("{} ", i);
        }
    }
    println!();
}

fn main() {
    println!("Enter n: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: u32 = input.trim().parse().expect("Invalid input");

    print_primes(n);
}
