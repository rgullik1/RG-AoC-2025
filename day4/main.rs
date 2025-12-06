use std::fs;

fn vec_from_str(s: &str) -> Vec<i32> {
    s.chars().map(|c| match c {
        '@' => 1,
        '.' => 0,
        _ => -1,
    }).collect()
}

fn vecs_from_strs(strings: &[String]) -> Vec<Vec<i32>> {
    let mut acc_vec: Vec<Vec<i32>> = Vec::new();

    for s in strings {
        let v = vec_from_str(s.as_str());
        acc_vec.push(v);
    }
    return acc_vec;
}

fn strings_from_file(contents: &str) -> Vec<String> {
    contents.split_whitespace().map(|s| s.to_string()).collect()
}


fn main() {
    let bool_array = vec_from_str("..@@.@@@@.");


    let test_strings = ["..@@.", "@@@@.", ".@.@."].map(|s| s.to_string());
    let result = vecs_from_strs(&test_strings);
    // println!("{:?}", result);


    let contents = std::fs::read_to_string("realdata")
        .expect("Failed to read file");
    let str_array = strings_from_file(contents.as_str());
    let mut tp_grid = vecs_from_strs(&str_array);

    // println!("{:?}", tp_grid);

    for (i, row) in tp_grid.iter().enumerate() {
        for (j, value) in row.iter().enumerate() {
            // println!("tp_grid[{}][{}] = {}", i, j, value);
        }
    }
    let mut toilet_rolls = 0;
    let mut changed = true;

    while changed {
        changed = false;
        for i in 0..tp_grid.len() {
            for j in 0..tp_grid[i].len() {
                if tp_grid[i][j] == 1 {
                    let mut neighbor_sum = 0;
                    let neighbors = [
                        (i as i32 - 1, j as i32),
                        (i as i32 + 1, j as i32),
                        (i as i32, j as i32 - 1),
                        (i as i32, j as i32 + 1),
                        (i as i32 - 1, j as i32 - 1),
                        (i as i32 - 1, j as i32 + 1),
                        (i as i32 + 1, j as i32 - 1),
                        (i as i32 + 1, j as i32 + 1),
                    ];

                    for (ni, nj) in neighbors {
                        if ni >= 0 && ni < tp_grid.len() as i32 && nj >= 0 && nj < tp_grid[0].len() as i32 {
                            let neighbor_value = tp_grid[ni as usize][nj as usize];
                            neighbor_sum += neighbor_value;
                        }
                    }
                    if neighbor_sum < 4 {
                        toilet_rolls += 1;
                        tp_grid[i][j] = 0;
                        changed = true;
                    }
                }
            }
        }
    }
    println!("{}", toilet_rolls);
}
