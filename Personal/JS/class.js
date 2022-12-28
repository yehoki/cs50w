class Person {
    constructor(name){
        this.name = name;
    }

    walk() {
        console.log("walk");
    }
}

const person = new Person("Patryk");
console.log(person.name);


// Inheritance and composition
// Inherit previous class
//super initializes the parent class
class Teacher extends Person{
    constructor(name, degree) {
        super(name);
        this.degree = degree;
    }

    teach() {
        console.log("teach");
    }
}

const teacher = new Teacher("Patryk","MMath");
console.log(teacher);
