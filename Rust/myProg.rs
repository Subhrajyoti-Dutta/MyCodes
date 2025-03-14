// fn fib(n: i64) -> i64 {
//     if n == 0 || n == 1 {
//         return 1;
//     } else {
//         return fib(n-1) + fib(n-2);
//     }
// }

fn main() {
    let n = 9;  // No need for `mut`
    let t = true;
    let y = !t;
    let _u = Vec::<i32>::new();
    println!("The {}th fib is {}", n, y);
}