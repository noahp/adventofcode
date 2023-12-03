
// this function takes the line vector and returns the sum of the first and
// last numerical digit in each line
fn part_one(lines: &Vec<String>) -> u32 {
    let mut sum = 0;
    for line in lines {
        let mut first = None;
        let mut last = None;
        for (_index, character) in line.char_indices() {
            if character.is_digit(10) {
                if first.is_none() {
                    // convert character to an integer
                    first = character.to_digit(10);
                }
                last = character.to_digit(10);
            }
        }
        // if we didn't find a first and last digit, print the offending line and crash
        if first.is_none() || last.is_none() {
            print!("{}", line);
            panic!("no digits found in line");
        }

        // combine the digits into a single number, of first*10 + last
        let number = first.unwrap()*10 + last.unwrap();
        sum += number;
    }
    sum
}

// part two also checks for first and last digits spelled out, "one", "two", etc.
fn part_two(lines: &Vec<String>) -> u32 {
    let mut sum = 0;
    for line in lines {
        let mut first = None;
        let mut last = None;
        for (_index, character) in line.char_indices() {
            if character.is_digit(10) {
                if first.is_none() {
                    // convert character to an integer
                    first = character.to_digit(10);
                }
                last = character.to_digit(10);
            }
        }
        // if we didn't find a first and last digit, print the offending line and crash
        if first.is_none() || last.is_none() {
            print!("{}", line);
            panic!("no digits found in line");
        }

        // combine the digits into a single number, of first*10 + last
        let number = first.unwrap()*10 + last.unwrap();
        sum += number;
    }
    sum
}


fn main() {
    // read lines from stdin into a vector
    let mut lines = Vec::new();
    loop {
        let mut line = String::new();
        match std::io::stdin().read_line(&mut line) {
            Ok(0) => break,
            Ok(_) => lines.push(line),
            Err(error) => panic!("{}", error),
        }
    }

    // part one
    let sum = part_one(&lines);
    println!("part one: {}", sum);

    // part two
    let sum = part_two(&lines);
    println!("part two: {}", sum);
}
