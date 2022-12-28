// var used inside scope
// let within the same function
// const is used for read only, can't reassign it no matter what

function sayHello(n) {
    for (let i = 0; i < n; i++){
        console.log(i);
    }
}

//return sayHello(10);

// Objects: key value pairs
// Strings and functions (method of an object)

//const person = {
   // name: 'Pat',
    //walk() {},
    //talk: function() {}
//}

//two ways of defining a method

//two ways of accessing a method:

//person.walk();
//person['name'] = 'John';

//bracket notation useful when we don't know ahead of time the value

//const targetMember = 'name';
//person[targetMember] = 'John';




// 'this' keyword.

const person = {
    name: 'Pat',
    walk() {
        console.log(this);
    }
}
person.walk();

const walk = person.walk.bind(person);
console.log(walk);
walk();


const square = function(number) {
    return number * number;
}

const squareNew = number => number * number ;
console.log(squareNew(5));


const jobs = [
    {id:1, isActive: true},
    {id:2, isActive: true},
    {id:1, isActive: false},
];

const activeJobs = jobs.filter(job => job.isActive);
console.log(activeJobs);


//arrow functions don't rebind this

const newPerson = {
    talk() {
        setTimeout(() => {
            console.log("this", this);
        }, 1000);
    }
};

newPerson.talk();