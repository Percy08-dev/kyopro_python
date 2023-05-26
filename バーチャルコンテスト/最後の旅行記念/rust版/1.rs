use proconio::input;

fn main() {
    input!{
        a: i32, b:i32,
    }
    
    if a <= b {
        println!("unsafe");
    }else {
        println!("safe");
    }
}
