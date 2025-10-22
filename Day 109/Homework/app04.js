let num = 10;
if (num > 10) {
    console.log("Big Number");
} else if (num < 10) {
    console.log("Small Number");
} else {
    console.log("Equal to 10");
}
let color = "red";

switch (color) {
    case "red":
        console.log("Stop!");
        break;
    case "yellow":
        console.log("Wait!")
        break;
    case "green":
        console.log("Go!")
        break;
    default:
        console.log("Unknown color");
}