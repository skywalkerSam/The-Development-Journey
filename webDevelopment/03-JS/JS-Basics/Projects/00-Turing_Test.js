function find_max(nums) {
    let max_num = Number.NEGATIVE_INFINITY;  // smaller than all other numbes
    for (let num of nums) {
        if (num > max_num){
            // (Fill in the missing line here)
            console.log(max_num);
        }
    }
    return max_num;
}

console.log(find_max())


// max_num += num