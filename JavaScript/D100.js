const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (input) => {
    const nums = input.split(' ').map(Number);
    const A = nums[0];
    const B = nums[1];

    const sum = A + B;

    console.log(sum);

    rl.close();
});
