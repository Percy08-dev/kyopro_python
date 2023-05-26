use proconio::{input, fastout};

#[fastout]
fn main(){
    input!{
        n:usize, 
        q:usize,
        s:String,
        que:[(usize, usize);q], 
    }

    let mut p = 0;
    let s:Vec<char> = s.chars().collect();

    for (t, x) in que.iter() {
        if *t==1 {
            p = (p-x+n) % n;
        }else {
            println!("{}", s[(p+x-1)%n]);
        }
    }


}
