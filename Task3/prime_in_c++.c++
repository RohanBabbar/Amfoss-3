#include <iostream>
#include <cmath>

bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int num;
    std::cout << "Enter n: ";
    std::cin >> num;
    std::cout << "Prime Numbers are:" << std::endl;
    for (int i = 2; i < num; i++) {
        if (isPrime(i)) {
            std::cout << i << " ";
        }
    }
    return 0;
}
