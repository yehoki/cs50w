const colors = ['red', 'green', 'blue'];
const items = colors.map(color => `<li>${color}</li>`);
console.log(items);

const address = {
    street: '',
    city: '',
    country: ''
};
//destructuring 

const {street: st} = address;
console.log(st);

// spread operator

const first = [1, 2, 3];
const second = [4, 5, 6];

//const combined = first.concat(second); <--- usual concat, spread operator is better

const combined = [...first, 'a', ...second, 'b'];

const clone = [...first];
console.log(first, clone);


