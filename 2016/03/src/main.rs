use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader, Result};

fn is_triangle(a: u32, b: u32, c: u32) -> bool {
    if a + b <= c || a + c <= b || b + c <= a {
        return false;
    }
    return true;
}

fn main() -> Result<()> {
    let args: Vec<String> = env::args().collect();

    let mut valid_triangles: u32 = 0;
    let mut all_triangles: u32 = 0;

    if args.len() == 2 {
        // part 1
        let file = File::open(&args[1])?;
        for line in BufReader::new(file).lines() {
            let realline = line.unwrap();
            let dim = realline.split_whitespace().collect::<Vec<&str>>();

            if is_triangle(
                dim[0].parse::<u32>().unwrap(),
                dim[1].parse::<u32>().unwrap(),
                dim[2].parse::<u32>().unwrap(),
            ) {
                valid_triangles += 1;
            }

            all_triangles += 1;
        }
    } else if args.len() == 3 {
        // part 2
        let mut rows: Vec<[u32; 3]> = Vec::new();

        let file = File::open(&args[1])?;
        for line in BufReader::new(file).lines() {
            let realline = line.unwrap();
            let dim = realline.split_whitespace().collect::<Vec<&str>>();
            let mut append: Vec<[u32; 3]> = vec![
                [
                    dim[0].parse::<u32>().unwrap(),
                    dim[1].parse::<u32>().unwrap(),
                    dim[2].parse::<u32>().unwrap(),
                ],
            ];
            rows.append(&mut append);

            if rows.len() == 3 {
                for i in 0..3 {
                    // println!("{}, {}, {}", rows[0][i],
                    //     rows[1][i],
                    //     rows[2][i]);
                    if is_triangle(
                        rows[0][i],
                        rows[1][i],
                        rows[2][i],
                    ) {
                        valid_triangles += 1;
                    }
                }
                rows.clear();
            }

            all_triangles += 1;
        }
    }
    println!("{} / {}", valid_triangles, all_triangles);
    Ok(())
}
