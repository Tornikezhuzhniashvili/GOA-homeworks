function Age(age) {
    if (age < 18) {
        return "You are teenager";
    } else if (age >= 18 && age < 60) {
        return "You are an adult";
    } else {
        return "You are a senior";
    }
}
console.log(Age(15));
console.log(Age(30));
console.log(Age(70));