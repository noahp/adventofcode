// --- Day 1: No Time for a Taxicab ---
// Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.
//
// Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
//
// You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.
//
// The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.
//
// There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?
//
// For example:
//
// Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
// R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
// R5, L5, R5, R3 leaves you 12 blocks away.
// How many blocks away is Easter Bunny HQ?

fn decrement(val: i32, max: i32) -> i32 {
    if val == 0 {
        return max;
    } else {
        return val - 1;
    }
}

fn increment(val: i32, max: i32) -> i32 {
    if val == max {
        return 0;
    } else {
        return val + 1;
    }
}

fn main() {
    // puzzle input
    let vec = vec![
        "L1", "L3", "L5", "L3", "R1", "L4", "L5", "R1", "R3", "L5", "R1", "L3", "L2", "L3", "R2",
        "R2", "L3", "L3", "R1", "L2", "R1", "L3", "L2", "R4", "R2", "L5", "R4", "L5", "R4", "L2",
        "R3", "L2", "R4", "R1", "L5", "L4", "R1", "L2", "R3", "R1", "R2", "L4", "R1", "L2", "R3",
        "L2", "L3", "R5", "L192", "R4", "L5", "R4", "L1", "R4", "L4", "R2", "L5", "R45", "L2",
        "L5", "R4", "R5", "L3", "R5", "R77", "R2", "R5", "L5", "R1", "R4", "L4", "L4", "R2", "L4",
        "L1", "R191", "R1", "L1", "L2", "L2", "L4", "L3", "R1", "L3", "R1", "R5", "R3", "L1", "L4",
        "L2", "L3", "L1", "L1", "R5", "L4", "R1", "L3", "R1", "L2", "R1", "R4", "R5", "L4", "L2",
        "R4", "R5", "L1", "L2", "R3", "L4", "R2", "R2", "R3", "L2", "L3", "L5", "R3", "R1", "L4",
        "L3", "R4", "R2", "R2", "R2", "R1", "L4", "R4", "R1", "R2", "R1", "L2", "L2", "R4", "L1",
        "L2", "R3", "L3", "L5", "L4", "R4", "L3", "L1", "L5", "L3", "L5", "R5", "L5", "L4", "L2",
        "R1", "L2", "L4", "L2", "L4", "L1", "R4", "R4", "R5", "R1", "L4", "R2", "L4", "L2", "L4",
        "R2", "L4", "L1", "L2", "R1", "R4", "R3", "R2", "R2", "R5", "L1", "L2",
    ];

    let mut direction: i32 = 0;
    let mut y: i32 = 0i32;
    let mut x: i32 = 0;
    for step in vec {
        let (turn, distance) = step.split_at(1);
        let distance = distance.parse::<i32>().unwrap();

        print!("{} ", step);

        if turn == "L" {
            direction = decrement(direction, 3);
        } else {
            direction = increment(direction, 3);
        }

        match direction {
            0 => {
                y = y + distance;
            }
            1 => {
                x = x + distance;
            }
            2 => {
                y = y - distance;
            }
            3 => {
                x = x - distance;
            }
            _ => (),
        }
        println!("{} {}", x, y);
    }

    // sum final x, y
    println!("delta: {}", x.abs() + y.abs());
}
