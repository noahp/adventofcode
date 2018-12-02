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

fn walk(
    x: i32,
    y: i32,
    new_x: i32,
    new_y: i32,
    coords: &mut Vec<(i32, i32)>,
) -> ((i32, i32), bool) {
    // walk between points, appending each position as we go.
    // return the first point hit that already exists in the coords
    let mut result: (i32, i32) = (0, 0);
    let mut found_dupe: bool = false;

    println!("{}, {} -> {}, {}", x, y, new_x, new_y);

    if x != new_x {
        let distance = new_x - x;
        let range = 1..distance.abs() + 1;
        for i in range {
            let new_pos = (if distance > 0 {x + i} else {x - i}, y);
            println!("{:?}", new_pos);
            if !found_dupe && coords.contains(&new_pos) {
                result = new_pos;
                found_dupe = true;
            }
            coords.insert(0, new_pos);
        }
    } else if y != new_y {
        let distance = new_y - y;
        let range = 1..distance.abs() + 1;
        for i in range {
            let new_pos = (x, if distance > 0 {y + i} else {y - i});
            println!("{:?}", new_pos);
            if !found_dupe && coords.contains(&new_pos) {
                result = new_pos;
                found_dupe = true;
            }
            coords.insert(0, new_pos);
        }
    }

    return (result, found_dupe);
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
    let mut y: i32 = 0;
    let mut x: i32 = 0;
    let mut secondvisit: (i32, i32) = (0, 0);
    let mut found_second_visit: bool = false;

    let mut coords: Vec<(i32, i32)> = Vec::new();
    for step in vec {
        let (turn, distance) = step.split_at(1);
        let distance = distance.parse::<i32>().unwrap();

        print!("{} ", step);

        if turn == "L" {
            direction = decrement(direction, 3);
        } else {
            direction = increment(direction, 3);
        }

        let mut new_y: i32 = y;
        let mut new_x: i32 = x;

        match direction {
            0 => {
                new_y = y + distance;
            }
            1 => {
                new_x = x + distance;
            }
            2 => {
                new_y = y - distance;
            }
            3 => {
                new_x = x - distance;
            }
            _ => (),
        }

        // walk!
        println!("{} {}", new_x, new_y);
        let (result, found) = walk(x, y, new_x, new_y, &mut coords);
        if found {
            println!("found second visit: {:?}", result);
            if !found_second_visit {
                secondvisit = result.clone();
                found_second_visit = true;
            }
        }

        x = new_x;
        y = new_y;
    }

    // sum final x, y
    println!("####");
    println!("total delta: {}", x.abs() + y.abs());
    println!(
        "first second visit: {:?}, distance: {}",
        secondvisit,
        secondvisit.0.abs() + secondvisit.1.abs()
    );
}
