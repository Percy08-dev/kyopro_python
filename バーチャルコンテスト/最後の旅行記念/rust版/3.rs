use proconio::input;
use num::integer::lcm;

fn main() {
    input!{
        a:i64, b:i64, 
    }

    println!("{}", lcm(a, b));
}
