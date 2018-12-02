use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader, Result};

fn main() -> Result<()> {
    let keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

    let args: Vec<String> = env::args().collect();

    if args.len() == 2 {
        // part 1
        let file = File::open(&args[1])?;
        for line in BufReader::new(file).lines() {
            let mut x: usize = 1;
            let mut y: usize = 1;

            for letter in line.unwrap().chars() {
                match letter {
                    'U' => {
                        // should use this instead :'( https://rust-num.github.io/num/num/trait.Bounded.html
                        y = if y > 0 { y - 1 } else { 0 }
                    }
                    'D' => y = if y < 2 { y + 1 } else { 2 },
                    'L' => x = if x > 0 { x - 1 } else { 0 },
                    'R' => x = if x < 2 { x + 1 } else { 0 },
                    _ => (),
                }
            }
            print!("{}", keypad[y][x]);
        }
        print!("\n");
    } else {
        // part 2
        // lol using -1 to mark unavailable positions >_<
        let keypad: [Box<[i32]>; 5] = [
            Box::new([-1, -1, 1, -1, -1]),
            Box::new([-1, 2, 3, 4, -1]),
            Box::new([5, 6, 7, 8, 9]),
            Box::new([-1, 0xA, 0xB, 0xC, -1]),
            Box::new([-1, -1, 0xD, -1, -1]),
        ];

        let file = File::open(&args[1])?;
        for line in BufReader::new(file).lines() {
            let mut x: usize = 1;
            let mut y: usize = 1;

            for letter in line.unwrap().chars() {
                match letter {
                    'U' => {
                        // should use this instead :'( https://rust-num.github.io/num/num/trait.Bounded.html
                        y = if y > 0 {
                            if keypad[y - 1][x] == -1 {
                                y
                            } else {
                                y - 1
                            }
                        } else {
                            y
                        };
                    }
                    'D' => {
                        y = if y < keypad.len() - 1 {
                            if keypad[y + 1][x] == -1 {
                                y
                            } else {
                                y + 1
                            }
                        } else {
                            y
                        };
                    }
                    'L' => {
                        x = if x > 0 {
                            if keypad[y][x - 1] == -1 {
                                x
                            } else {
                                x - 1
                            }
                        } else {
                            x
                        };
                    }
                    'R' => {
                        x = if x < keypad[y].len() - 1 {
                            if keypad[y][x + 1] == -1 {
                                x
                            } else {
                                x + 1
                            }
                        } else {
                            x
                        };
                    },
                    _ => (),
                }
            }
            print!("{:x}", keypad[y][x]);
        }
        print!("\n");
    }

    Ok(())
}
