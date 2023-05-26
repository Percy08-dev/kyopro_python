use proconio::input;

fn main() {
    input!{
        a: i32, b: i32, c: i32,
    }

    if b/a > c{
        println!("{}", c);
    }else{
        println!("{}", b/a);
    }
}
